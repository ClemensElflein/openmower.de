#!/usr/bin/env python3
"""Prepare GitHub Pages root files and exact HTML redirects after a latest build.

GitHub Pages cannot configure HTTP 301s. These pages use immediate refresh,
canonical markup, and a visible fallback link. Never run this on archive builds.
"""
import argparse
import csv
import html
import shutil
from pathlib import Path
from urllib.parse import urlsplit


def redirect_page(target):
    target = html.escape(target, quote=True)
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<title>Page moved | OpenMower</title>'
            f'<link rel="canonical" href="{target}">'
            f'<meta http-equiv="refresh" content="0; url={target}">'
            f'</head><body><p>This page has moved. <a href="{target}">'
            'Continue to OpenMower</a>.</p></body></html>\n')


def prepare(latest, root, origin, inventory):
    origin = origin.rstrip('/')
    parsed = urlsplit(origin)
    if parsed.scheme not in ('http', 'https') or not parsed.netloc or parsed.path:
        raise ValueError('origin must be an HTTP(S) origin without a path')
    planned = []
    with inventory.open() as source:
        for row in csv.DictReader(source):
            old, target = row['old_path'], row['replacement_path']
            for path in (old, target):
                if not path.startswith('/') or not path.endswith('/') or '..' in path or '//' in path:
                    raise ValueError(f'Invalid route: {path}')
            if not target.startswith('/latest/') or old == target:
                raise ValueError(f'Invalid redirect: {old} -> {target}')
            replacement = latest / target.removeprefix('/latest/') / 'index.html'
            if not replacement.is_file() or 'http-equiv="refresh"' in replacement.read_text():
                raise ValueError(f'Missing or non-final target: {target}')
            output = (latest / old.removeprefix('/latest/') if old.startswith('/latest/')
                      else root / old.lstrip('/')) / 'index.html'
            if output.exists():
                raise ValueError(f'Redirect would overwrite an existing page: {output}')
            planned.append((output, origin + target))
    root.mkdir(parents=True, exist_ok=True)
    for name in ('index.html', 'sitemap.xml', 'robots.txt'):
        shutil.copyfile(latest / name, root / name)
    for output, target in planned:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(redirect_page(target))
    print(f'Prepared root files and {len(planned)} historical redirects')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--latest', type=Path, default=Path('public'))
    parser.add_argument('--root', type=Path, default=Path('public-root'))
    parser.add_argument('--origin', default='https://openmower.de')
    parser.add_argument('--inventory', type=Path, default=Path('data/redirects.csv'))
    args = parser.parse_args()
    prepare(args.latest, args.root, args.origin, args.inventory)
