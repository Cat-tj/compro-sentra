# Sentra Technology company profile (sentratechnology.com)

Static site, no build step. Everything served lives in `site/`. Vercel project `sentratech/compro-sentra`
(`vercel.json`: framework null, `outputDirectory: site`, clean URLs, `/assets/*` cached 1 year immutable).

> Melanjutkan pekerjaan sebagai agent lain? Baca `HANDOFF.md` dan `docs/seo/` dulu.

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
- Brand queries: the bare word "sentra" is generic (Google shows Sentra Computer, Nissan Sentra, etc.) and is not winnable. Target "sentra technology", "sentra technology samarinda", "PT Sentra Visi Teknologi". Done on 2026-10-31: homepage FAQ "Apa itu Sentra Technology?" (visible + FAQPage JSON-LD, 5 languages), WebSite `alternateName`, ID homepage title "Sentra Technology Samarinda | ...", disambiguation line in `llms.txt`. Still needs the owner: Google Search Console verification (add the `google-site-verification` meta to the 5 homepages) + sitemap submit, Google Business Profile, social profiles for Organization `sameAs`, backlinks.
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

## Copy style (anti AI-slop, decided 2026-11-02)
The owner dislikes generic AI-sounding copy. Rules: plain descriptive headings ("Sembilan layanan, satu tim", "Cara kerja kami") instead of
abstract ones ("Kapabilitas terpadu", "Pusat teknologi"); concrete nouns and numbers (50+ proyek, 13 ahli, 2-4 minggu pilot) instead of
superlatives (terbaik, terdepan, inovatif); no floating claim chips; avoid repeated "dari X sampai Y" and triads of vague benefits; every
claim must exist on the site or in docs/. Reference research (Gamatechno, Mitrais, SoftwareSeni, Nodeflux): borrow their *structure* (stat
grid, case-study cards with type/duration/tech, plain service names, logo wall, short numbered use cases), not their language, which is
full of superlatives and repeated blurbs. Rewrite all 5 languages together.

## Design decisions so far
- Light theme everywhere; only the footer is dark navy.
- About page team section: three groups (Leadership, Infra, Software; "Hardware" was renamed "Infra"),
  big equal photo cards centered per group, hover/tap eats the photo into ASCII then shows the bio (`js/team-hang.js`),
  white background with static ripple-circle line art (`img/art/team-lines-v2.svg`). No fish in that section.
- Team photos live in `img/team/` as 400x400 webp. Only Ilham still uses an initial avatar (no photo yet). Richard Chandra's ("icat") photo is the original lamp-lit studio shot cropped inside the yellow light (cutout/mask attempts left glitches, so no background editing).
- Team bios are drafts written from job titles; replace when real bios arrive.

## Open items
- Owner is looking for a new reference for the About hero ASCII; hero and footer animations may become static.
- Real photo for Ilham; real bios; whether Adam's title becomes "Infra Lead".
- PR https://github.com/Sentra-Technology/compro-sentra/pull/2 needs a repo writer to merge.

## Partners and price rules
- GIDA (PT GIDA International Trading Indonesia) became a Sentra partner on 2026-11-02 (mobile light towers, energy storage containers, solar 4G cameras). Page: `/services/menara-lampu-surya` (source `tools/pages/menara-lampu-surya.build.py`, specs from their brochure), article `/blog/light-tower-surya-vs-diesel`.
- Never publish distributor or partner price lists (GIDA's says distributor price is for partners only and market price is only a recommendation). Pages say "price follows the manufacturer's official quotation; request via WhatsApp". Brochure and price list model names differ (GD7-H vs 7H) and some specs disagree (PV 595 W vs 610 W per panel); the page uses the brochure.
- Not yet on the site: GD-MES energy storage containers and the GDKJ-D440 solar 4G camera (could become pages after the owner confirms Sentra sells them).
