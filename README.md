# DrakeLabs

Zachary Drake’s portfolio: infrastructure, projects, practical lessons, and professional experience in unified communications and contact centers.

- Website: https://drakelabs.org/
- Service status: https://status.drakelabs.org/
- Organization: https://github.com/DrakeLabs

## Develop locally

Use Node.js 24 and pnpm:

```sh
pnpm install --frozen-lockfile
pnpm dev
```

Open the printed localhost address. Stop the development server with Ctrl+C.

```sh
pnpm build
python3 scripts/check-site.py
pnpm preview
```

Build output is in `dist/`; it is not committed. Only this website directory belongs in this repository.

## Structure

- `src/pages/`: Home, Infrastructure, Projects, family media case study, Journal, Professional, About, Support, Status, and the 404 page.
- `src/layouts/Layout.astro`: shared navigation, metadata, and footer.
- `src/styles/global.css`: responsive navy/teal styling and seasonal accents.
- `public/images/`: owner-supplied screenshots.
- `public/brand/`: transparent SVG and PNG logos for light and dark backgrounds.
- `.github/workflows/pages.yml`: GitHub Pages deployment on pushes to `main` or manual dispatch.

## Hosting

The static Astro website runs independently of the home lab. It contains no server credentials, monitoring tokens, or live-service controls. Its status links go to the independently hosted Better Stack page; availability results are not duplicated in the static build.

The organization-site repository uses `SITE_URL=https://drakelabs.org` and `BASE_PATH=/`. The custom domain is drakelabs.org; its DNS records are managed separately in Cloudflare.

See [deployment instructions](docs/DEPLOYMENT.md) and [status setup](docs/STATUS.md).

## Seasonal accents

Themes follow the visitor’s local date each year:

- Halloween: October 24–31.
- Christmas: December 18–26.
- New Year’s: December 27–January 8, inclusive.

Other dates use the service-manual palette: off-white, charcoal, forest green, and rust orange. The footer’s Seasonal accents checkbox remembers the visitor’s choice. The status route keeps its standard colors. No scheduler or annual deployment is required.

Local preview overrides: `/?season=halloween`, `/?season=christmas`, `/?season=new-year`, and `/?season=default`. Overrides are disabled in production. Without JavaScript, the standard theme remains usable.

## Content

The owner supplies the personal history, project direction, and career details. ChatGPT and Codex implement the website. Approximate timeline dates remain explicitly identified. The build-your-own section is a roadmap for future tested guides. No blanket license is granted for third-party artwork visible in screenshots.
