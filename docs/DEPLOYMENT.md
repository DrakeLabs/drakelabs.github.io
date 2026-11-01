# GitHub Pages deployment

Repository: https://github.com/DrakeLabs/drakelabs.github.io

Initial website: https://drakelabs.github.io/

## Deploy

1. In repository Settings → Pages, select GitHub Actions as the build source.
2. Push the website source to `main`. The Pages workflow builds Astro and deploys the static output. It can also be run manually from the Actions tab.
3. Verify the completed deployment URL, navigation, images, logo downloads, and service-status link.

Build settings are `SITE_URL=https://drakelabs.github.io` and `BASE_PATH=/`. Dependencies are locked in pnpm-lock.yaml. The workflow uses Node.js 24 and the official Astro build/upload action.

Public publication was authorized by Zach on November 1, 2026, including the career wording and screenshots as supplied. Private editorial provenance and review files are excluded from Git. No parent server files belong in this repository.

## Custom domain

Moving the portfolio to drakelabs.org is a separate DNS phase. Verify domain ownership and existing records before configuring GitHub Pages, DNS, HTTPS, and SITE_URL together. Do not change Jellyfin or other service records as part of portfolio deployment.

The independent status page already uses https://status.drakelabs.org/.

Reference: https://docs.astro.build/en/guides/deploy/github/
