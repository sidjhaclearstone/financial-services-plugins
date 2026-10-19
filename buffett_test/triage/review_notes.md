# Triage calibration review (Stage 3)

**Scope:** all 781 rows in 39 batches (MZTI-US excluded). Every KEEP (59) and TOO HARD (153) was compared within its RBICS industry group using `scripts/summarize.py` stats. NO rows were only spot-checked for homebuilder consistency.
**Result:** KEEP went from 59 to **37**. There are 24 overrides: 23 demotions (KEEP to TOO HARD) and 1 promotion (TOO HARD to KEEP). See `review_overrides.csv`.

## Principles applied
1. **Unforecastable earnings drivers.** I discarded names whose earnings are set mainly by things no one can forecast:
   - capital-markets activity or market levels (wealth managers, alternative managers, custody/sweep NII);
   - rate and credit cycles (banks at peak net interest margin (NIM), homebuilders);
   - commodity prices.
2. **Banks.** I kept a bank only when it is best-in-class through cycles. Every bank is at or near a 10-year EPS high after the 2023–26 rate tailwind, so the test was ROE and growth during the zero-rate years (2016–21), credit record, deposit quality, and a ≥7% growth route that does not depend on NIM.
3. **Near-cyclical-peak rule.** In a cyclical industry, EPS ≥0.95× its 10-year max with EBIT margin at the 10-year high (100th percentile, well above average) means TOO HARD. I applied this to LII and CRH, matching MWA and EXP, which workers had already marked TOO HARD.
4. **Cross-batch consistency.** Names with the same profile get the same verdict:
   - recent transformational deal: BRO and UMBF, matching DKS, FITB and PNFP;
   - short public record untested in a soft market: PLMR and ALH, matching SKWD, ASIC and SARO;
   - near-zero GAAP margins: VERX, matching BL, HUBS, BILL and NCNO;
   - BaaS partner deposits: TBBK, matching CASH;
   - homebuilders: DHI, matching PHM and GRBK, which were NO.
5. **Promotions.** A TOO HARD name moved up only if it is as forecastable as typical KEEPs: durable, non-cyclical, a ≥7% growth route and a sound balance sheet. Most TOO HARD reasons hold up under the rules: government payers, AI disintermediation, single customer, pending mergers, peak margins. Only ADBE moved up, for consistency with INTU (KEEP).

## Banks and insurers kept
| Name | Why kept |
|---|---|
| **JPM** | Fortress balance sheet, Dimon. EPS grew through the zero-rate years (6.19 to 15.36 over 2016–21). 13.5% average ROE, shares −2.9%/yr. |
| **CBSH** | Family-run, conservative underwriter with zero acquisitions. 14.5% 10-year average ROE earned mostly at zero rates. About 9% consensus growth. |
| **SFBS** | Organic, branch-light model. ~18% average ROE. EPS rose every year through 2020–22 (1.37 to 2.31), so growth was not rate-driven. |
| **EWBC** | 15.4% average ROE. EPS grew through the zero-rate years (4.61 to 6.10 to 7.92). 7–8% consensus. US–China and commercial real estate (CRE) exposure must be tested in the deep dive. |
| **AGM** (Farmer Mac) | No down year worse than −0.1% across 2020 and 2022–23. Agency-level funding and minimal credit losses. 30× leverage is structural and needs a capital review. |
| **PGR** | Best-in-class auto underwriter with a long record. The deep dive must normalise its peak margins (consensus FY2 −12%). |
| **ORI** | Century-long disciplined commercial underwriter with no acquisitions. |
| **GL** | Simple, persistent life and supplemental-health book. Shares −4.2%/yr. |
| **PRI** | Term-life distribution. EPS up in 9 of 10 years, ~25% ROE. |
| **CPAY**, **TRU** | Kept because the cyclical-peak lens does not trigger. TRU's margin is at the 55th percentile and its worst EPS year was −6.9%. |

## Notable demotions
- **12 banks** at peak-NIM EPS that are not through-cycle best-in-class: BANF, BAC, SRCE, USB, CHCO, MTB, UMBF, SYBT, FFIN, CFR, TBBK, BFC. The main reasons were:
  - FY2–FY3 consensus growth of only 2–6% (SRCE, CHCO, FFIN, BANF, SYBT);
  - average ROE below 10% (BAC, MTB);
  - strong asset sensitivity (CFR);
  - weak 10-year EPS growth (USB).
- **Capital-markets earnings:** RJF, AMP, BNY, HLNE.
- **Other:** BRO, PLMR, LII, CRH, ALH, VERX, DHI.

## Notable promotion
- **ADBE:** 10 of 10 years of EPS growth, 26% 10-year EPS CAGR, net cash, 25.8% average ROIC. The AI threat is a deep-dive test, as it is for INTU.

## Caveat on the count
37 KEEP is below the 50–90 guide. Two things drive this:
- **Banks and wealth managers:** the explicit rules on these account for 16 of the 23 demotions.
- **Few rule-compliant promotions:** in the TOO HARD pool, the closest misses were LOPE (single customer), MMS, BAH and LDOS (government contracts), G, DOX and EPAM (AI threat to labour-based billing), and ALGN (stalled revenue). All fail an explicit rule.

If more names are needed, the next candidates in order are FFIN, CFR and BANF (banks), then LII and DHI. Each is a defensible "good, track for dislocation" name.
