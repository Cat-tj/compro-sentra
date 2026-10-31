"""Tell Bing (and every other IndexNow engine: Yandex, Seznam, Naver, Yep) about new or changed pages.
Run it AFTER the change is live in production, never for a preview.

  python3 tools/indexnow.py https://www.sentratechnology.com/blog/new-article ...   specific URLs
  python3 tools/indexnow.py --since 2026-10-30                                       sitemap URLs with lastmod >= date
  python3 tools/indexnow.py --all                                                    every URL in sitemap.xml
Add --dry-run to print the URLs without sending.

The key file site/<KEY>.txt must stay deployed at the site root, or the engines reject the submission."""
import json, os, re, sys, urllib.error, urllib.request

KEY = "d01773ca34bcf938cfbdbeff95ad2284"
HOST = "www.sentratechnology.com"
SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")


def sitemap_urls(since=None):
    xml = open(os.path.join(SITE, "sitemap.xml"), encoding="utf-8").read()
    pairs = re.findall(r"<loc>([^<]+)</loc>(?:<lastmod>([^<]+)</lastmod>)?", xml)
    return [loc for loc, mod in pairs if since is None or (mod and mod[:10] >= since)]


def main(args):
    dry = "--dry-run" in args
    args = [a for a in args if a != "--dry-run"]
    if args[:1] == ["--all"]:
        urls = sitemap_urls()
    elif args[:1] == ["--since"] and len(args) == 2:
        urls = sitemap_urls(args[1])
    elif args and all(a.startswith(f"https://{HOST}/") for a in args):
        urls = args
    else:
        sys.exit(__doc__)
    if not urls:
        sys.exit("No URLs to submit.")
    print("\n".join(urls), f"\n{len(urls)} URL(s)")
    if dry:
        return
    body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt",
                       "urlList": urls[:10000]}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print("IndexNow:", r.status, "(200/202 = accepted)")
    except urllib.error.HTTPError as e:
        sys.exit(f"IndexNow rejected: {e.code} {e.read().decode(errors='replace')[:300]}")


if __name__ == "__main__":
    main(sys.argv[1:])
