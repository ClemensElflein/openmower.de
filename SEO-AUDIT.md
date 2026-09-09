# OpenMower SEO audit — 9 September 2026

The strongest technical finding is that historical documentation URLs were moved without working redirects. The strongest content finding is that the homepage does not adequately answer the questions of someone discovering DIY robotic mowing. Existing project publicity also does not necessarily translate into direct backlinks to this domain.

These are credible explanations for underperformance, not a measured attribution of lost rankings. Search Console query, country, indexing, and backlink data were not available. The target market was not specified; the content assessment considers prospective DIY builders, with German-language opportunities treated as conditional.

## Scope and confirmed healthy behavior

Inspected Hugo configuration, templates, content, deployment workflow, and Git history. Fetched all 102 URLs in the live root sitemap, 19 historical knowledge-base URLs derived from Git renames, representative older root documentation URLs, four archive entry pages, and the homepage variants. Checked internal HTML page destinations linked from sitemap pages, excluding archive subtrees; this was not an exhaustive asset, fragment, or external-link audit.

- All 102 sitemap URLs returned HTTP 200, had canonical tags and nonempty meta descriptions, and had no `noindex` directive.
- Current pages deliver their content in HTML; indexing does not depend on executing a client-side application.
- No broken current internal HTML page destinations were found within the checked scope.
- HTTP and www homepage requests resolved to HTTPS on the bare domain.
- All four sampled archive entry pages were marked `noindex`.

Public search surfaced the homepage and current documentation. Search results from this tool are not a location-controlled Google rank tracker, and `site:` results do not establish Google's selected canonical or indexed-page count.

## 1. High priority: restore historical URLs

On 25 June 2026, commit `36d13274` reorganized 19 knowledge-base articles. Internal references were updated, but all 19 previous URLs now return HTTP 404. Their replacement URLs return 200.

Examples:

| Old URL path — returns 404 | Current replacement path |
| --- | --- |
| `/latest/docs/knowledge-base/compatible-mowers/` | `/latest/docs/knowledge-base/getting-started/compatible-mowers/` |
| `/latest/docs/knowledge-base/shopping-list/` | `/latest/docs/knowledge-base/getting-started/shopping-list/` |
| `/latest/docs/knowledge-base/rtk-gps/` | `/latest/docs/knowledge-base/gps/rtk-gps/` |
| `/latest/docs/knowledge-base/rtk-base-setup/` | `/latest/docs/knowledge-base/gps/rtk-base-setup/` |

The site also moved to the `/latest/` deployment structure in November 2025 (`009633c5`, `345ef2bc`). Sampled older URLs `/docs/`, `/docs/getting-started/`, and `/docs/knowledge-base/compatible-mowers/` return 404 rather than taking visitors to the current documentation.

Consequently, any external links and bookmarks to these addresses lead to dead pages. The replacement pages lack a redirect signal connecting them to their previous addresses. The number and value of backlinks affected remain unknown.

**Action:** inventory earlier URLs from Git history and Search Console, and map each to its closest current equivalent. Prefer permanent server/edge redirects. GitHub Pages hosting constrains server redirects; Hugo aliases with immediate refresh and canonical markup are a fallback, but they are not HTTP 301 responses. Do not redirect every missing page to the homepage. Preserve existing working `/latest/docs/` URLs to avoid another migration.

The companion `seo-audit-redirects.csv` contains the 19 verified mappings. This is a starting inventory, not the complete historical redirect set. Google's [redirect documentation](https://developers.google.com/search/docs/crawling-indexing/301-redirects) explains permanent relocation signals.

## 2. High priority: make the homepage useful for discovery

The title already contains useful terms: “OpenMower — Open Source RTK GPS Robotic Mower.” However, the visible H1 is “Smart. Open. Autonomous.” The introductory copy concentrates on GPL, ROS, RTOS, and manufacturer lock-in. The following prominent sections ask visitors to support, contribute, or join Discord.

The homepage does not explain enough about compatibility, build cost, skills, installation steps, perimeter-wire replacement, or real mowing results. Useful answers exist deeper in the documentation, but the homepage offers little context or direct navigation to them. Its “Get Started” button links to the documentation index rather than the actual getting-started guide.

Source: `content/en/_index.html:17` and `:20`.

**Action:** use a descriptive main heading such as “Build an open-source robot lawn mower with RTK GPS.” Explain what the conversion does, who it suits, supported mower families, realistic costs and exclusions, setup effort, and limitations. Link directly to compatibility, shopping list, build guide, and RTK explanation. Show original build photos and mowing demonstrations. Keep the open-source benefits, supported by practical information.

The existing getting-started guide estimates about €700 excluding the mower and RTK base station; validate that estimate before featuring it prominently. Improve existing resources into clear entry pages rather than creating overlapping articles for every keyword variation. Google's [content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) emphasizes descriptive headings, completeness, and first-hand expertise.

## 3. Medium priority: align homepage canonical signals

Both `https://openmower.de/` and `https://openmower.de/latest/` return the same homepage. Both declare `https://openmower.de/latest/` as canonical. The sitemap includes `/latest/`, while the structured-data application URL uses the root domain.

The cause is explicit in `.github/workflows/gh-pages.yaml:55`: Hugo builds against `/latest/`. At line 98 the generated homepage is copied unchanged to the root. `layouts/partials/hooks/head-end.html:2` uses `.Permalink` for every canonical tag.

This is not proof of a duplicate-content penalty or lost link equity: the two pages already nominate one canonical, and Google can consolidate duplicates. It is nevertheless a confusing choice if `/` is intended to be the public project homepage.

**Action:** make `/` the preferred homepage, align canonical, sitemap, social metadata, and internal home links, and redirect only the duplicate `/latest/` homepage where possible. Leave current documentation paths intact. Google recommends [consistent canonical signals](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls).

## 4. Project publicity and domain backlinks need separate accounting

The [Raspberry Pi feature from May 2022](https://www.raspberrypi.com/news/build-your-own-smart-lawn-mower-with-raspberry-pi/) directs prospective builders to GitHub and Discord. Its build-resource link does not point directly to openmower.de. This is one verified example, not a complete backlink assessment.

The project therefore has established recognition, but some of that recognition is attached to other URLs and platforms. Age and a few backlinks do not establish relevance for every mower-related query. Ranking also depends on the particular page answering the searcher's needs; the site has its clearest fit with DIY and open-source searches.

**Action:** inspect Search Console's linked pages and referring sites. Check whether important references point to the homepage, live documentation, broken historical URLs, GitHub, or older project sites. Recover broken destinations first. Maintain clear website links from project profiles you control; consider requesting updated editorial links after the destination pages are improved. No outreach was performed.

## 5. Conditional priority: language and geography

The site is English-only (`config.toml:6`, `:69`), on a German country-code domain. Google treats `.de` as a strong Germany signal and tries to match pages to the searcher's language. This makes German discovery queries an opportunity the current content does not directly serve; it does not make international ranking impossible. See Google's [international-site guidance](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites).

**Action:** if Germany matters, add substantial German homepage and beginner content, with separate URLs, reciprocal `hreflang`, and language navigation. If the priority is international English traffic, inspect country performance before considering any domain change. A domain migration is not justified by this audit alone.

## 6. Smaller technical and content improvements

| Finding | Recommendation and significance |
| --- | --- |
| Live `/robots.txt` contains only `User-agent: *`; the static source contains a sitemap declaration. | Check generated output and put the sitemap declaration in the effective robots template. Crawling is currently allowed; this is a discovery improvement, not an indexing blocker. |
| 20 of 102 sitemap URLs are tag/category pages, including near-synonymous tags such as `map`, `maps`, and `mapping`; `/latest/search/` is also indexable. | Inspect utility and overlap, consolidate tags, and exclude internal search and unhelpful listings from indexing and the sitemap. At this scale, there is no evidence of a crawl-budget crisis. |
| Two pairs of duplicate titles: “Getting Started” and “Classic 500(B).” Every non-home title repeats the long site title suffix. | Distinguish the beginner guide from the knowledge-base index and label version-specific guides. Use a short brand suffix while retaining useful page-specific terms. |
| Generic descriptions such as “A shopping list for your Open Mower build.” | Describe the page's actual information and audience. Better snippets may help clicks; meta descriptions are not a direct ranking boost. |
| Some document pages contain multiple H1s; search and updates listings have none. | Improve heading hierarchy for clarity and accessibility. This is not evidence of a ranking penalty. |
| Asciinema, carousel, and image zoom assets load globally, including the homepage. | Load features where needed, and measure mobile performance before assigning priority. The hero already has responsive image preloads. |
| Sampled newer archive pages output both `noindex, nofollow` and `noindex, follow`. | Emit one deliberate robots directive. The archives are already excluded from indexing in these samples. |

No field Core Web Vitals or valid browser performance trace was obtained: the browser tool could not start because its profile was already in use. Performance is unmeasured, not a confirmed explanation for poor rankings. A local Lighthouse score alone would not establish real-user performance either.

## Validation and implementation order

1. Export Search Console performance by query, page, country, and device; separate branded and non-branded traffic. Compare periods around November 2025 and June 2026, accounting for mowing season and year-over-year differences.
2. Restore historical URL mappings. Verify old URLs reach the exact replacement, replacements return 200, and internal links use final destinations.
3. Align homepage canonical signals and verify Google's selected canonical in URL Inspection for `/` and `/latest/`.
4. Improve the homepage and existing beginner, compatibility, and cost resources. Publish German entry pages if the target audience warrants them.
5. Clean up sitemap/robots output, repetitive titles, and low-value listings. Measure mobile Core Web Vitals using Search Console or PageSpeed Insights field data where available.
6. Submit the final sitemap, inspect representative repaired URLs, and monitor indexing, non-branded impressions, clicks, and relevant query positions over subsequent weeks. No ranking position or recovery timeline can be promised from these checks.

Only audit documentation was added to the repository. Website code, content, and deployment were not changed.
