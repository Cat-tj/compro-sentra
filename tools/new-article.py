"""Publish a new article in all 5 languages from a content file: python3 tools/new-article.py tools/articles/<slug>.py
then run python3 tools/blog-seo.py (author, feed, lastmod).

The content file is plain Python defining SLUG, DATE (YYYY-MM-DD), COVER, OG_IMAGE and LANGS = {prefix: {...}}; each
language gives title, description, category, lead, wa_text, body (HTML with <h2 id=...>) and aside [(href, label)].
Each language's blog/<TEMPLATE>.html is the shell; this replaces its meta, JSON-LD, language links and article,
adds a card to the top of that language's blog.html (and the category filter if it is new) and the sitemap entries."""
import html, json, os, re, runpy, sys
from urllib.parse import quote

SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
BASE = "https://www.sentratechnology.com"
TEMPLATE = "private-llm-on-premise"
MONTHS = {
    "": "Januari Februari Maret April Mei Juni Juli Agustus September Oktober November Desember".split(),
    "ms": "Januari Februari Mac April Mei Jun Julai Ogos September Oktober November Disember".split(),
    "en": "January February March April May June July August September October November December".split(),
}
READ = {"": "{} menit baca", "ms": "{} minit bacaan", "en": "{} min read", "zh": "{} 分钟阅读", "ko": "{} 분 소요"}


def fmt_date(prefix, d):
    y, m, day = d.split("-")
    m, day = int(m), int(day)
    if prefix == "en":
        return f"{MONTHS['en'][m - 1]} {day}, {y}"
    if prefix == "zh":
        return f"{y}年{m}月{day}日"
    if prefix == "ko":
        return f"{y}년 {m}월 {day}일"
    return f"{day} {MONTHS[prefix][m - 1]} {y}"


def read_minutes(prefix, body):
    text = re.sub(r"<[^>]+>", " ", body)
    if prefix in ("zh", "ko"):
        units, per_min = len(re.sub(r"\s", "", text)), 500
    else:
        units, per_min = len(text.split()), 200
    return max(1, round(units / per_min))


def e(s):
    return html.escape(s, quote=False)


def main(path):
    c = runpy.run_path(path)
    slug, date = c["SLUG"], c["DATE"]
    sitemap_path = os.path.join(SITE, "sitemap.xml")
    sitemap = open(sitemap_path, encoding="utf-8").read()
    for prefix, t in c["LANGS"].items():
        p = "/" + prefix if prefix else ""
        url = f"{BASE}{p}/blog/{slug}"
        root = os.path.join(SITE, prefix)
        page = open(os.path.join(root, "blog", TEMPLATE + ".html"), encoding="utf-8").read()
        head, rest = page.split("</head>", 1)

        head = head.replace(f"/blog/{TEMPLATE}", f"/blog/{slug}")
        head = re.sub(r"<title>.*?</title>", f"<title>{e(t['title'])} | Sentra</title>", head, count=1)
        desc = html.escape(t["description"])
        for attr, name in (("name", "description"), ("property", "og:description")):
            head = re.sub(r'<meta content="[^"]*" %s="%s"/>' % (attr, name), f'<meta content="{desc}" {attr}="{name}"/>', head, count=1)
        for name in ("og:title", "og:image:alt"):
            head = re.sub(r'<meta content="[^"]*" property="%s"/>' % name, f'<meta content="{html.escape(t["title"])} | Sentra" property="{name}"/>', head, count=1)
        head = re.sub(r'<meta content="[^"]*" property="og:image"/>', f'<meta content="{BASE}{c["OG_IMAGE"]}" property="og:image"/>', head, count=1)
        for name in ("article:published_time", "article:modified_time"):
            head = re.sub(r'<meta content="[^"]*" property="%s"/>' % name, f'<meta content="{date}T08:00:00+07:00" property="{name}"/>', head, count=1)

        def ld(m):
            data = json.loads(m.group(1))
            for node in data["@graph"]:
                if node.get("@type") in ("BlogPosting", "NewsArticle"):
                    node.update(headline=t["title"], description=t["description"], datePublished=date, dateModified=date,
                                image=BASE + c["COVER"], mainEntityOfPage=url)
                if node.get("@type") == "BreadcrumbList":
                    node["itemListElement"][-1].update(name=t["title"], item=url)
            return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"
        head = re.sub(r'<script type="application/ld\+json">(.*?)</script>', ld, head, count=1, flags=re.S)

        rest = re.sub(r'(<div class="lang-menu">.*?</div>)', lambda m: m.group(1).replace(f"/blog/{TEMPLATE}", f"/blog/{slug}"), rest, count=1, flags=re.S)
        h2s = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', t["body"])
        toc_label = re.search(r'<nav aria-label="([^"]*)" class="toc">', rest).group(1)
        toc = f'<nav aria-label="{toc_label}" class="toc"><b>{toc_label}</b><ol>' + "".join(f'<li><a href="#{i}">{h}</a></li>' for i, h in h2s) + "</ol></nav>"
        aside_label = re.search(r'<div class="aside-links"><b>([^<]*)</b>', rest).group(1)
        aside = f'<div class="aside-links"><b>{aside_label}</b>' + "".join(f'<a href="{p}{href}">{e(label)} →</a>' for href, label in t["aside"]) + "</div>"
        wa = "https://wa.me/628170822552?text=" + quote(t["wa_text"])
        rest = re.sub(r"<h1>.*?</h1>", f"<h1>{e(t['title'])}</h1>", rest, count=1)
        rest = re.sub(r'(<section class="page-hero center">.*?<p class="lead">).*?(</p>)', lambda m: m.group(1) + e(t["lead"]) + m.group(2), rest, count=1, flags=re.S)
        meta = f'<time datetime="{date}">{fmt_date(prefix, date)}</time> · {READ[prefix].format(read_minutes(prefix, t["body"]))}'
        rest = re.sub(r'(<p class="post-meta">[^<]*· )<time.*?</p>', lambda m: m.group(1) + meta + "</p>", rest, count=1, flags=re.S)
        rest = re.sub(r'(<div class="post-cover"><img alt=")[^"]*(" src=")[^"]*', lambda m: m.group(1) + html.escape(t["title"]) + m.group(2) + c["COVER"], rest, count=1)
        rest = re.sub(r'<nav aria-label="[^"]*" class="toc">.*?(<div class="post-cta">)', lambda m: toc + t["body"] + aside + m.group(1), rest, count=1, flags=re.S)
        rest = re.sub(r'(<div class="post-cta">.*?<a class="btn btn-primary" href=")[^"]*', lambda m: m.group(1) + wa, rest, count=1, flags=re.S)
        open(os.path.join(root, "blog", slug + ".html"), "w", encoding="utf-8").write(head + "</head>" + rest)

        listing_path = os.path.join(root, "blog.html")
        listing = open(listing_path, encoding="utf-8").read()
        if f'href="{p}/blog/{slug}"' not in listing:
            cat = e(t["category"])
            read_more = re.search(r'<a class="post-card bl-card[^>]*>.*?<span class="link">([^<]*)</span>', listing, re.S).group(1)
            card = (f'<a class="post-card bl-card rv" data-cat="{cat}" href="{p}/blog/{slug}"><img alt="" loading="lazy" src="{c["COVER"]}"/>'
                    f'<span class="body"><small>{cat} · {fmt_date(prefix, date)}</small><h3>{e(t["title"])}</h3><p>{e(t["description"])}</p>'
                    f'<span class="link">{read_more}</span></span></a>')
            listing = listing.replace('<div class="grid g2">', '<div class="grid g2">' + card, 1)
            if f'data-cat="{cat}" type="button"' not in listing:
                last = list(re.finditer(r'<button aria-pressed="false" data-cat="[^"]*" type="button">[^<]*</button>', listing))[-1]
                listing = listing[:last.end()] + f'<button aria-pressed="false" data-cat="{cat}" type="button">{cat}</button>' + listing[last.end():]
            open(listing_path, "w", encoding="utf-8").write(listing)

        if f"<loc>{url}</loc>" not in sitemap:
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{h}" href="{BASE}{q}/blog/{slug}"/>'
                           for h, q in (("en", "/en"), ("id", ""), ("ko", "/ko"), ("ms", "/ms"), ("zh-CN", "/zh"), ("x-default", "")))
            entry = f"<url><loc>{url}</loc><lastmod>{date}</lastmod><priority>0.6</priority>{alts}</url>\n"
            anchor = f"<url><loc>{BASE}{p}/blog/{TEMPLATE}</loc>"
            sitemap = sitemap.replace(anchor, entry + anchor, 1)
        print(f"{prefix or 'id'}: {url}")
    open(sitemap_path, "w", encoding="utf-8").write(sitemap)


if __name__ == "__main__":
    main(sys.argv[1])
