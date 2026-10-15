# X-Cache · Project Page

Astro-built project page for the X-Cache technical report (XPeng AI Infra).
Editorial-tech aesthetic, fully localised in English and Chinese, with a custom
wipe / diff / shadow video comparator that lets the reader inspect the
"lossless" claim pixel by pixel.

## Development

```sh
npm ci
npm run dev
```

The default local path is `/x-cache-1.github.io/`. Run `npm run build` to
generate the static site and `npm run preview` to check it locally.

## GitHub Pages

In **Settings → Pages → Build and deployment**, select **GitHub Actions**.
The deployment workflow reads the site's URL from GitHub Pages and passes it
to Astro as `PAGES_URL`, so the hostname and project subpath match the Pages
settings. Local builds default to
`https://jackzeng0208.github.io/x-cache-1.github.io/`.

After a repository transfer, the previous owner's `github.io` address does
not transfer with it. A project site also inherits any custom domain configured
on the owner's `<owner>.github.io` repository. That domain must serve the
project through GitHub Pages, or its hosting provider must route the project
path explicitly; otherwise the inherited URL can return a 404 even after a
successful deployment.
