"""Blog SEO upkeep. Run after adding or editing an article: python3 tools/blog-seo.py

For every article in site/{,en/,zh/,ko/,ms/}blog/*.html it reads the JSON-LD (headline, dates, image) and:
- sets the author (JSON-LD Person, visible byline, article:author) to AUTHOR_NAME
- sets og:type to article and adds article:published_time / article:modified_time
- adds the RSS <link rel="alternate"> to the article and to that language's blog.html
- writes the RSS feed site/<lang>/blog/feed.xml
- sets the article's <lastmod> in sitemap.xml to its dateModified
Safe to run repeatedly."""
import glob, html, json, os, re
from datetime import datetime, timezone
from email.utils import format_datetime

SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
BASE = "https://www.sentratechnology.com"
# Every article is written by Raphael Wicaksono (owner's decision, 2026-10-30).
AUTHOR_NAME = "Raphael Wicaksono"
ORG_AUTHOR = '"author": {"@type": "Organization", "name": "Sentra Technology"}'
PERSON_AUTHOR = ('"author": {"@type": "Person", "name": "%s", '
                 '"worksFor": {"@id": "%s/#organization"}}' % (AUTHOR_NAME, BASE))
LANGS = {  # prefix: (rss language, feed title)
    "": ("id", "Artikel Sentra Technology"),
    "en": ("en", "Sentra Technology Articles"),
    "zh": ("zh-CN", "Sentra Technology 文章"),
    "ko": ("ko", "Sentra Technology 아티클"),
    "ms": ("ms", "Artikel Sentra Technology"),
}


def ld_post(page):
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', page, re.S):
        for node in json.loads(block).get("@graph", []):
            if node.get("@type") in ("BlogPosting", "NewsArticle", "Article"):
                return node
    raise ValueError("no article JSON-LD")


def meta(page, attr, name):
    m = re.search(r'<meta content="([^"]*)" %s="%s"/>' % (attr, re.escape(name)), page)
    return html.unescape(m.group(1)) if m else ""


def add_rss_link(page, href, title):
    if 'type="application/rss+xml"' in page:
        return page
    tag = '<link href="%s" rel="alternate" title="%s" type="application/rss+xml"/>' % (href, html.escape(title))
    return page.replace('<meta content="index,follow', tag + '<meta content="index,follow', 1)


def iso(d):
    return d + "T08:00:00+07:00" if len(d) == 10 else d


def rfc822(d):
    return format_datetime(datetime.fromisoformat(iso(d)))


def main():
    sitemap_path = os.path.join(SITE, "sitemap.xml")
    sitemap = open(sitemap_path, encoding="utf-8").read()
    for prefix, (rss_lang, feed_title) in LANGS.items():
        root = os.path.join(SITE, prefix)
        path_prefix = "/" + prefix if prefix else ""
        feed_url = f"{BASE}{path_prefix}/blog/feed.xml"
        items = []
        for f in sorted(glob.glob(os.path.join(root, "blog", "*.html"))):
            page = open(f, encoding="utf-8").read()
            post = ld_post(page)
            url = post["mainEntityOfPage"]
            published, modified = post["datePublished"], post.get("dateModified", post["datePublished"])

            page = page.replace(ORG_AUTHOR, PERSON_AUTHOR)
            page = re.sub(r'(<p class="post-meta">)[^<·]*?( · )', r"\g<1>%s\g<2>" % AUTHOR_NAME, page, count=1)
            if 'property="article:author"' not in page:
                page = page.replace('<meta content="Sentra Technology" property="og:site_name"/>',
                                    '<meta content="Sentra Technology" property="og:site_name"/>'
                                    '<meta content="%s" property="article:author"/>' % AUTHOR_NAME, 1)
            page = page.replace('<meta content="website" property="og:type"/>', '<meta content="article" property="og:type"/>')
            if "article:published_time" not in page:
                times = ('<meta content="%s" property="article:published_time"/>'
                         '<meta content="%s" property="article:modified_time"/>') % (iso(published), iso(modified))
                page = page.replace('<meta content="article" property="og:type"/>',
                                    '<meta content="article" property="og:type"/>' + times, 1)
            page = add_rss_link(page, feed_url, feed_title)
            open(f, "w", encoding="utf-8").write(page)

            sitemap = re.sub(r"(<loc>%s</loc><lastmod>)[^<]*" % re.escape(url), r"\g<1>" + modified[:10], sitemap)
            items.append((published, post["headline"], url, meta(page, "name", "description"), post.get("image", "")))

        listing = os.path.join(root, "blog.html")
        page = open(listing, encoding="utf-8").read()
        open(listing, "w", encoding="utf-8").write(add_rss_link(page, feed_url, feed_title))
        blog_url = f"{BASE}{path_prefix}/blog"
        listing_desc = meta(page, "name", "description")

        items.sort(reverse=True)
        out = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:media="http://search.yahoo.com/mrss/">',
               "<channel>",
               f"<title>{html.escape(feed_title)}</title>",
               f"<link>{blog_url}</link>",
               f"<description>{html.escape(listing_desc)}</description>",
               f"<language>{rss_lang}</language>",
               f"<lastBuildDate>{rfc822(items[0][0]) if items else format_datetime(datetime.now(timezone.utc))}</lastBuildDate>",
               f'<atom:link href="{feed_url}" rel="self" type="application/rss+xml"/>']
        for published, title, url, desc, image in items:
            out += ["<item>",
                    f"<title>{html.escape(title)}</title>",
                    f"<link>{url}</link>",
                    f'<guid isPermaLink="true">{url}</guid>',
                    f"<pubDate>{rfc822(published)}</pubDate>",
                    f"<description>{html.escape(desc)}</description>"]
            if image:
                out.append(f'<media:content url="{image}" medium="image"/>')
            out.append("</item>")
        out += ["</channel>", "</rss>", ""]
        open(os.path.join(root, "blog", "feed.xml"), "w", encoding="utf-8").write("\n".join(out))
        print(f"{prefix or 'id'}: {len(items)} articles -> {feed_url}")

    open(sitemap_path, "w", encoding="utf-8").write(sitemap)


if __name__ == "__main__":
    main()
