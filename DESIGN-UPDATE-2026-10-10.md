# Private design update — 10 October 2026

Coverage: retained actual market pins; added three equal regional cards for India, United Arab Emirates and United States, with selectable cities and subtle connecting-line animation. No new market locations invented. Exact QDnCo spelling retained.

Themes: India iteration and shared v3 pages now have theme-aware gradient panels, visible borders, edge highlights, shadows and hover transitions. Light hero uses pale architectural imagery, dark navy text/navigation and light metric cards. Existing dark hero retained with clearer metric boundaries. Reduced-motion preference disables new motion.

Rebuilt with build-v3.py followed by build-dubai-v4.py. Verified rendered light/dark desktop views, map geometry and region selection; browser reported no errors. Attempted viewport override did not change actual viewport from 1728px; mobile visual QA remains unverified. Responsive CSS supplied. Dubai v4 keeps its separate layout/styles. Nothing deployed.


### Pale beige / metro / India atlas iteration
- India shared pages use light limestone #f9f6ef, warm bordered panels and beige wallpaper wash; default preview theme light. Dark mode retained.
- New built-in imagegen edit: assets/architecture-metro-concept.png. Prompt: preserve premium right-side towers, warm daylight, add elevated concrete metro bridge and silver train; clean left negative space, no text/logos. AI architectural concept, not an actual project.
- Replace full-world overview with cropped Chicago–Dubai–India map plus larger India detail; label five existing Indian cities, staggered firefly pins and reduced-motion fallback.
- Build-v3 and build-dubai-v4 succeeded. Desktop beige hero and both map themes inspected; city labels and pulse CSS verified in browser. Separate Dubai-v4 layout unchanged. Nothing deployed.

### Vajram logo contrast
Updated shared Vajram logo to brands/vajram-dark-on-white.png using built-in imagegen: preserve symbol, VAJRAM lettering and CRAFTING LANDMARKS; dark forest green and burgundy on white. Removed dark logo containers in marquee and portfolio, including Dubai build input. Original retained. Preview only.

### Removed process overview
Owner requested removal of the screenshot section: Build the foundation / Then build demand plus Understand, Position, Connect, Improve cards. Removed from shared private source and Dubai base. Retained the separate animated Client Roadmap. Both themes inherit removal. No deployment.

### Afternoon beige refinement
Light theme warmed to #fbf4e6 across shared India pages and wallpaper. Hero begins at 5vw instead of centered max-width container; single-line desktop promise, expanded line spacing, softened building-edge fade and bronze result cards with reduced-motion-safe accent pulse. Dark hero conditional preserves original text line breaks and image. Both builders passed; desktop local preview visually checked. Nothing deployed.

### Viewport-triggered founder video
Shared India/Dubai founder video plays muted at 35% visibility, pauses out of view or when tab hidden, retains native sound/play controls. Catches blocked autoplay and cleans up observer; revisits resume or replay if ended. Dubai shared source also now uses the current owner-supplied video/poster. Preview only.

### Animated services concept map
Replaced India V3Services two cards with Our services root, Marketing/Technology branches and seven connected service nodes. Removed Human oversight, measurable qualification. Viewport observer triggers one-time fade/stagger; Technology enters from right, nodes top-to-bottom, arrows softly pulse. Reduced-motion fallback and stacked mobile layout included. Both builders passed; browser verified seven nodes, viewport entered state and removed phrase. Private only.

### Contact intake fields
Replaced business-email input with phone; conditional WhatsApp input, grouped enquiry types, all-service selector and required Others explanation. Non-client enquiry hides project fields and pricing. Synced shared India/Dubai contact component. Builds pass; browser verified conditional reveal/hide and client-project fields restored. Form remains preview-only with no lead transmission.

### Contact pricing positioning
Removed the optional brief/What needs to improve textarea. New hero: Your next growth plan. Start with the numbers. Added free indicative-estimate explanation, no-commitment copy and 43+ active Bangalore projects proof with service/scope clarity. Rates remain unchanged, indicative and non-submitting. India/Dubai shared component rebuilt.

### Framed compact light hero
Added rounded image frame with 24px white surround and nav aligned to its top edge. Reduced light hero typography, controls, cards and spacing. At desktop viewport 878px high, frame top24/bottom854 and caption bottom730: full frame and content fit without scrolling. Small-screen layout retains natural height for readable content. Dark hero preserved. Builders pass; no deployment.

### Detached navbar and enclosed brand scroll
Light home navbar moved to 8px from top; hero begins at116px with 15px gap after navbar and rounded top corners. Developer scroll now inside hero bottom, removed external duplicate in light mode; dark mode keeps its existing strip placement. Browser verified hero bottom854 and strip bottom853 within878px viewport, leaving24px bottom white margin. Preview only.

## Services refinement — two marketing offers
- Marketing now has Meta & Google Ad Campaigns and Real Estate SEO & AI Search Optimization only. Research/positioning moved into visible campaign inclusions, including user-requested unlimited creatives and Meta asset setup at no extra charge, campaign management, weekly reporting and dedicated relationship manager.
- Technology: CRM Setup & Automation, Landing Pages, AI Lead Follow-Up & WhatsApp Automation. Contact service choices aligned.
- Independent horizontal arrows from one left-hand rail per discipline, higher-contrast bordered cards, per-card viewport reveals and reduced-motion support. India and Dubai previews rebuilt; no deployment.
- Search naming informed by current primary service pages: https://lunasol.ae/geo/real-estate-dubai and https://www.oyemarketor.com/services/search-engine-optimization ; follow-up terminology: https://zakeli.com/features/whatsapp-crm . This is terminology research, not measured keyword volume or a ranking guarantee.
- Browser verified India rendered copy, two marketing cards, visible inclusions, dark/light presentation and all ten scroll reveal targets.

## Expanded developer marquee
Added Emaar, Sobha Realty, DAMAC and Danube Properties to shared India/Dubai brand scroll, now 13 developer marks plus seamless duplicate track. Kept portfolio cards separate, preserving their project data. Download/source details in brands/DEVELOPER-LOGO-SOURCES.md. White tiles preserve logo contrast in both themes; changed Dubai trust copy to reflect India and Dubai project experience. Both builds succeeded and browser confirmed all 13 assets loaded on India and Dubai. Private preview only; not deployed.

## Co-founder video audio
Changed label to “From our co-founder: your next buyer · 25 seconds”; presenter label includes Co-founder. Removed forced muted playback. Video attempts audible playback at 35% visibility and pauses out of view or when tab is hidden. If browser denies autoplay, a Play with sound button provides explicit activation; native mute controls remain respected. Shared India/Dubai component updated. Browser confirmed unmuted playback progressing at 6.93s after entering via homepage watch link and paused outside the section. Autoplay with sound before user interaction remains subject to browser policy. No production deployment.

## Homepage order, global feature and link continuity
- India: Hero/brand scroll → Worldwide → Services → Who We Work With → creative scroll bridge → platform strip → co-founder film bridge → Client Roadmap → resources → FAQ → CTA → footer. Dubai uses the same Services → Work → creative → film → Roadmap order while retaining its earlier performance evidence sections.
- Removed the right-message/right-buyer ribbon from the rendered homepage.
- Worldwide feature moved near the top: emerald surface, warm gold type/pins, clearer map cards and market CTA. Current geographic footprint preserved; no invented offices.
- Emaar Dubai/UAE homepage SVG wordmark is explicitly named brands/emaar-dubai.svg; no India sublabel.
- Live homepage links audited through rendered DOM. Deduplicated 33 content/legal footer destinations, plus 10 public social/directory profiles. Added Resources navigation and resources.html containing the existing sitemap inventory (121 URLs). All existing destinations remain on their public URLs, not redirected into design-preview routes.
- No launch performed. Incoming backlinks cannot be moved by footer edits: preserve all existing public paths at launch, using live-url-preservation.json as an additive-release guard.

## Latest layout and dropdown correction
- Latest explicit order supersedes earlier order: hero/brand strip → co-founder film → Services → creative bridge → Who We Work With → platform bridge → Client Roadmap. Worldwide follows Roadmap, then resources and expanded FAQ. Dubai matches this key sequence and retains its performance sections later.
- Hero logo tiles enlarged from 128×48 to 166×68 in light desktop, with larger dark/Dubai strip tiles.
- Service headers now use accessible button disclosures (aria-expanded/controls), one open at a time, smooth height reveal, rotating circular arrows with soft pulse, keyboard support and reduced-motion rules. The earlier always-visible inclusion preference is overridden by this explicit request. All service inclusions remain.
- Collapsed desktop services section measured 711px tall. Click and Enter activation verified; opening another card closes the previous one.
- Platform strip animation direction reversed to left-to-right.
- FAQ expanded from 4 to 11 relevant questions drawn from existing live-site topics; latest service/commercial directions retained over conflicting older live copy.
- Rebuilt India and Dubai private previews. No publication.

## Team portraits — 10 October
- Built-in image generation used for faithful face restoration of Sai: remove patchy/etched pixelation, preserve identity, expression, skin tone, suit, pose, hands/watch and transparent background. New asset: assets/sai-retouched.png; original preserved.
- Matched visible head height using uniform portrait frames and individual crop/scales. Sai watch hand retained, lower non-watch hand cropped. India and Dubai About components updated.
- Rebuilt both editions; browser checked all three loaded and aligned in beige and dark themes. Local preview only; no deployment.

## Gold contrast and enquiry starter
- Inspected live qdnco.com CTA styles and local region-cta source: #E0A526 gold ring, animated sheen and focus outline; live primary CTA is violet. Adapted hierarchy to a shared gold-ui.css with gold-filled primary actions, outlined secondary buttons, visible card/form/FAQ/navigation borders, dark text on gold and restrained navbar sheen.
- Added side-by-side closing enquiry starter. Name/phone tiles and free-estimate CTA route to the corresponding contact fields; Dubai keeps Dubai routing. These are clearly labelled links; no premature lead submission.
- Shared styles persist through both build scripts. Resources gets outlined navigation, category/link cards and the same enquiry starter; all existing URLs retained.
- Verified Home/About/Work/Contact/Resources and Dubai About load shared CSS and starter. Browser checked 390px mobile layout, no horizontal overflow; contact name tile navigates to contact.html#name. Checked beige/dark and corrected Dubai CTA contrast. Preview-only; no live deployment.

## Contact: calculator before lead capture
Two separate forms, each inside one two-column gold-glowing group. First: role/price left; role and project-count questions right. Second: 43+ Bangalore project context left; client contact, service and project details right. The calculator works without personal details; its CTA scrolls to lead capture. Existing rates preserved, two forms not nested; non-client paths retained. Reduced-motion disables glow animation. Rebuilt India/Dubai. Verified developer/3 projects = ₹66,000 per project, Other hides project count, contact anchor navigation, mobile one-column/no overflow and dark styling. No publication or lead submission.

## Original-face portrait revision
Owner rejected retouched face; supplied original pink-shirt photo as identity source. Built-in image tool produced suit composite from original photo after two-reference attempt still showed artificial texture. Selected assets/sai-original-face-v3.png; clothing and face are AI-assisted, not a pixel-identical paste or identical tailoring. Prompt: preserve original face/expression/hair, change pink shirt to black suit, white shirt/black tie, retain crossed arms and watch, transparent cutout. Prior images retained. Updated India/Dubai About, checked local team framing. No publication.

## Adarsh video framing
Cropped existing 1080×1920 clip to 1080×1200 at y=720, removing upper sky/title region and preserving full horizontal frame and audio via stream copy. 25.1-second duration unchanged. New assets: assets/adarsh-tight-frame-v2.mp4 and matching poster. Shared India/Dubai component updated wherever used; original retained. Frame widened to 350px, no rotation; attribution below bottom-right, zero picture overlap. Browser verified metadata 1080×1200, 25.1s and unmuted active playback. Preview only.

## Video v3: centred framing and rebuilt graphics
Source graphics are baked in; no clean editable-layer master found. Rebuilt timed smaller captions using existing clean transcript, cropped presenter to 900×1000 at (20,700), scaled to 1080×1200. Replaced original graphic-heavy cutaways (8.47–10.6s,16.7–19.23s) and closing (20–25.1s) with navy/gold animated type cards, preserving source audio and duration. Caption phrases condensed from transcript; not a verbatim subtitle file. Retained ₹7cr historical statement from video, not current aggregate claim. New MP4 and matched poster wired into shared India/Dubai film component. Label corner overlaps lower-right by 62×13px desktop, 8px-high overlap mobile. Sound fallback moved outside caption band. Reproducible render: video-edit/rebuild-adarsh.py and .ass. Checked sample frames 1,4,12,18,23 seconds and browser metadata. No deployment.

## Original video restored after owner review
Removed generated captions/motion cards from active site. Restored qd-ad-enhanced-1080x1920.mp4 and matching cover, native 9:16 contain frame with uniform 8px padding; no source graphics cropped. Frame 330px desktop/300px mobile. Source composition retained (headroom reserved for original graphics; not an equidistant presenter crop). Co-founder corner tag widened to270px, slogan nowrap one18px line. India/Dubai rebuilt, verified source dimensions1920×1080 portrait, unmuted playback and single-line slogan. Preview only.


### 2026-10-10 — Worldwide section palette
- Owner prefers warm beige/ivory instead of emerald for the worldwide section enclosure, black heading text, and the exact Let’s talk gold gradient for emphasized words and the glowing border. Preserve the existing map design, pins and animations. Applied in private redesign gold-ui.css; localhost verified; not published.


## Work library redesign
14 new clickable project cards and 14 local case pages; eight sections each. Shared beige/gold and dark themes, persistent India theme preference, mobile stacking. Results scoped to evidence; planning models excluded. Local HTTP and browser checks passed. Not published. Evidence decisions recorded in Rank 1 runs/2026-10-10-work-case-redesign/STATUS.md.

- 2026-10-10 Worldwide palette supersedes beige/black/gold iteration: owner rejected that combination. Headline must read “QDnCo is now present worldwide!” on one line. New preview uses midnight-blue atlas, pearl heading, slate-blue land, restrained champagne pins/borders, integrated map panels. Existing geometry, places and firefly motion retained. Checked desktop/light/dark/mobile and Chennai pin interaction; no deployment.

- 2026-10-10 Contact calculator: service dropdown belongs in the pricing group and stays synchronized with the enquiry service. Fixed rates only for Meta & Google Ad Campaigns and eligible real-estate roles; all other services show “Let’s connect” with a tailored-scope message and no rate/count. Owner explicitly requests campaign-count pricing; labels and hidden field now use campaigns, existing monetary tiers unchanged. Updated India and shared Dubai template; verified all seven service options, reverse dropdown sync and Developer/3 campaigns at ₹66,000 per campaign/month. Preview only.

- 2026-10-10 Theme parity supersedes earlier dark-hero preservation of layout: dark must match light typography, structure, dimensions, spacing and positioning throughout; only colors and the existing dark hero photo differ. Unified hero promise markup and inside-hero brand scroll, shared responsive geometry for light-only rules, preserved architecture-concept.png for dark. Checked About/Work/Contact identical dimensions, mobile/desktop hero geometry (headline entrance animation produces transient offsets). Added CSS content-hash cache versioning to preview builds. No deployment.


## 2026-10-10 — Dubai shared-layout rebuild
Dubai Home/About/Work/Contact now use the same v3 components and gold-ui stylesheet as India; build-dubai-v4.py copies the shared generated layout rather than using the old orange fork. Dubai-specific hero imagery (official Emaar Creek Palace), developer logos, buyer messaging, map focus, enquiry proof and resources. Real estate heading uses CTA gold. Shared compact hero correction prevents brand-strip clipping. Company-wide INR outcomes clearly distinguished from Dubai results. Dubai case-study records remain pending; no results invented. Existing India creative examples labeled as such.
Validation: all four local pages HTTP200/noindex; desktop light/dark hero and mobile 390px checked; no broken images or horizontal overflow; service selection switches non-ad enquiries to tailored scope. Preview only.

- 2026-10-10 dark background preference: animated wallpaper should remain subtle behind content. Reduced saturation to .65, brightness to .72 and strengthened navy wash to .70 in shared SiteWallpaper. Applies to private India/Dubai pages; light theme, foreground imagery and CTA highlights unchanged. Browser verified; not published.

- 2026-10-10 hero refinement: quiet neutral nav/card borders in both themes; remove individual nav-link rings and CTA sheen, retain primary gold actions. Slightly smaller header logo and responsive hero spacing/type keep developer strip within first view. Danube official PNG has white Properties lettering: dark backing fixes all shared logo placements without altering artwork. Verified India/Dubai at desktop 1366x668 and mobile 390x844 plus default desktop; preview only.

- 2026-10-11 service arrow refinement: owner wants stronger gold glow and breathing motion on circular accordion arrows. Shared India/Dubai light/dark controls now use gold fill, three-second scale pulse and expanding halo. Open controls settle; reduced-motion preference disables pulses. Accordion expansion verified locally; not published.

- 2026-10-11 Dubai pricing: use live qdnco.com/dubai published AED models (20,000/month flat retainer or 200/qualified lead, tiers180 above150 and160 above250;100/monthminimum). Media separate;15AIstatics andcopy,studio separate. Other services customquote. Hero retainslatest1400Cr and15Cr totals, displaysrounded535M/5.73M AED at published reference26.17 INR/AED, explicitlyIndiaexperience/notliveFX. Do not regress to old277M pipeline. Every subsequent preview edit must refresh the same temporary share link; regional build now automatically syncs the sanitized snapshot when present. No production launch.

Live source checked: https://qdnco.com/dubai/ on 11 October2026. External preview calculator and service switch verified.
