"""Build portable GitHub Pages redirects to the English X-Cache project page.

Only Python's standard library is needed. The output works at a github.io
root or under /x-cache-1.github.io/, including locale paths and old anchors.
"""
from argparse import ArgumentParser
from pathlib import Path


def render() -> str:
    target = "https://www.rabin.ai/en/blog/x-cache/"
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="refresh" content="0;url={target}">
  <link rel="canonical" href="{target}">
  <meta name="robots" content="noindex">
  <title>X-Cache — Rabinovich's Codex</title>
  <script>
    const target = "{target}";
    location.replace(target + location.search + location.hash);
  </script>
</head>
<body><p><a href="{target}">View the X-Cache project page</a></p></body>
</html>
'''


def main() -> None:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=Path('dist'))
    args = parser.parse_args()
    for path in ['index.html', 'en/index.html', 'zh/index.html', '404.html']:
        dest = args.out / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render(), encoding='utf-8')
    (args.out / '.nojekyll').touch()
    print(f'Wrote legacy locale, root and fallback redirects to {args.out}')


if __name__ == '__main__':
    main()
