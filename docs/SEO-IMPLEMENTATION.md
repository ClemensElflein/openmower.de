# SEO audit implementation

Local implementation of the 9 September 2026 audit. Nothing has been pushed or deployed.

## Repository fixes

| Audit finding | Implementation |
| --- | --- |
| Historical documentation URLs | `data/redirects.csv` maps 91 routes, including all 19 verified knowledge-base moves, older root `/docs/` routes, conversion-guide renames, and version-specific YardForce guides. Git rename chains were followed to current files. |
| Homepage discovery content | Descriptive H1, direct beginner and build links, compatibility, budget components, skills, setup steps, RTK limitations, an existing build photo, and the original mowing demonstration. Cost and RTK entry pages were expanded. |
| Homepage canonical signals | `/` is the homepage canonical, Open Graph URL, application URL, sitemap entry, and internal home destination. Only the duplicate `/latest/` homepage redirects to `/`; documentation paths stay under `/latest/docs/`. Preview prefixes and archive canonical paths are retained. |
| Effective robots output | A Hugo robots template advertises the canonical sitemap; the shadowed static file was removed. |
| Search and thin listings | Search and taxonomy pages have `noindex, follow` and are absent from the sitemap. `map` and `maps` were consolidated into `mapping`, with aliases for the former tag URLs. |
| Duplicate and repetitive titles | Unique beginner/index titles, carrier-board version labels for Classic 500(B), and a short `OpenMower` suffix. |
| Generic descriptions | Page-specific summaries for the homepage's main beginner, compatibility, cost, RTK, and troubleshooting resources. |
| Heading hierarchy | One H1 per rendered page; section headings and search/updates listings corrected. The compatibility check links to the detailed model guide instead of repeating it. |
| Globally loaded feature assets | Asciinema is enabled explicitly on recording pages; carousel assets follow shortcode use; zoom loads when content contains zoomable images. The homepage loads none of these assets. |
| Conflicting archive directives | One `noindex, follow` directive per archive page. Archive pages are omitted from newly generated archive sitemaps. |

GitHub Pages cannot configure HTTP 301 responses through this repository. The redirects use immediate HTML refresh, canonical markup, and a visible destination link. They return HTTP 200 on static hosting. The preparation script rejects missing targets, redirect chains, collisions, and reuse of an already prepared build. It runs only for main-branch deployments.

The historical inventory is based on the audit and recoverable Git renames. It does not claim to cover every externally linked URL. Deleted pages without a clear surviving equivalent need individual review; they were not redirected indiscriminately.

## Validation

Tested with Hugo Extended 0.111.3, matching the deployment workflow:

- Production build and assembled root/latest deployment passed `scripts/check-pages.py`: 81 sitemap pages and 92 redirects (91 historical routes plus the duplicate homepage).
- Canonical URLs, Open Graph URLs, unique titles, descriptions, robots directives, H1s, internal page links, and referenced image/script/stylesheet files passed checks. External destinations, fragments, and existing archive files are outside this automated link check.
- All 101 non-redirect index pages had one H1 before root/latest assembly.
- Archive build verified a single noindex directive, preserved archive canonicals, and an empty sitemap.
- Recording pages retained the player, the overview retained its carousel, and illustrated documentation retained zoom. The homepage omitted these assets.
- Mobile homepage visually checked at 390 × 844. This is a layout smoke test, not a Core Web Vitals measurement.

After a fresh production Hugo build with `baseURL = "https://openmower.de/latest/"`, run:

```sh
python3 scripts/prepare-pages.py
python3 scripts/check-pages.py
```

The defaults read `public/` and prepare `public-root/`. Both scripts accept `--latest`, `--root`, and `--origin` for temporary build directories and another deployment origin. Rebuild into clean directories before repeating preparation. The GitHub Pages workflow now runs both commands before any main-branch deployment.

## Follow-ups requiring account data or an audience decision

1. **Search Console measurement:** Export query/page/country/device performance, separate branded and non-branded traffic, and compare the November 2025 and June 2026 migrations with seasonal and year-over-year context. No Search Console account data was available in this task.
2. **Backlinks and project profiles:** Export linked pages and referring sites. Classify destinations as root homepage, current docs, retired routes, GitHub, or older sites; extend the redirect inventory where an exact successor exists. The [main project README](https://github.com/ClemensElflein/OpenMower#readme), checked on 9 September 2026, already prominently links to openmower.de. No profile changes or editorial outreach were made.
3. **German-language content:** Deferred pending a target-audience decision. If Germany is a priority, translate substantial homepage and beginner content with separate URLs, reciprocal hreflang, and language navigation. No domain migration is proposed.
4. **Current build pricing:** The existing approximately €700 conversion estimate is now explicitly labelled as an earlier estimate with exclusions. The homepage directs readers to price their selected parts; a current supplier-priced bill of materials still needs confirmation.
5. **Field performance:** Review Search Console Core Web Vitals or PageSpeed Insights field data for mobile visitors. Conditional loading reduces unused assets, but no field-performance improvement or ranking effect has been measured.
6. **After deployment:** Inspect representative historical redirects, root/latest canonicals, robots, and sitemap on the live host. Submit the root sitemap and use URL Inspection to check Google's selected canonical. Monitor indexing and non-branded traffic over subsequent weeks.
7. **Previously published archives:** Template fixes apply to future builds. Existing archive HTML was not republished; older deployments may still contain the duplicate robots directives observed in the audit. Rebuilding old tags requires a deliberate backport/deployment plan because their source predates these changes.
