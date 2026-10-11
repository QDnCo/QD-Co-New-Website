# QDnCo search favicon — prepared, not deployed

The supplied Google screenshot shows the purple lightning icon. Direct checks of the current production homepage and favicon.svg/favicon.ico on 11 October show the older QD monogram instead. This supports a stale Google icon cache; it does not establish when Google last fetched it. The redesign inherited the old favicon.

Reused approved QDnCo square artwork without changing the logo. Packaged SVG, multi-size ICO, 48/96/192/512 PNG, Apple 180 PNG and webmanifest. All142 candidate HTML pages now reference stable root icon URLs. The redesigned Organization logo references /icon-512.png. Preview uses the same assets and remains noindex; production source unchanged.

Durable hooks: brand-icons.py; build-v3.py; release-prep/prepare.sh; sync-share-preview.py; preview-branded-pages.py. Full release audit passed; favicon-audit.json has zero missing-page errors. Temporary public preview icon hash verified.

## At approved launch
1. Deploy icons with HTML, including root favicon.ico, not only the visible navbar logo.
2. Verify HTTPS icon responses, correct image MIME types and that Googlebot can fetch homepage and Googlebot-Image can fetch icons. Production robots must permit them; preview remains blocked.
3. Purge hosting/CDN caches if present, then request homepage indexing in Google Search Console.
4. Keep favicon URL stable. Allow days to weeks for recrawl; Google does not guarantee favicon display. India and Dubai on the same hostname share one favicon.

Official guidance: https://developers.google.com/search/docs/appearance/favicon-in-search
