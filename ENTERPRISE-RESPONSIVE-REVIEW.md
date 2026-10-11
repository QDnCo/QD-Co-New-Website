# UI and responsive review — 11 October 2026

Private preview only. No production deployment.

## Implemented
- Developer, Mandate firm, Channel partner order; Developer initially selected. Dubai labels Realtor / Channel partner.
- Existing React calculator and conditional fields retained; native accessible select menus, custom closed-state chevrons, consistent 54px controls, visible labels, focus rings, dark/light contrast and spacing.
- Shared card radii, CTA minimum heights, FAQ touch affordances, restrained form borders, ultra-wide content limits and narrow-screen adjustments.
- No pricing changes, no new third-party dependencies. Dubai hero layout preserved.

## Screen coverage (CSS viewports, not physical-device certification)
| Category | Sizes checked |
|---|---|
| Compact phones | 320×740, 375×812 |
| Narrow foldable cover / Galaxy Z Fold-class | 344×882 |
| Standard / large iPhone and Android phones | 390×844, 430×932 |
| Small foldable/tablet | 540×720 |
| Foldable inner / tablet portrait | 768×1024, 820×1180 |
| Tablet landscape | 1024×768 |
| Phone landscape | 844×390 |
| Laptop | 1366×768 |
| Full HD monitor / projector | 1920×1080 |
| QHD monitor | 2560×1440 |
| Ultra-wide monitor | 3440×1440 |
| 4K monitor / projector | 3840×2160 |

These are representative browser viewport classes, not asserted device hardware specifications. The phrase “iPhone Dio” does not identify a verified model; fluid phone layouts cover the tested size range without inventing a model specification. Projector legibility additionally depends on viewing distance, browser zoom and room lighting.

## Validation
55 Chrome page/viewport checks: Contact at all 15 sizes; Home/About/Work, Dubai Home/About/Work/Contact and Resources at five representative sizes. No page horizontal overflow or off-screen headings detected. Contact controls remained within viewport. Visually reviewed desktop light and narrow foldable form. Existing dark-theme controls checked through DOM. Dynamic pricing verified: channel partner two campaigns ₹48,600; Landing Pages switches to tailored scope; separate WhatsApp field reveals correctly. Native menu appearance follows browser/OS.

See release-prep/enterprise-responsive-audit.json. Physical iOS Safari, Android devices, hinge-spanning dual-screen modes and actual projectors were not tested. Preview form does not send leads; existing launch integration checks remain required.
