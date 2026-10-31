"""Generate a service page in all 5 languages from a content file: python3 tools/new-service-page.py tools/pages/starlink.json

Each language's site/<lang>/services/<template>.html is the shell (head, header, footer, scripts); this replaces the
page's meta, JSON-LD, language-menu links and <main>. Catalog cards listed in "catalog_ids" are copied verbatim from
that language's produk.html, so they keep their translations and "add to list" buttons; a service without hardware
gives "project_slugs" instead and shows those portfolio cards from portfolio.html.
When the content file has "list_after" (a service slug) and each language a "card" block, the page is also added to
that language's services.html (card, renumbering, service count, meta), plus sitemap.xml and llms.txt ("llms")."""
import html, json, os, re, sys
from urllib.parse import quote

SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
BASE = "https://www.sentratechnology.com"
WA = "https://wa.me/628170822552?text="
ARROW = '<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ICONS = {
    "dish": '<path d="M4 10a8 8 0 0 0 10 10L4 10z"/><path d="M9 15l3-3M13 4a7 7 0 0 1 7 7M13 8a3 3 0 0 1 3 3"/>',
    "box": '<path d="M3 7l9-4 9 4-9 4-9-4z"/><path d="M3 7v10l9 4 9-4V7M12 11v10"/>',
    "pin": '<path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
    "wifi": '<path d="M2 9a15 15 0 0 1 20 0M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0"/><path d="M12 19.5h.01"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    "shuffle": '<path d="M16 3h5v5M4 20 21 3M21 16v5h-5M15 15l6 6M4 4l5 5"/>',
    "wrench": '<path d="M14.7 6.3a4 4 0 0 0 5 5L22 14l-8 8-2.3-2.3a4 4 0 0 0-5-5L4 12l8-8z"/>',
    "pick": '<path d="M14 4c3 0 6 2 7 5-3-1-6-1-9 1L4 18l-2-2 8-8c2-3 2-6 1-9z"/>',
    "leaf": '<path d="M5 21c0-9 6-15 16-16-1 10-7 16-16 16z"/><path d="M5 21 14 12"/>',
    "crane": '<path d="M4 21V5l8-2v18M12 5h9l-3 4M12 9h6v4"/><path d="M2 21h12"/>',
    "ship": '<path d="M3 17l2 4h14l2-4H3zM6 17V9h12v8M12 9V4"/>',
    "gov": '<path d="M3 10h18M5 10v8M9 10v8M15 10v8M19 10v8M3 21h18M12 3l9 5H3z"/>',
    "office": '<rect height="18" rx="1.5" width="14" x="5" y="3"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M10 21v-4h4v4"/>',
    "cam": '<path d="M3 7h12l3 3v4H3z"/><path d="M18 10h3M7 14v6M4 20h6"/>',
    "nvr": '<rect height="8" rx="1.5" width="18" x="3" y="8"/><path d="M7 12h.01M11 12h6"/>',
    "phone": '<rect height="18" rx="2" width="10" x="7" y="3"/><path d="M11 17h2"/>',
    "school": '<path d="M2 9l10-5 10 5-10 5-10-5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/>',
    "shop": '<path d="M4 9h16l-1-5H5zM5 9v11h14V9M9 20v-6h6v6"/>',
    "factory": '<path d="M3 21V10l6 4V10l6 4V6l6 4v11z"/><path d="M7 17h2M13 17h2"/>',
}

NUMBERS = {
    "": "Satu Dua Tiga Empat Lima Enam Tujuh Delapan Sembilan Sepuluh Sebelas Dua_belas Tiga_belas Empat_belas Lima_belas",
    "ms": "Satu Dua Tiga Empat Lima Enam Tujuh Lapan Sembilan Sepuluh Sebelas Dua_belas Tiga_belas Empat_belas Lima_belas",
    "en": "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen",
    "zh": "一 二 三 四 五 六 七 八 九 十 十一 十二 十三 十四 十五",
    "ko": "한 두 세 네 다섯 여섯 일곱 여덟 아홉 열 열한 열두 열세 열네 열다섯",
}
SERVICE_WORD = {"": " layanan,", "ms": " perkhidmatan,", "en": " services,", "zh": "项服务，", "ko": " 가지 서비스,"}


def add_to_listing(c, prefix, t):
    p = "/" + prefix if prefix else ""
    f = os.path.join(SITE, prefix, "services.html")
    s = open(f, encoding="utf-8").read()
    if f'href="{p}/services/{c["slug"]}"' in s:
        return
    i = s.index(f'href="{p}/services/{c["list_after"]}"')
    end = s.index("</a>", i) + 4
    link = re.search(r'<span class="link">([^<]*)</span>', s[i:end]).group(1)
    card = t["card"]
    tags = "".join(f"<span class=tag>{e(x)}</span>" for x in card["tags"])
    s = s[:end] + (f'<a class="card rv" href="{p}/services/{c["slug"]}"><span class="ico-tile">{icon(c["card_icon"])}</span>'
                   f'<span class="num">00 · {e(card["num"])}</span><h3>{e(t["name"])}</h3><p>{e(card["desc"])}</p>'
                   f'<div class="tags">{tags}</div><span class="link">{link}</span></a>') + s[end:]
    n = iter(range(1, 100))
    s = re.sub(r'<span class="num">\d\d ·', lambda m: f'<span class="num">{next(n):02d} ·', s)
    total = len(re.findall(r'<span class="num">\d\d ·', s))
    words = [w.replace("_", " ") for w in NUMBERS[prefix].split()]
    old, new = words[total - 2] + SERVICE_WORD[prefix], words[total - 1] + SERVICE_WORD[prefix]
    assert old in s, (f, old)
    s = s.replace(old, new, 1)
    head, rest = s.split("</head>", 1)
    after, add = card["meta_after"], card["meta_add"]
    if add not in head:
        head = head.replace(after, after + add)
    open(f, "w", encoding="utf-8").write(head + "</head>" + rest)


def add_to_sitemap_and_llms(c):
    slug = c["slug"]
    sm_path = os.path.join(SITE, "sitemap.xml")
    sm = open(sm_path, encoding="utf-8").read()
    if f"/services/{slug}</loc>" not in sm:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{h}" href="{BASE}{q}/services/{slug}"/>'
                       for h, q in (("en", "/en"), ("id", ""), ("ko", "/ko"), ("ms", "/ms"), ("zh-CN", "/zh"), ("x-default", "")))
        entries = "".join(f"<url><loc>{BASE}{q}/services/{slug}</loc><lastmod>{c['date']}</lastmod><priority>0.8</priority>{alts}</url>\n"
                          for q in ("", "/en", "/zh", "/ko", "/ms"))
        anchor = f"<url><loc>{BASE}/services/{c['list_after']}</loc>"
        sm = sm.replace(anchor, entries + anchor, 1)
        open(sm_path, "w", encoding="utf-8").write(sm)
    llms_path = os.path.join(SITE, "llms.txt")
    llms = open(llms_path, encoding="utf-8").read()
    if f"/services/{slug})" not in llms:
        i = llms.index(f"/en/services/{c['list_after']})")
        j = llms.index("\n", i) + 1
        llms = llms[:j] + c["llms"] + "\n" + llms[j:]
        open(llms_path, "w", encoding="utf-8").write(llms)


def icon(key):
    return '<svg aria-hidden="true" viewBox="0 0 24 24">%s</svg>' % ICONS[key]


def e(s):
    return html.escape(s, quote=False)


def catalog_cards(prefix, ids):
    page = open(os.path.join(SITE, prefix, "produk.html"), encoding="utf-8").read()
    cards = []
    for cid in ids:
        m = re.search(r'<article class="hwi"[^>]*id="%s">.*?</article>' % re.escape(cid), page, re.S)
        if not m:
            sys.exit(f"{prefix or 'id'}: catalog card {cid} not found in produk.html")
        cards.append(m.group(0))
    return "".join(cards)


def project_cards(prefix, slugs):
    p = "/" + prefix if prefix else ""
    page = open(os.path.join(SITE, prefix, "portfolio.html"), encoding="utf-8").read()
    cards = []
    for s in slugs:
        m = re.search(r'<a class="projects-card[^"]*"[^>]*href="%s/portfolio/%s">.*?</a>' % (re.escape(p), re.escape(s)), page, re.S)
        if not m:
            sys.exit(f"{prefix or 'id'}: portfolio card {s} not found in portfolio.html")
        cards.append(m.group(0))
    return "".join(cards)


def build_main(c, t, prefix, slug):
    p = "/" + prefix if prefix else ""
    wa = WA + quote(t["wa_text"])
    pains = "".join(f"<li><span><b>{e(b)}</b><span>{e(d)}</span></span></li>" for b, d in t["pains"])
    cards = "".join(f'<article class="card rv"><span class="ico-tile">{icon(k)}</span><h3>{e(h)}</h3><p>{e(d)}</p></article>'
                    for k, (h, d) in zip(c["do_icons"], t["do"]))
    sectors = "".join(f'<a class="card rv" href="{p}{href}"><span class="ico-tile">{icon(k)}</span><h3>{e(h)}</h3><p>{e(d)}</p>'
                      f'<span class="link">{e(t["sector_link"])}</span></a>'
                      for k, href, (h, d) in zip(c["sector_icons"], c["sector_links"], t["sectors"]))
    steps = "".join(f"<li><b>{e(s)}</b></li>" for s in t["steps"])
    related = "".join(f'<a class="mini-card" href="{p}{href}"><span class="mc-ico">{ARROW}</span><span><b>{e(label)}</b></span></a>'
                      for href, label in zip(c["related_links"], t["related"]))
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in t["faq"])
    chips = "".join(f'<span class="float-chip c{i + 1}">{e(x)}</span>' for i, x in enumerate(t["chips"]))
    trust = "".join(f"<li>{e(x)}</li>" for x in t["cta_trust"])
    if c.get("catalog_ids"):
        kits = f'<div class="hwi-grid">{catalog_cards(prefix, c["catalog_ids"])}</div>'
    else:
        kits = f'<div class="grid g3">{project_cards(prefix, c["project_slugs"])}</div>'
    return (
        f'<main id="main"><section class="page-hero"><div class="wrap split"><div class="ph-in">'
        f'<nav aria-label="Breadcrumb" class="crumb"><a href="{p}/">{e(t["crumb_home"])}</a><a href="{p}/services">{e(t["crumb_services"])}</a><span>{e(t["name"])}</span></nav>'
        f'<h1>{e(t["h1"])}</h1><p class="lead">{e(t["lead"])}</p>'
        f'<div class="hero-actions"><a class="btn btn-primary" href="{wa}" rel="noopener" target="_blank">{e(t["btn_consult"])}</a>'
        f'<a class="btn btn-ghost" href="#kit">{e(t["btn_kits"])}</a></div></div>'
        f'<div class="rv"><div class="media wide"><img alt="{e(t["name"])}" src="{c["hero_img"]}"/>{chips}</div></div></div></section>'
        f'<section class="sec sec-alt"><div class="wrap split"><div class="split-copy rv"><h2>{e(t["pains_h2"])}</h2></div><ul class="pains rv">{pains}</ul></div></section>'
        f'<section class="sec"><div class="wrap"><div class="sec-head center rv"><h2>{e(t["do_h2"])}</h2></div><div class="grid g3">{cards}</div></div></section>'
        f'<section class="sec sec-alt" id="kit"><div class="wrap"><div class="sec-head center rv"><h2>{e(t["kits_h2"])}</h2><p class="lead">{e(t["kits_lead"])}</p></div>'
        f'{kits}</div></section>'
        f'<section class="sec"><div class="wrap"><div class="sec-head center rv"><h2>{e(t["sectors_h2"])}</h2></div><div class="grid g3">{sectors}</div></div></section>'
        f'<section class="sec sec-alt"><div class="wrap"><div class="sec-head center rv"><h2>{e(t["steps_h2"])}</h2></div><div class="rv"><ol class="steps">{steps}</ol></div></div></section>'
        f'<section class="sec" id="terkait"><div class="wrap"><div class="sec-head center rv"><h2>{e(t["related_h2"])}</h2></div><div class="grid g3">{related}</div></div></section>'
        f'<section class="sec sec-alt"><div class="narrow"><div class="sec-head center rv"><h2>{e(t["faq_h2"])}</h2></div><div class="faq">{faq}</div></div></section>'
        f'<section class="cta-sec"><div aria-hidden="true" class="net-bg dark"></div><div class="wrap"><div class="cta-band rv"><h2>{e(t["cta_h2"])}</h2><p>{e(t["cta_p"])}</p>'
        f'<div class="hero-actions"><a class="btn btn-white" href="{wa}" rel="noopener" target="_blank">{e(t["cta_wa"])}</a><a class="btn btn-outline-light" href="{p}/contact">{e(t["cta_msg"])}</a></div>'
        f'<ul class="cta-trust">{trust}</ul></div></div></section></main>'
    )


def build_ld(c, t, prefix, slug):
    p = "/" + prefix if prefix else ""
    url = f"{BASE}{p}/services/{slug}"
    return json.dumps({"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "name": t["name"], "description": t["description"], "url": url,
         "provider": {"@id": f"{BASE}/#organization"}, "areaServed": {"@type": "Country", "name": "Indonesia"},
         "serviceType": t["name"]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": t["crumb_home"], "item": f"{BASE}{p}/"},
            {"@type": "ListItem", "position": 2, "name": t["crumb_services"], "item": f"{BASE}{p}/services"},
            {"@type": "ListItem", "position": 3, "name": t["name"], "item": url}]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]},
    ]}, ensure_ascii=False)


def main(path):
    c = json.load(open(path, encoding="utf-8"))
    slug, tpl = c["slug"], c["template"]
    for prefix, t in c["langs"].items():
        page = open(os.path.join(SITE, prefix, "services", tpl + ".html"), encoding="utf-8").read()
        head, rest = page.split("</head>", 1)
        head = head.replace(f"/services/{tpl}", f"/services/{slug}")
        head = re.sub(r"<title>.*?</title>", f"<title>{e(t['title'])}</title>", head, count=1)
        attr = html.escape(t["description"])
        head = re.sub(r'<meta content="[^"]*" name="description"/>', f'<meta content="{attr}" name="description"/>', head, count=1)
        head = re.sub(r'<meta content="[^"]*" property="og:description"/>', f'<meta content="{attr}" property="og:description"/>', head, count=1)
        for prop in ("og:title", "og:image:alt"):
            head = re.sub(r'<meta content="[^"]*" property="%s"/>' % prop, f'<meta content="{html.escape(t["title"])}" property="{prop}"/>', head, count=1)
        head = re.sub(r'<meta content="[^"]*" property="og:image"/>', f'<meta content="{BASE}{c["og_img"]}" property="og:image"/>', head, count=1)
        head = re.sub(r'<script type="application/ld\+json">.*?</script>',
                      lambda _: f'<script type="application/ld+json">{build_ld(c, t, prefix, slug)}</script>', head, count=1, flags=re.S)
        rest = re.sub(r'(<div class="lang-menu">.*?</div>)', lambda m: m.group(1).replace(f"/services/{tpl}", f"/services/{slug}"), rest, count=1, flags=re.S)
        rest = re.sub(r'<main id="main">.*?</main>', lambda _: build_main(c, t, prefix, slug), rest, count=1, flags=re.S)
        out = os.path.join(SITE, prefix, "services", slug + ".html")
        open(out, "w", encoding="utf-8").write(head + "</head>" + rest)
        print("wrote", os.path.relpath(out, SITE))
        if "list_after" in c:
            add_to_listing(c, prefix, t)
    if "list_after" in c:
        add_to_sitemap_and_llms(c)


if __name__ == "__main__":
    main(sys.argv[1])
