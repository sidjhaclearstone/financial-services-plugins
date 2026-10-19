# Stage 4 calibration review, v2 re-run (19-Oct-2026)

**Method.** The 42 calibrated v1 values (`_results_final.jsonl`) are the anchor. I read the Test 2 and Test 3 sections of all 18 KEEP_V2 analyses (last `_results.jsonl` line per ticker) and of their v1 peers:
- software/data: ADSK, BR vs ADBE, INTU, CPAY, TRU, GDDY, BLKB
- brokerage: MRSH vs GL, PRI
- healthcare: ABT, COR vs BSX, GEHC, ZTS, COO
- consumer: AZO, TSCO, MCD, DPZ vs BOOT, DECK, PLNT, SFM, POOL
- industrials: AWI, OTIS, SNA, XYL, WMS, CPRT vs CSL, AOS, ATMU, HAYW, DORM, LII
- financials: AXP vs JPM, CBSH
- services: SCI, PAYX vs BFAM

I also checked `summarize.py` stats (years ≥7%, worst year, margin percentile, ND/EBITDA, FY1–FY3 consensus). I used the v1 yardsticks:
- **Stall weight.** A stall where growth falls below what is still needed counts as a failure about half the time.
- **Endpoint recession.** About 15% for cyclicals, with any cyclical name held below 80%.
- **Arithmetic.** The stated probability must match the threat table, unless a peer reason holds it lower (the HAYW precedent).
- **Top tier.** The 85% level (ADBE, CPAY, TRU) is for names with ≥8/10 years ≥7% including 2020, mostly recurring revenue, a consensus cushion and at most one credible threat.

**Result.** I changed 3 of 18, all on Test 2 only. No value crossed a pass threshold. No v1 value changed: no v2 comparison exposed a v1 inconsistency.

| Ticker | P2 % before→after | P3 % before→after | Reason |
|---|---|---|---|
| BR | 88 | 40 | unchanged. 10/10 years incl. 2020, ~75% recurring, 1.7x leverage, no single large threat. It is above ADBE/CPAY/TRU, but its regulatory and tokenisation tails keep it under 90%. Its P3 sits at the top of the band with ADBE (37%). |
| MRSH | 87→**85** | 25 | Margin is at its 10y high (100th pct) and consensus sits above the 8.0% driver stack, but the table had no margin-reversion term (LII/ATMU carry one). Adding ~2 pts of failure makes it level with TRU. |
| COR | 83 | 33 | unchanged. Non-cyclical, 9/10 years. The policy threat is weighted sensibly because FY3 consensus is already near the bar. Same level as GL/INTU. |
| ABT | 82 | 13 | unchanged. Many small threats, no single large one. Above GEHC (80%). |
| ADSK | 82 | 30 | unchanged. The same AI threat as ADBE plus construction cyclicality, and a shorter record. Sits just below ADBE (85/37). |
| AZO | 82 | 25 | unchanged. Its stall is already weighted 0.5. Its FY25–26 stall and capex-constrained buybacks rule out the top tier. |
| OTIS | 84→**81** | 1 | FY1 is flat, and FY2–3 consensus (+11–12%) sits above its own 8.5% stack. The rebound-failure stall is set at 20%×0.5, as for GEHC. A 3/5 record and 2.9x leverage. |
| PAYX | 80 | 6 | unchanged. Arithmetic gives 83. It is held at the BLKB/GEHC level (80%) on a peer basis. Its "0.3-pt cushion" refers to the 7% Test 3 bar; the Test 2 cushion is ~1.9 pts. |
| SCI | 80 | 9 | unchanged. Arithmetic gives 83. It is held lower for thin coverage, 3.8x leverage and a 6/10 record (HAYW precedent). |
| DPZ | 80→**77** | 10 | The aggregator stall (3–4% growth) straddles the 3.7%/yr needed after FY3, so it is weighted 0.5 as for PLNT and TSCO. It stays above PLNT (75%). |
| XYL | 78 | 22 | unchanged. Cyclical, with 2020 at −32%. Level with ATMU. Its P3 is in line with AWI and BFAM. |
| CPRT | 78 | 4 | unchanged. A 0.5 stall weight would give 77%. Held at 78% because of $4.4bn net cash (AOS precedent). FY1 at +4.5% breaks Test 3. |
| AXP | 78 | 18 | unchanged. Arithmetic gives 82, held below 80% as a cyclical (BKNG 78%). P3 is inside the ≤25% financials band. |
| AWI | 76 | 20 | unchanged. Sits between CSL (74%; FY3 consensus at the bar) and ATMU (78%). |
| WMS | 76 | 1 | unchanged. Cyclical, with its stall and margin threats overlap-adjusted. FY1 is −0.4%. |
| TSCO | 75 | 1 | unchanged. Level with POOL (75%). FY1 is −5.9%. |
| MCD | 70 | 2 | unchanged. Its stack of 5.5% is barely above the 5.4% bar. Level with AOS (70%). |
| SNA | 65 | 1 | unchanged. Arithmetic gives 68. It sits below AOS and MCD because it combines cyclicality with a stack on the bar. FY1 is +2.9%. |

**Test 3.** No v2 Test 3 values changed. Six names are broken by FY1 consensus: OTIS, TSCO, WMS, SNA, CPRT and MCD. The others fall within the 20–40% compounder band or below it, and financials stay at or under 25%. The highest P3 across all 60 names is BR at 40%.

**Pass all three (60 names):** none. The highest P2 is BR at 88%. No name has P2 ≥90% or P3 ≥50%.

**Near-misses (60 names; P2 ≥85% or P3 ≥45%; no name passes 2 of 3):**
- **BR** (88/40)
- **ADBE** (85/37)
- **CPAY** (85/30)
- **TRU** (85/25)
- **MRSH** (85/25)

The full 60-record set is in `_results_final_v2.jsonl`. MRSH.md, OTIS.md and DPZ.md now carry an updated RESULT line and a `## Calibration note` section.
