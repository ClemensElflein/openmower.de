# English and German

English remains the default language. Production URLs keep the existing structure:

| Page | English | German |
| --- | --- | --- |
| Homepage | `/` | `/de/` |
| Documentation | `/latest/docs/` | `/latest/de/docs/` |
| Updates | `/latest/updates/` | `/latest/de/updates/` |
| Community | `/latest/community/` | `/latest/de/community/` |

The language menu links to the matching page. If a future page has no translation,
its menu link falls back to the other language's homepage. There is no automatic
language redirect.

## Editing translations

Keep matching file paths under `content/en` and `content/de`. Hugo uses those paths
to associate translations. English URL slugs remain unchanged in German so links
and page associations are stable.

German copy uses natural, direct language and a consistent informal “du”. Preserve
qualifications, warnings, historical context, compatibility limits, quantities,
units, and instructions. Translate prose, captions, alt text, and descriptions.
Keep commands, filenames, URLs, configuration keys and values, and actual UI button
names intact. If the English source appears incorrect, flag it and resolve it in
both languages rather than silently changing only the translation.

Images, recordings, and downloadable configuration files live with the English
bundles. Hugo mounts their non-page resources into the German content tree too.
Do not duplicate those binaries. Gallery captions are translated in
`assets/json/gallery-captions-de.json`; the gallery reads Hugo page resources,
so both languages work with these shared files. Text inside existing screenshots,
diagrams, and terminal recordings retains the original language.

General UI strings live in `i18n/en.toml` and `i18n/de.toml`, with Docsy supplying
its existing translations. Consent-dialog strings live in
`layouts/partials/hooks/body-end.html`. Search uses a separate index per language.

Preserve explicit heading IDs used by links, such as
`{#plan-the-total-build-cost}`, when rewording a heading.

## Publishing and validation

Use Hugo **0.111.3 extended**, matching CI, and install the package dependencies.
Build into fresh output directories: `prepare-pages.py` intentionally rejects
redirects that would overwrite existing files.

```sh
hugo --minify --baseURL https://openmower.de/latest/ --destination /tmp/openmower-build/latest
python3 scripts/prepare-pages.py --latest /tmp/openmower-build/latest --root /tmp/openmower-build/root
python3 scripts/check-translations.py
python3 scripts/check-pages.py --latest /tmp/openmower-build/latest --root /tmp/openmower-build/root
```

The preparation script publishes both homepages at the origin and redirects their
`/latest/` duplicates. The root sitemap contains both languages, with reciprocal
`hreflang` links and English as `x-default`. Archive builds stay `noindex` and omit
language alternates from indexing signals.

The translation check verifies all 83 source/translation pairs, executable code
blocks, external links, page references, included content, dates, authors, and
gallery-caption coverage. It does not replace a language and factual review.
The SEO check validates both languages' metadata, sitemap entries, redirects,
internal assets, and language-isolated search indexes.
