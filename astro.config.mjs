import { defineConfig } from 'astro/config';

// The organization site lives at the root; SITE_URL can change for a custom domain.
export default defineConfig({
  output: 'static',
  site: process.env.SITE_URL || 'https://drakelabs.org',
  base: process.env.BASE_PATH || '/',
  trailingSlash: 'always',
  devToolbar: { enabled: false },
});
