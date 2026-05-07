"""Extract Framer-rendered articles into clean markdown.

Usage: python3 extract_articles.py
Writes to ../articles/*.md relative to this script (i.e. scrape/articles/).
"""
from __future__ import annotations

import os
import re
from bs4 import BeautifulSoup, Comment, NavigableString, Tag

BASE = '/Users/agent/my/nostr/flotilla-website/scrape'
RAW_DIR = os.path.join(BASE, 'raw')
OUT_DIR = os.path.join(BASE, 'articles')
ASSETS_DIR = os.path.join(BASE, 'assets')

ARTICLE_FILES = [
    # (slug, source_filename)
    ('what-is-flotilla', 'article-what-is-flotilla.html'),
    ('getting-started', 'article-getting-started.html'),
    ('joining-a-space', 'article-joining-a-space.html'),
    ('is-flotilla-private', 'article-is-flotilla-private.html'),
    ('community-and-support', 'article-community-and-support.html'),
    ('creating-a-space', 'article-creating-a-space.html'),
    ('self-hosting-a-space', 'article-self-hosting-a-space.html'),
    ('managing-a-space', 'article-managing-a-space.html'),
    ('running-a-community', 'article-running-a-community.html'),
]


# Inferred from the index/sidebar structure of articles.html.
# what-is-flotilla appears as the featured/hero card and lacks an explicit
# category section, so we omit a category for it.
CATEGORY_ORDERING = {
    'basics': [
        'getting-started',
        'joining-a-space',
        'is-flotilla-private',
        'community-and-support',
    ],
    'advanced': [
        'creating-a-space',
        'self-hosting-a-space',
        'managing-a-space',
        'running-a-community',
    ],
}


def category_for(slug: str) -> str | None:
    for cat, items in CATEGORY_ORDERING.items():
        if slug in items:
            return cat
    return None


def order_for(slug: str) -> int:
    """Stable order across categories so Astro can sort by it.

    1: what-is-flotilla (featured)
    2..5: Basics
    6..8: Advanced
    """
    if slug == 'what-is-flotilla':
        return 1
    if slug in CATEGORY_ORDERING['basics']:
        return 2 + CATEGORY_ORDERING['basics'].index(slug)
    if slug in CATEGORY_ORDERING['advanced']:
        return 6 + CATEGORY_ORDERING['advanced'].index(slug)
    return 99


# ---------------------------------------------------------------------------
# Inline conversion
# ---------------------------------------------------------------------------

def _inline(node, in_link: bool = False) -> str:
    """Convert a tag's inline children to markdown.

    Handles <strong>, <em>, <code>, <a>, <br>, plus nested combos.
    Does NOT handle block-level (p/ul/ol/h*/img/pre/div) — caller dispatches.
    """
    if isinstance(node, Comment):
        # Strip React SSR markers like <!--$--> and <!--/$-->.
        return ''
    if isinstance(node, NavigableString):
        return str(node)

    name = node.name
    if name == 'br':
        return '  \n'

    if name == 'strong' or name == 'b':
        inner = ''.join(_inline(c, in_link) for c in node.children)
        # avoid empty bold
        if not inner.strip():
            return inner
        return f'**{inner}**'

    if name == 'em' or name == 'i':
        inner = ''.join(_inline(c, in_link) for c in node.children)
        if not inner.strip():
            return inner
        return f'*{inner}*'

    if name == 'code':
        # Inline code: take literal text content (no further markdown inside).
        text = node.get_text()
        # If code text contains backticks, use double-backtick wrapper.
        if '`' in text:
            return f'`` {text} ``'
        return f'`{text}`'

    if name == 'a':
        href = node.get('href') or ''
        inner = ''.join(_inline(c, in_link=True) for c in node.children).strip()
        if not inner:
            inner = href
        # Rewrite internal article links: ./other-slug stays the same;
        # /articles/other-slug becomes ./other-slug.
        if href.startswith('./articles/'):
            href = './' + href[len('./articles/'):]
        elif href.startswith('/articles/'):
            href = './' + href[len('/articles/'):]
        # Sibling-page references like ./other-slug already have the right shape.
        return f'[{inner}]({href})'

    if name == 'span':
        # transparent wrapper
        return ''.join(_inline(c, in_link) for c in node.children)

    # Some inline elements come through as <p> nested inside <li>: caller handles.
    # Fallback: just take inner text.
    return ''.join(_inline(c, in_link) for c in node.children)


def _clean_text(s: str) -> str:
    """Collapse Framer's stray whitespace inside paragraphs.

    Preserves intentional double-newlines (we don't introduce them mid-paragraph).
    """
    # Replace non-breaking spaces with normal spaces.
    s = s.replace(' ', ' ')
    # Collapse runs of spaces/tabs (not newlines).
    s = re.sub(r'[ \t]+', ' ', s)
    # Trim each line.
    lines = [ln.strip() for ln in s.split('\n')]
    return '\n'.join(lines).strip()


# ---------------------------------------------------------------------------
# Block conversion
# ---------------------------------------------------------------------------

LANG_HINTS = {
    # Heuristic: detect a fenced-block language from the code's first line.
    'sudo apt': 'bash',
    'version:': 'yaml',
    'server {': 'nginx',
    'host = ': 'toml',
}


def _detect_lang(code: str) -> str:
    text = code.lstrip()
    for prefix, lang in LANG_HINTS.items():
        if text.startswith(prefix):
            return lang
    if 'apt ' in text and text.startswith('sudo'):
        return 'bash'
    return ''


def _img_block(node: Tag, used_images: list[dict]) -> str:
    src = node.get('src') or ''
    alt = node.get('alt') or ''
    m = re.search(r'/images/([^?]+)', src)
    if not m:
        # Skip non-Framer images (shouldn't happen in article bodies).
        return ''
    filename = m.group(1)
    used_images.append({
        'local': f'../assets/{filename}',
        'original': f'https://framerusercontent.com/images/{filename}',
        'alt': alt,
    })
    return f'![{alt}](../assets/{filename})'


def _list_block(node: Tag, ordered: bool) -> str:
    out = []
    marker = '1.' if ordered else '-'
    for i, li in enumerate(node.find_all('li', recursive=False), 1):
        # A li may contain a single <p> (Framer wraps inline content in <p>).
        # Convert children inline; if it has nested ul/ol, indent them.
        parts = []
        for child in li.children:
            if isinstance(child, Comment):
                continue
            if isinstance(child, NavigableString):
                t = str(child)
                if t.strip():
                    parts.append(t)
                continue
            if not isinstance(child, Tag):
                continue
            if child.name in ('ul', 'ol'):
                nested = _list_block(child, ordered=child.name == 'ol')
                # indent nested by 4 spaces
                indented = '\n'.join('    ' + ln if ln else '' for ln in nested.split('\n'))
                parts.append('\n' + indented)
            elif child.name == 'p':
                parts.append(''.join(_inline(c) for c in child.children))
            else:
                parts.append(_inline(child))
        text = ''.join(parts)
        text = _clean_text(text)
        m = marker if not ordered else f'{i}.'
        out.append(f'{m} {text}')
    return '\n'.join(out)


def _code_block_from_div(div: Tag) -> tuple[str, str]:
    """Extract literal code text from a Framer code-block container.

    The container has TWO inner <pre> elements (Framer's SSR + client placeholders);
    they have identical content. We return the text of the first plus a detected lang.
    """
    pre = div.find('pre')
    code = pre.get_text() if pre else ''
    # Some code blocks include trailing blank chars; preserve as-is.
    return code, _detect_lang(code)


def _heading(node: Tag) -> str:
    level = int(node.name[1])
    text = ''.join(_inline(c) for c in node.children).strip()
    # Skip empty headings.
    if not text:
        return ''
    return f'{"#" * level} {text}'


def _paragraph(node: Tag) -> str:
    parts = []
    for child in node.children:
        if isinstance(child, Comment):
            continue
        if isinstance(child, NavigableString):
            parts.append(str(child))
        elif isinstance(child, Tag):
            if child.name == 'img':
                # Inline image inside paragraph — promote it to its own block.
                # (We lose the prose split, but Framer rarely mixes both.)
                pass  # handled by caller via separate img scan
            else:
                parts.append(_inline(child))
    text = ''.join(parts)
    return _clean_text(text)


def _blockquote(node: Tag) -> str:
    # Convert children to markdown blocks, prefix each line with '> '.
    inner_blocks = _convert_blocks(node, used_images=[])
    return '\n'.join('> ' + ln if ln else '>' for ln in inner_blocks.split('\n'))


def _is_code_block_div(node: Tag) -> bool:
    return node.name == 'div' and 'framer-text-module' in (node.get('class') or [])


def _convert_blocks(container: Tag, used_images: list[dict]) -> str:
    blocks: list[str] = []
    for child in container.children:
        if isinstance(child, Comment):
            continue
        if isinstance(child, NavigableString):
            t = str(child).strip()
            if t:
                blocks.append(_clean_text(t))
            continue
        if not isinstance(child, Tag):
            continue

        name = child.name
        if name in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            h = _heading(child)
            if h:
                blocks.append(h)
        elif name == 'p':
            # Paragraph may contain an inline <img>. Split: text before, img, text after.
            inner_imgs = child.find_all('img', recursive=False)
            if inner_imgs:
                # Walk: emit text segments + image blocks in document order.
                buf = []
                def flush():
                    if buf:
                        s = _clean_text(''.join(buf))
                        if s:
                            blocks.append(s)
                        buf.clear()
                for c in child.children:
                    if isinstance(c, Comment):
                        continue
                    if isinstance(c, Tag) and c.name == 'img':
                        flush()
                        ib = _img_block(c, used_images)
                        if ib:
                            blocks.append(ib)
                    else:
                        buf.append(str(c) if isinstance(c, NavigableString) else _inline(c))
                flush()
            else:
                p = _paragraph(child)
                if p:
                    blocks.append(p)
        elif name == 'ul':
            blocks.append(_list_block(child, ordered=False))
        elif name == 'ol':
            blocks.append(_list_block(child, ordered=True))
        elif name == 'img':
            ib = _img_block(child, used_images)
            if ib:
                blocks.append(ib)
        elif name == 'blockquote':
            blocks.append(_blockquote(child))
        elif _is_code_block_div(child):
            code, lang = _code_block_from_div(child)
            blocks.append(f'```{lang}\n{code}\n```')
        elif name == 'div':
            # Other Framer divs: treat transparently (recurse into children).
            sub = _convert_blocks(child, used_images)
            if sub:
                blocks.append(sub)
        elif name == 'pre':
            # Standalone <pre> (rare). Use literal text.
            code = child.get_text()
            lang = _detect_lang(code)
            blocks.append(f'```{lang}\n{code}\n```')
        elif name == 'figure':
            sub = _convert_blocks(child, used_images)
            if sub:
                blocks.append(sub)
        else:
            # Unknown tag — fall back to inline conversion.
            t = _inline(child)
            if t.strip():
                blocks.append(_clean_text(t))

    # Filter empty
    return '\n\n'.join(b for b in blocks if b)


# ---------------------------------------------------------------------------
# Per-article driver
# ---------------------------------------------------------------------------

def yaml_escape(s: str) -> str:
    if s is None:
        return ''
    s = s.replace('\\', '\\\\').replace('"', '\\"')
    return s


def extract_article(slug: str, fname: str) -> dict:
    path = os.path.join(RAW_DIR, fname)
    with open(path, encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Title from the article H2 (Framer uses h2 for the article heading; H1 is reserved
    # for the page brand).
    title_el = soup.find('h2')
    title = title_el.get_text(strip=True) if title_el else slug

    # Description: meta name=description (used as hero subtitle on Framer).
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    description = meta_desc.get('content', '').strip() if meta_desc else ''

    content_el = soup.select_one('[data-framer-name="Content"]')
    if content_el is None:
        raise RuntimeError(f'No Content block in {fname}')

    used_images: list[dict] = []
    body_md = _convert_blocks(content_el, used_images)

    return {
        'slug': slug,
        'title': title,
        'description': description,
        'category': category_for(slug),
        'order': order_for(slug),
        'body': body_md,
        'images': used_images,
    }


def render_article(article: dict) -> str:
    fm_lines = [
        '---',
        f'title: "{yaml_escape(article["title"])}"',
        f'slug: {article["slug"]}',
        f'source: https://flotilla.social/articles/{article["slug"]}',
        f'description: "{yaml_escape(article["description"])}"',
        f'order: {article["order"]}',
    ]
    if article['category']:
        fm_lines.append(f'category: {article["category"]}')
    fm_lines.append('---')
    front = '\n'.join(fm_lines)

    out = [front, '', f'# {article["title"]}', '', article['body']]

    if article['images']:
        # Dedup by local path
        seen = set()
        rows = []
        for img in article['images']:
            key = img['local']
            if key in seen:
                continue
            seen.add(key)
            usage = 'inline body image'
            alt = img['alt'] or ''
            rows.append(f'| {img["local"]} | {img["original"]} | {alt} | {usage} |')
        out += [
            '',
            '## Images',
            '',
            '| local | original | alt | usage |',
            '|---|---|---|---|',
            *rows,
        ]

    return '\n'.join(out).rstrip() + '\n'


# ---------------------------------------------------------------------------
# Index page
# ---------------------------------------------------------------------------

INDEX_DESCRIPTIONS = {
    # Pulled from the article hero/description text observed during scraping.
    # Falls back to the article's meta description when not overridden.
}


def extract_index(articles: list[dict]) -> str:
    # Build the index from the scraped index.html: pull H2 headline, intro paragraph,
    # then list articles by category in the order they appear in the sidebar.
    idx_path = os.path.join(RAW_DIR, 'articles.html')
    with open(idx_path, encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    h2 = soup.find('h2')
    page_title = h2.get_text(strip=True) if h2 else 'Knowledge Base'

    meta_desc = soup.find('meta', attrs={'name': 'description'})
    description = meta_desc.get('content', '').strip() if meta_desc else ''

    by_slug = {a['slug']: a for a in articles}

    lines = [
        '---',
        f'title: "{yaml_escape(page_title)}"',
        'slug: articles',
        'source: https://flotilla.social/articles',
        f'description: "{yaml_escape(description)}"',
        '---',
        '',
        f'# {page_title}',
        '',
    ]

    # Featured / intro
    if 'what-is-flotilla' in by_slug:
        wif = by_slug['what-is-flotilla']
        lines.append('## Featured')
        lines.append('')
        lines.append(f'- [{wif["title"]}](./{wif["slug"]})')
        lines.append('')

    # Basics
    lines.append('## The Basics')
    lines.append('')
    for slug in CATEGORY_ORDERING['basics']:
        if slug in by_slug:
            a = by_slug[slug]
            lines.append(f'- [{a["title"]}](./{a["slug"]})')
    lines.append('')

    # Advanced
    lines.append('## Advanced')
    lines.append('')
    for slug in CATEGORY_ORDERING['advanced']:
        if slug in by_slug:
            a = by_slug[slug]
            lines.append(f'- [{a["title"]}](./{a["slug"]})')
    # Note any sidebar entries we don't have HTML for.
    extras = [s for s in CATEGORY_ORDERING['advanced'] if s not in by_slug]
    # The live index also lists running-a-community with no scraped HTML — surface it.
    if 'running-a-community' not in by_slug:
        lines.append('- [Running a Community](./running-a-community) <!-- not scraped -->')
    lines.append('')

    return '\n'.join(lines).rstrip() + '\n'


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    articles = []
    for slug, fname in ARTICLE_FILES:
        art = extract_article(slug, fname)
        articles.append(art)
        out_path = os.path.join(OUT_DIR, f'{slug}.md')
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(render_article(art))
        wc = len(art['body'].split())
        print(f'wrote {slug}.md  words={wc}  imgs={len(art["images"])}')

    idx_md = extract_index(articles)
    with open(os.path.join(OUT_DIR, '_index.md'), 'w', encoding='utf-8') as f:
        f.write(idx_md)
    print(f'wrote _index.md')


if __name__ == '__main__':
    main()
