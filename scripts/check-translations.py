#!/usr/bin/env python3
"""Check translation coverage and non-prose invariants without network requests."""
import json
import re
from pathlib import Path


def pages(root):
    return {p.relative_to(root): p for p in root.rglob('*')
            if p.suffix in ('.md', '.html')}


def code_blocks(text):
    # Prose inside a Mermaid diagram is translated; executable examples are not.
    return [block for block in re.findall(r'^\s*```([^\n]*\n.*?)^\s*```', text, re.M | re.S)
            if not block.startswith('mermaid\n')]


def external_links(text):
    return {url.rstrip("`'.,") for url in re.findall(r'https?://[^\s<>\")]+', text)}


def check():
    english = pages(Path('content/en'))
    german = pages(Path('content/de'))
    assert english.keys() == german.keys(), {
        'missing': sorted(english.keys() - german.keys()),
        'extra': sorted(german.keys() - english.keys()),
    }
    for path, source in english.items():
        en, de = source.read_text(), german[path].read_text()
        assert code_blocks(en) == code_blocks(de), f'Changed executable example: {path}'
        assert external_links(en) == external_links(de), (
            path, external_links(en) ^ external_links(de))
        for pattern in (
            r'{{[%<]\s*relref\s+"([^"]+)"',
            r'include-markdown\s+file="([^"]+)"',
            r'image-gallery\s+gallery_dir="([^"]+)"',
            r'^date:\s*(.*)$', r'^author:\s*(.*)$',
        ):
            assert sorted(re.findall(pattern, en, re.M)) == sorted(re.findall(pattern, de, re.M)), (path, pattern)
        for language, text in [('en', en), ('de', de)]:
            assert re.match(r'\A---\n.*?\n---(?:\n|$)', text, re.S), (path, language)
    captions = json.loads(Path('assets/json/gallery-captions-de.json').read_text())
    for source in english.values():
        for directory in re.findall(r'image-gallery\s+gallery_dir="([^"]+)"', source.read_text()):
            for image in (source.parent / directory).iterdir():
                if image.is_file():
                    assert image.stem in captions, f'Missing German gallery caption: {image}'
    print(f'Passed: {len(english)} translation pairs, code blocks, links, includes, dates, authors, and gallery captions')


if __name__ == '__main__':
    check()
