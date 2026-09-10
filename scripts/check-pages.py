#!/usr/bin/env python3
"""Check a prepared root/latest deployment without making network requests."""
import argparse
import csv
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.canonical = []
        self.robots = []
        self.refresh = []
        self.links = []
        self.h1 = 0
        self.title = ''
        self.in_title = False
        self.og_url = None
        self.description = ''
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'h1':
            self.h1 += 1
        if tag == 'title':
            self.in_title = True
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical.append(a['href'])
        if tag == 'meta':
            if a.get('name') == 'robots':
                self.robots.append(a['content'])
            if a.get('name') == 'description':
                self.description = a['content']
            if a.get('http-equiv', '').lower() == 'refresh':
                self.refresh.append(a['content'])
            if a.get('property') == 'og:url':
                self.og_url = a['content']
        if tag == 'a' and 'href' in a:
            self.links.append(a['href'])
        if tag in ('img', 'script') and 'src' in a:
            self.links.append(a['src'])
        if tag == 'link' and a.get('rel') == 'stylesheet':
            self.links.append(a['href'])

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, text):
        if self.in_title:
            self.title += text


def check(latest, root, origin, inventory):
    origin = origin.rstrip('/')

    def local(url):
        path = unquote(urlsplit(url).path)
        file = latest / path.removeprefix('/latest/') if path.startswith('/latest/') else root / path.lstrip('/')
        return file / 'index.html' if path.endswith('/') else file

    urls = [e.text for e in ET.parse(root / 'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    assert origin + '/' in urls and origin + '/latest/' not in urls
    assert len(urls) == len(set(urls)), 'Duplicate sitemap URLs'
    titles = defaultdict(list)
    for url in urls:
        page = Page(local(url))
        assert not page.refresh, url
        assert page.canonical == [url], (url, page.canonical)
        assert page.robots == ['index, follow'], (url, page.robots)
        assert page.h1 == 1 and page.description.strip(), url
        assert page.og_url == url, (url, page.og_url)
        titles[page.title].append(url)
        if url != origin + '/':
            assert page.title.endswith(' | OpenMower'), (url, page.title)
        for link in page.links:
            target = urljoin(url, link)
            parsed = urlsplit(target)
            if parsed.netloc != urlsplit(origin).netloc or parsed.path.startswith('/archive/'):
                continue
            assert local(target).is_file(), (url, link)
    assert all(len(v) == 1 for v in titles.values()), dict(titles)
    assert f'Sitemap: {origin}/sitemap.xml' in (root / 'robots.txt').read_text()
    assert (root / 'sitemap.xml').read_bytes() == (latest / 'sitemap.xml').read_bytes()
    for route in ('search/', 'tags/', 'tags/mapping/', 'categories/'):
        url = origin + '/latest/' + route
        assert url not in urls
        assert Page(local(url)).robots == ['noindex, follow'], url
    rows = list(csv.DictReader(inventory.open()))
    rows.append({'old_path': '/latest/', 'replacement_path': '/'})
    for row in rows:
        target = origin + row['replacement_path']
        page = Page(local(origin + row['old_path']))
        assert page.canonical == [target], row
        assert page.refresh == [f'0; url={target}'], row
        assert not Page(local(target)).refresh, row
    home = (root / 'index.html').read_text()
    for asset in ('asciinema-player', 'carousel.js', 'carousel.css', 'medium-zoom'):
        assert asset not in home, asset
    print(f'Passed: {len(urls)} sitemap pages, {len(rows)} redirects, metadata, headings, internal links/assets, and indexing rules')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--latest', type=Path, default=Path('public'))
    parser.add_argument('--root', type=Path, default=Path('public-root'))
    parser.add_argument('--origin', default='https://openmower.de')
    parser.add_argument('--inventory', type=Path, default=Path('data/redirects.csv'))
    args = parser.parse_args()
    check(args.latest, args.root, args.origin, args.inventory)
