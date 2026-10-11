# Responsive preview update — 11 October 2026

Preview only; production not deployed. responsive.css is included after the approved visual CSS and copied into the guarded release candidate.

- India metric layout: pipeline on first row, ad spend and60%+ together underneath with26px desktop gap. Dubai hero arrangement and imagery remain as before, per latest direction. General navigation adjustments apply to both markets.
- Navigation wraps at1100px instead of clipping, with Resources available on phones, regional controls visible and44px phone navigation targets. Hero and contact CTAs remain available; small-screen header omits duplicate CTA to preserve space.
- India phone/tablet hero reflows naturally, avoids portrait-tablet empty height, retains brand strip; ultrawide hero is bounded at1920px and1000px high.
- Forms use16px fields, stacked tablet calculator/lead sections. Mobile single-column project cards and constrained metric labels; team portraits retain matched heights.
- Map, service flow, footer, case studies and video label adapt to screen width. Laptop video label no longer escapes the right edge. Reduced-motion preference respected.
- Preserved guides receive responsive navigation and readable content sizing; tables scroll locally. Resources preview alias now uses the branded resource page.

## Verification
40 page/viewport combinations: Home/About/Work/Contact, Dubai About/Work/Contact, Resources at320x740,820x1180,844x390,1366x768,2560x1440. No heading/form/navigation/card overflow in final checks. Additional390x844 checks for service disclosure, resource menu, case study and calculator;3 campaigns gives INR45,600, Landing Pages shows custom quote. Earlier768x1024 and1024x768 checks also performed. Light and dark screenshots inspected. Chrome viewport emulation only, not a claim of physical iOS/Android/Safari testing.

Full release audit passed and production source baseline unchanged. Shared responsive.css hash matches local build. See release-prep/responsive-audit.json and responsive-mobile-preview.png.
