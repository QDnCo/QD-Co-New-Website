# QDnCo release preparation — LOCAL ONLY, NOT DEPLOYED

Prepared 11 October 2026. Website launch remains explicitly unauthorized. This folder is separate from the live `Portfolio Website/dist` and from the noindex temporary design preview.

## Open and rebuild

- Local candidate: http://127.0.0.1:8771/ and http://127.0.0.1:8771/dubai/
- Contact: http://127.0.0.1:8771/contact/ and http://127.0.0.1:8771/dubai/contact/
- Run `./release-prep/prepare.sh` from the redesign repository to build and audit locally. It never uploads files or changes the live repository.
- Start the local candidate with `python3 release-prep/serve.py`. Bound to localhost; noindex response headers; directory listings disabled. Do not point the existing public tunnel at this candidate.
- `candidate/` is the staged webroot. Do not upload it until all launch gates below are closed. `prepare.sh` must be rerun after future design edits.

## Prepared

1. All 121 live sitemap URLs returned HTTP 200 and matched the local production baseline byte-for-byte at this check. `live-url-http-audit.json` contains each URL and hash.
2. Existing resource, research, guide, answer, tool, legal, directory and case-study paths are retained. No production baseline file was deleted. Existing verification files and robots policy retained.
3. New regional main pages and 14 case studies rendered to readable HTML before JavaScript. Existing case-study URLs preserved. New resource library and six guides plus their index have metadata and canonical paths.
4. 32 redesigned/new pages checked for title/description, single H1, canonical, structured JSON and local file references. Zero missing old URLs and zero broken local references in these pages in `audit.json`.
5. Regional homepage alternates, page-specific metadata and social previews, Organization/WebSite/WebPage/Article/Service/FAQ/Breadcrumb structured data where applicable. Service/FAQ schema is based on visible content; no fake ratings or invented review markup. Markup does not guarantee rich results or AI citations.
6. Verified company profiles connected in entity schema and the visible site. Pending profiles are excluded from public publication claims; see `FOOTPRINT-EVIDENCE.md`.
7. Existing sitemap routes preserved, new routes added, `llms.txt` and `llms-full.txt` updated to current services and campaign/project pricing. These are supplemental discovery files, not ranking guarantees.
8. Public `/pricing/index.html` contains the new calculator. Older educational/comparison URLs remain accessible with prominent notices that earlier lead-fee examples are withdrawn, plus links to current fees. Old Offer/FAQ schema removed from affected legacy pages to prevent outdated pricing claims. `legacy-commercial-notices.json` lists 11 affected pages.
9. Production navigation uses stable paths rather than temporary preview filenames. Legacy preview aliases redirect to matching routes in staged `.htaccess`; contact/pricing homepage hashes route to the new contact page. New `/resources/` and `/insights/` are no longer caught by old broad guide redirects.
10. JSX precompiled, runtime Babel/Tailwind compiler removed. Existing compiled utility CSS retained. Four pinned React/Motion/HLS npm distribution assets copied to local vendor paths; asset namespace prevents collisions with existing pages.
11. Lead form adapter preserves phone/WhatsApp, business type, service, project/campaign count, price, project, optional call date, other-service text and UTM context. Extended Apps Script source provided in `lead-backend-candidate.gs`; current seven lead-sheet columns kept in place. No secrets added.
12. GA4 ID G-GZE73M9Q4M retained. `generate_lead` fires only after the receipt helper confirms persistence, never on a submit click. Personal form fields are not sent to GA4. Preview hosts block enquiries and analytics. No test lead or email was sent.
13. Six meaningful local form/backend tests passed (`lead-tests.json`). Browser-tested compiled navigation, 14 portfolio links, detailed case content, custom-service pricing and Dubai three-project AED 51,000 total; no runtime errors observed in these views.

## Launch gates — not yet cleared

- **Lead backend:** the exact Apps Script URL embedded in the live homepage returned HTTP 404 during the read-only GET check. Restore the existing Web App deployment/access (or supply the correct endpoint), apply the prepared optional-field backend update, and confirm its GET version/health. Then send one clearly labelled owner test enquiry and verify the sheet receipt, WhatsApp/service/count fields and notification email. Do not launch with a dead or silently truncated backend.
- **GA4:** confirm `generate_lead` in DebugView/realtime and confirm its key-event designation after the labelled backend test. Presence of the measurement ID is not proof of end-to-end attribution.
- **Release approval:** the owner must approve the final website and proposed Dubai commercial tiers for public launch. Check public-use permission for Dubai hero/developer imagery, which was originally collected for private preview. The company-profile review PDF is intentionally still behind a noindex profile page and needs its own final review.
- **Host rules:** `.htaccess` redirect behavior must be checked on the actual Hostinger/LiteSpeed staging environment. Python localhost verifies files and app behavior, not Apache rewrite execution. No DNS or hosting changes have been made.
- **Pre-launch freshness/backup:** recheck production against `baseline-manifest.json`, rebuild the candidate from the latest sources, and take a recoverable remote webroot backup. Do not overwrite newer live files or the growth-status/creative-review surfaces from an old package.
- **Search monitoring:** save current GSC/Bing landing-page/keyword and GA4 lead baselines before launch. URL continuity reduces migration risk but does not guarantee unchanged traffic or rank one. Do not mass-request indexing or mark new pages indexed without evidence.

## Approved launch sequence (instructions only)

1. Close the gates above; rebuild; run audits. Inspect the staged diff/manifest and approve the exact release. Keep new pages noindex anywhere outside production.
2. Back up the current remote webroot and its server rules. Use a reviewed deployment manifest of changed/new files; do not replace the root by deleting it. Preserve unchanged live resources and all account verification files.
3. Upload namespaced assets first, then approved HTML, then sitemap/discovery files and tested server rules. Do not use the private preview root as the deployment source.
4. Check old 121 URLs and all new routes for status, correct content, canonicals, robots headers, images, theme/mobile behavior, redirects, form receipt and GA4 event.
5. If critical errors appear, restore changed files and server rules from the backup. Keep unrelated live directory/publication changes intact.
6. Submit the sitemap through existing Search Console/Bing accounts only after successful verification; monitor page indexing, errors, organic landing traffic and real enquiries. Update the growth dashboard from verified outcomes.

The code preparation is complete for review. The external backend, analytics and approved-host deployment gates prevent calling this a cleared live release.
