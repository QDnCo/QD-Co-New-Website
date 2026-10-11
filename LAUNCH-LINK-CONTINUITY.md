# Launch gate — not deployed

The redesign remains noindex/nofollow and private. The new footer and resource hub link to current production content so existing guides, citations and published case-study URLs stay connected.

Before approved launch:
1. Preserve every URL in live-url-preservation.json. Deploy the new homepage/navigation additively; do not replace or delete existing guides, answers, data, legal, work, tools, Dubai or other content directories.
2. Keep existing canonical paths (/dubai/, /about/, /work/) and adapt preview .html navigation. If any path must change, create a one-to-one permanent redirect and verify each old URL resolves to its matching content.
3. Render launch content and links as crawlable HTML, retain appropriate organization/service schema, canonical tags and the production sitemap. Preview intentionally remains noindex; remove preview directives only from approved production outputs.
4. Verify conversion tracking and contact backend end-to-end. Current contact preview does not submit leads.
5. Repeat live HTTP, canonical and internal-link checks after deployment. Compare original sitemap inventory against the final release. Profile links with automated 403s require a public browser check, not a claim that the profile is broken.
6. Incoming third-party links remain outside our control; unchanged destination URLs protect them. No ranking improvement can be guaranteed by this UI change.
