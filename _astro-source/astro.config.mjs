import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://bionicbanker.tech',
  integrations: [sitemap()],
  output: 'static',
});
