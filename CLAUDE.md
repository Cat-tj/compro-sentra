# Sentra Technology company profile (sentratechnology.com)

Static site, no build step. Everything served lives in `site/`. Vercel project `sentratech/compro-sentra`
(`vercel.json`: framework null, `outputDirectory: site`, clean URLs, `/assets/*` cached 1 year immutable).

## Structure
- 5 languages: Indonesian at the root, plus `en/`, `zh/`, `ko/`, `ms/`. Every page change must be made in all 5.
- Shared assets in `site/assets/` (`css/site.css`, `css/ocean.css`, `js/*.js`, `img/`).
- `sitemap.xml` and `llms.txt` list every page; update them when adding pages.
- `tools/ascii-art.py` (Lucide icon to ASCII illustration) and `tools/ascii-panel.py` (glyph field panels).

## SEO upkeep
- Every article is by **Raphael Wicaksono** (JSON-LD `Person`, visible byline, `article:author`).
- After adding or editing an article, run `python3 tools/blog-seo.py`: sets author, `og:type` article and
  `article:*_time`, the RSS `<link>`, rewrites `site/<lang>/blog/feed.xml`, and syncs the article's sitemap `<lastmod>`
  to its JSON-LD `dateModified`. Keep `datePublished`/`dateModified` in the JSON-LD accurate; everything derives from them.
- News/press items (awards, launches, partnerships) use `"@type": "NewsArticle"` instead of `BlogPosting`.
- New service page in 5 languages: write `tools/pages/<slug>.json` (see `starlink.json`), run
  `python3 tools/new-service-page.py tools/pages/<slug>.json`, then add its card to every `services.html`, plus
  `sitemap.xml` and `llms.txt`.
- New article in 5 languages: write `tools/articles/<slug>.py` (see `starlink-untuk-tambang.py`), run
  `python3 tools/new-article.py tools/articles/<slug>.py` (page, blog.html card + category filter, sitemap), then
  `python3 tools/blog-seo.py`. Dates are always the real publish date.
- The keyword map and article backlog live in the "Peta Pasar & Keyword SEO Sentra" doc on claude.ai.
- IndexNow: key file `site/d01773ca34bcf938cfbdbeff95ad2284.txt` must stay deployed. Never rename or delete it.

## Rules that bite
- **Cache busting**: assets are immutable for a year. After editing a CSS/JS file, bump its `?v=` in every HTML file
  that references it (e.g. `site.css?v=20261031a`). For a changed image, give it a new file name (`-v2`, `-v3`),
  never overwrite in place. A 404 can get cached too: if a new image shows broken in production, rename it.
- Keep it light: the owner tests on weak laptops and phones. Prefer static images/SVG over animation.
  WebGL is still used in the homepage hero and footer (`field.js`) and the About hero koi pond (`koi.js`).
- Contact: WhatsApp `628170822552` (shown as +62 817-0822-552), emails admin@ and richard@ (product contact).

## Deploy flow (always in this order)
1. Commit, push to the fork remote `fork` (Cat-tj/compro-sentra), branch `static-site-remodel`.
2. Deploy a **preview** from a clean export (`git archive HEAD`) with `vercel deploy --yes --scope sentratech`,
   then share it with a Vercel share link.
3. **Promote right after the preview passes verification** (owner's standing instruction since 2026-10-30, "langsung
   promote, gausah tanya"; before that, promote waited for an explicit "Promote"):
   `vercel promote <preview-url> --yes --timeout 3m --scope sentratech`, then verify with curl on www.sentratechnology.com.
4. Ping Bing and the other IndexNow engines for the changed pages (production only):
   `python3 tools/indexnow.py <url> ...` or `python3 tools/indexnow.py --since <YYYY-MM-DD>`.

## Design decisions so far
- Light theme everywhere; only the footer is dark navy.
- About page team section: three groups (Leadership, Infra, Software; "Hardware" was renamed "Infra"),
  big equal photo cards centered per group, hover/tap eats the photo into ASCII then shows the bio (`js/team-hang.js`),
  white background with static ripple-circle line art (`img/art/team-lines-v2.svg`). No fish in that section.
- Team photos live in `img/team/` as 400x400 webp. Only Ilham still uses an initial avatar. Richard Chandra's photo had its background replaced with plain white (Apple Vision subject mask).
- Team bios are drafts written from job titles; replace when real bios arrive.

## Open items
- Owner is looking for a new reference for the About hero ASCII; hero and footer animations may become static.
- Real photo for Ilham; real bios; whether Adam's title becomes "Infra Lead".
- PR https://github.com/Sentra-Technology/compro-sentra/pull/2 needs a repo writer to merge.
