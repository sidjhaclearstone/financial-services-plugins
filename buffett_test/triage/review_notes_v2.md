# Triage calibration review v2 (Test 1 widened: NTM P/E <18x OR FCF yield >=6%)

**Scope:** 348 new names in batches 41–58. I compared every KEEP (22) and TOO HARD (88) within its RBICS industry using `scripts/summarize.py`, and checked each against the v1 final KEEPs and the v1 overrides in the same industries. NO rows were not re-reviewed.
**Result:** KEEP goes from 22 to **18** (5.2% of 348, within the ~5–10% guide; v1 ended at 4.7%). There are 6 overrides: 5 demotions and 1 promotion (`review_overrides_v2.csv`).

## v1 principles applied
| Rule (v1 precedent) | v2 outcome |
|---|---|
| Homebuilders are housing-cycle earners (DHI TOO HARD, PHM/LEN/TOL NO) | **NVR** demoted. EPS is 0.86x its peak, consensus FY1 is −17.8%. |
| Capital-markets earners (RJF, AMP, BNY, HLNE; TRU kept with worst year −6.9%) | **MORN** demoted. Ratings and asset-based fees drove EPS −39% in 2022; EPS is now 1.0x its peak. SEIC, BLK, BX, ARES and HLI stay TOO HARD. |
| P&C at a hard-market peak (PLMR, SKWD, TRV, HIG TOO HARD; only long-record PGR and ORI kept) | **KNSL** demoted. EPS is 1.0x peak after a 6x rise, consensus FY2 is +1.6%. WRB stays TOO HARD (FY2 −1.2%), matching TRV. |
| Recent levered deal or transformation (BRO, UMBF, DKS) | **LOW** demoted. The $10.1bn FBM/ADG deal is 2.0x FY FCF, and net debt/EBITDA is 3.51x in a housing-cyclical. AJG, CARR, FTV, J, KNF and VVV stay TOO HARD. |
| ≥7% route plus named threats (GLP-1; MKC/GIS NO) | **HSY** demoted. Cocoa set 2025 EPS (−33%), and consensus implies only ~1.7%/yr from the 2023 level. |
| Near-cyclical-peak rule applied with judgement (CSL kept at 82nd pctile; LII/CRH out at 100th pctile after sharp run-ups) | **AWI** promoted. Margin is 19.8% vs a 17.0% average (modest drift), ROIC 15%, net debt 0.9x, 8/10 years ≥7%. RPM, VMI, MOD, AGX and CRAI stay TOO HARD: peak margins after a sharper run-up, or ordinary ROIC. |

## Judgement calls kept as KEEP
- **AXP: judged against the v1 bank standard, and it passes.** EPS grew through the zero-rate years (5.65 to 10.02 over 2016–21) and ROE averaged 28%. The growth route is spend and fees rather than NIM, and the margin is at the 45th pctile, not a peak.
  - Two points separate it from COF (TOO HARD: Discover transformation) and SYF/BFH (NO): a prime closed-loop book and minimal M&A.
  - Deep-dive item: the 2020 EPS fall of −53%, which reflected credit plus a T&E shock.
- **MRSH.** The McGriff deal ($8.5bn in 2024) is about 5% of revenue, net debt is 2.4x, and EPS rose ≥7% in 9 of 10 years. That is unlike BRO's transformational Accession deal. Watch: margin at its 10y high as P&C pricing softens.
- **OTIS, PAYX, MCD, DPZ, SNA, BR, ADSK:** margins are at the 91st–100th pctile, but these are non-cyclical or recurring streams with only small drift above average, so the peak rule does not apply. ADSK is kept for consistency with INTU/ADBE (25% GAAP EBIT, unlike VERX).
- **COR, ABT.** Deals (RCA, and the pending Exact Sciences) are under 10% of the base and leverage is ≤1.1x. Walgreens concentration (COR) and the NEC litigation (ABT) are deep-dive tests.
- **TSCO.** Kept for consistency with POOL (v1 KEEP): margin is at the 27th pctile, not a peak, and consensus FY3 is +10%. The stalled 2022–25 EPS (~2%/yr) is the deep-dive test.
- **WMS and PAYX (FCF route).** FCF is recurring: 10y FCF conversion is 1.32x and 1.08x.

## No-change TOO HARD worth noting
- **FICO** has 10/10 years of growth, but FHFA's VantageScore decision and bureau direct licensing are a credible regulatory threat within 5 years.
- **EXLS** faces the same AI threat to labour-based billing as G, DOX and EPAM in v1.
- **PAYC and WDAY** face a growth slowdown and the AI/seat threat.
- FCF-route names with non-recurring FCF stay TOO HARD: AGX (advance billings), CHWY (working capital and SBC), GLIBK (FCF conversion 0.14).

**Next candidates if more names are needed:** WRB, then FICO, then KNSL.
