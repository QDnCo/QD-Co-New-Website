# GitHub delivery

Repository: https://github.com/QDnCo/QD-Co-New-Website (private). Display title: QD&Co New Website; website branding remains QDnCo.

## Source and build
- React/JSX, styles, images, videos, logos and preserved public guide/citation routes are versioned.
- `release-source/` is the public-site continuity baseline; update deliberately when the live site changes.
- Backend Apps Script source and frontend adapter are included; secrets and account access are not. Third-party platform dashboards are not hosted by this repository.
- Fresh setup: `npm ci`, `python3 -m pip install -r requirements.txt`, `npm run build`.
- `release-prep/candidate/` is the future production-shaped build, never auto-deployed.

## CI/CD
Push to main triggers Ubuntu build, six lead tests, URL/metadata/reference audits, baseline guard, preview noindex checks and private seven-day artifact. A repository-scoped ARM64 macOS runner downloads the passing artifact and updates only `/tmp/qdnco-share-preview-20261011/`. It checks localhost served content against the artifact. No production credentials or deployment step. Runner is installed as a user login service on this Mac. Mac, local port 8770 server and Cloudflare tunnel must remain available; tunnel URL is temporary and can change.

## Working on changes
Commit and push to `new-website/main`; watch Actions before saying preview updated. Existing `origin` remote points to older redesign repo and is preserved. Current branch pushRemote is new-website. Failed CI leaves last successful preview.

## Production remains blocked
No Hostinger upload, DNS change or public GitHub Pages enablement. User launch approval, backend health/receipt validation and analytics verification remain prerequisites. Production CI/CD requires a separate reviewed workflow after those gates; this workflow only deploys the current private preview.
