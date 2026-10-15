"""Build portable GitHub Pages redirects to the migrated X-Cache article.

Only Python's standard library is needed. The output works at a github.io
root or under /x-cache-1.github.io/, including locale paths and old anchors.
"""
from argparse import ArgumentParser
from pathlib import Path


def render(locale: str, detect_locale: bool = False) -> str:
    target = f"https://www.rabin.ai/{locale}/blog/x-cache/"
    label = "前往 X-Cache 新文章" if locale == "zh" else "Read X-Cache at its new home"
    script = (
        'const locale = /(?:^|\\/)zh(?:\\/|$)/.test(location.pathname) ? "zh" : "en";\n'
        'const target = "https://www.rabin.ai/" + locale + "/blog/x-cache/";'
        if detect_locale else f'const target = "{target}";'
    )
    return f'''<!doctype html>
<html lang="{locale}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="refresh" content="0;url={target}">
  <link rel="canonical" href="{target}">
  <meta name="robots" content="noindex">
  <title>X-Cache — Rabinovich's Codex</title>
  <script>
    {script}
    location.replace(target + location.search + location.hash);
  </script>
</head>
<body><p><a href="{target}">{label}</a></p></body>
</html>
'''


def main() -> None:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=Path('dist'))
    args = parser.parse_args()
    for path, locale, detect in [
        ('index.html', 'en', False),
        ('en/index.html', 'en', False),
        ('zh/index.html', 'zh', False),
        ('404.html', 'en', True),
    ]:
        dest = args.out / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render(locale, detect), encoding='utf-8')
    (args.out / '.nojekyll').touch()
    print(f'Wrote English, Chinese, root and fallback redirects to {args.out}')


if __name__ == '__main__':
    main()
