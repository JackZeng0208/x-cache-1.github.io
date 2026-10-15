# X-Cache · Project Page

The project page has moved into **Rabinovich's Codex**:

https://www.rabin.ai/en/blog/x-cache/

The original Astro source and media remain here as an archive. GitHub Actions
now publishes only small redirect pages, preserving query strings
and section anchors. All old language paths now lead to the English project
page; the Chinese version has been removed. The interactive figures live in
`JackZeng0208/jackzeng0208.github.io`.

## Restoring the original domain

`x-cache-1.github.io` belongs to the GitHub account or organization named
`x-cache-1`. Transferring this repository does not transfer that domain. If the
old account was deleted, the redirect cannot be served there until that account
or organization name can be restored or registered again. GitHub documents a
90-day username reuse delay after account deletion.

Once you control that namespace, create `x-cache-1/x-cache-1.github.io`, run
`python3 scripts/build_redirects.py --out /tmp/x-cache-redirect-site`, and copy
the generated files (including `.nojekyll`) to the new repository's root.
Enable **Settings → Pages → Deploy from a branch → main → / (root)**.
No project source, videos, or custom-domain setting is needed in that repository.

The personal blog also handles `/x-cache-1.github.io/`, `/x-cache-1.github.io/en/`,
and `/x-cache-1.github.io/zh/`, which covers the transferred repository's current
Pages address and its inherited `rabin.ai` address.

## Archived project

Astro-built project page for the X-Cache technical report (XPeng AI Infra).
Editorial-tech aesthetic, fully localised in English and Chinese, with a custom
wipe / diff / shadow video comparator that lets the reader inspect the
baseline and cached outputs pixel by pixel.

## Development

```sh
npm ci
npm run dev
```

The default local path is `/x-cache-1.github.io/`. Run `npm run build` to
generate the static site and `npm run preview` to check it locally.

## Archived Astro build

The archived Astro configuration accepts `PAGES_URL` to set the hostname and
project subpath. This build is no longer used by the deployment workflow.
Local builds default to
`https://jackzeng0208.github.io/x-cache-1.github.io/`.

After a repository transfer, the previous owner's `github.io` address does
not transfer with it. A project site also inherits any custom domain configured
on the owner's `<owner>.github.io` repository. That domain must serve the
project through GitHub Pages, or its hosting provider must route the project
path explicitly; otherwise the inherited URL can return a 404 even after a
successful deployment.
