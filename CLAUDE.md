# Sentra Technology company profile (sentratechnology.com)

Static site, no build step. Everything served lives in `site/`. Vercel project `sentratech/compro-sentra`
(`vercel.json`: framework null, `outputDirectory: site`, clean URLs, `/assets/*` cached 1 year immutable).

## Structure
- 5 languages: Indonesian at the root, plus `en/`, `zh/`, `ko/`, `ms/`. Every page change must be made in all 5.
- Shared assets in `site/assets/` (`css/site.css`, `css/ocean.css`, `js/*.js`, `img/`).
- `sitemap.xml` and `llms.txt` list every page; update them when adding pages.
- `tools/ascii-art.py` (Lucide icon to ASCII illustration) and `tools/ascii-panel.py` (glyph field panels).

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
3. **Promote to production only after the owner explicitly says "Promote"**:
   `vercel promote <preview-url> --yes --timeout 3m --scope sentratech`, then verify with curl on www.sentratechnology.com.

## Design decisions so far
- Light theme everywhere; only the footer is dark navy.
- About page team section: three groups (Leadership, Infra, Software; "Hardware" was renamed "Infra"),
  big equal photo cards centered per group, hover/tap eats the photo into ASCII then shows the bio (`js/team-hang.js`),
  white background with static ripple-circle line art (`img/art/team-lines-v2.svg`). No fish in that section.
- Team photos live in `img/team/` as 400x400 webp. Richard Chandra, Ridhwan and Ilham still use initial avatars.
- Team bios are drafts written from job titles; replace when real bios arrive.

## Open items
- Owner is looking for a new reference for the About hero ASCII; hero and footer animations may become static.
- Real photos for Richard Chandra (COO), Ridhwan, Ilham; real bios; whether Adam's title becomes "Infra Lead".
- PR https://github.com/Sentra-Technology/compro-sentra/pull/2 needs a repo writer to merge.
