# QDnCo website redesign — private preview

Unpublished India and Dubai website iterations. **Do not deploy, enable GitHub Pages, or connect hosting without the owner’s explicit launch approval.** This repository has no production deployment workflow or hosting credentials. The live website is separately maintained in [QDnCo/qdnco-website](https://github.com/QDnCo/qdnco-website).

## Preview

Requires Python 3. From this folder:

```sh
python3 -m http.server 8767 --bind 127.0.0.1
```

Open http://localhost:8767/ for India and http://localhost:8767/dubai.html for Dubai. Assets are included; some browser libraries/fonts use external CDNs. Preview forms must not be treated as confirmed bookings or a validated production lead flow.

## Edit and rebuild

- India layout and interactions: `v3.jsx` and `v3.css`.
- Dubai layout and interactions: `dubai-v4.jsx` and `dubai-v4.css`.
- Shared visual source snapshots: `build-inputs/`.
- Images, video, fonts and map geometry: `assets/`, `brands/`, `team/`, `shots/`, `adreel/`.
- Original educational resources: `insights/`.

Rebuild in this order:

```sh
python3 build-v3.py
python3 build-dubai-v4.py
```

The India builder also writes temporary Dubai pages, so always run the Dubai builder second. `build.py` and `build-v2.py` retain earlier concepts and will overwrite newer pages if run. Current generated HTML is included for immediate preview.

This repository was copied from `Portfolio Website/redesign-private` on 10 October 2026. The original working directory remains intact. Coordinate future edits against this repository to avoid divergent copies. Review notes and earlier preview screenshots are historical and may not match the latest design.

## Contributors

[Vinayak Tiwari (@akvinayaktiwari)](https://github.com/akvinayaktiwari) contributed to the current QDnCo website and this redesign, as confirmed by the owner. Collaborator access is managed through GitHub invitations. GitHub’s automatic Contributors graph is based on attributed commits; this import does not fabricate commit authorship.

## Before launch

Obtain owner approval; reconcile pricing and performance claims; replace any unverified Dubai placeholders; preserve production URLs, redirects, guides, schema and backlinks; verify lead capture, accessibility and responsive layouts. Assets remain subject to their existing rights; no blanket open-source licence is granted.
