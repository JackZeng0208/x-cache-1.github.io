import { defineConfig } from 'astro/config';

// CI reads the actual URL from GitHub Pages, including any custom domain.
const pagesUrl = new URL(
  process.env.PAGES_URL || 'https://jackzeng0208.github.io/x-cache-1.github.io/',
);

export default defineConfig({
  site: pagesUrl.origin,
  base: pagesUrl.pathname,
  trailingSlash: 'always',
  i18n: {
    locales: ['en', 'zh'],
    defaultLocale: 'en',
    routing: {
      prefixDefaultLocale: true,
      redirectToDefaultLocale: false,
    },
  },
  build: {
    assets: '_assets',
  },
  vite: {
    server: {
      fs: {
        allow: ['..'],
      },
    },
  },
});
