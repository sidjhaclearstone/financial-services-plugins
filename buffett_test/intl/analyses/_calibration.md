# Europe & India — Stage 4 calibration (20-Oct-2026)

**Method.** The anchor is the 60 calibrated US values in `../../analyses/_results_final_v2.jsonl`; no US value was changed. I read the Test 2 and Test 3 sections of all 17 intl analyses (last `_results.jsonl` line per ticker) against these US peers:
- software/data/platforms: LSEG, WKL, AUTO, G24, BCG, IOS and ADYEN vs ADBE, INTU, BR, TRU, CPAY, GDDY and CARG
- brokers: AON and WTW vs MRSH
- industrials: TEL and HLMA vs OTIS, SNA, XYL and CSL
- consumer: LVMH and EVD vs BKNG, DECK and MCD
- lenders: HDFC Bank and Can Fin vs JPM, CBSH, EWBC and AXP
- other: HWDN and VIRP vs POOL, ZTS and COO

I used the v1/v2 yardsticks:
- A stall below the remaining bar fails about half the time.
- An endpoint recession is about 15% for cyclicals, and cyclicals are held below 80%.
- The stated value must match the arithmetic unless a peer reason holds it lower (the HAYW precedent).
- The 85% top tier needs ≥8/10 years ≥7% including 2020, mostly recurring revenue, a consensus cushion and at most one credible threat.

FX translation in reporting currency and country growth are accepted as legitimate differences where the analysis argues them. US anchors themselves mix Test 3 windows (FY1–FY5 vs FY2–FY6), so window choice was not penalised.

**Result: changed 1 of 17** (ADYEN). No value crossed a threshold.

| Ticker | P2 % before→after | P3 % before→after | Reason |
|---|---|---|---|
| ADYEN-NL | 87→**85** | 40→**37** | The margin is at its 10y high (100th pct), but the table has no reversion term and no short-record add-on (7y), despite a named disruption threat. The MRSH precedent puts it level with CPAY. P3 sat level with BR (10/10 years, buybacks) despite a shorter record and no buybacks, so it gets the BCG short-record haircut to the ADBE level. |
| WKL-NL | 84 | 15 | Unchanged. Arithmetic gives 85; held at 84 for EUR/USD translation (2018 and 2025 misses were FX years), a legitimate FX difference. FY1 breaks Test 3. |
| HLMA-GB | 84 | 33 | Unchanged. Arithmetic gives 85; held at 84 because of the COVID-year miss. EPS never fell, so it sits above OTIS (81). |
| LSEG-GB | 83 | 28 | Unchanged. Arithmetic gives ~86; held at the INTU/GL level for a 7/10 record and the AI threat. |
| AON-US | 83 | 18 | Unchanged. Held below MRSH (85): 6/10 years vs 9/10, and higher leverage. |
| WTW-US | 83 | 18 | Unchanged. Its weaker franchise is offset by an easier consensus path. |
| G24-DE | 82 | 30 | Unchanged. Level with GDDY (same AI threat) and with INTU on P3. |
| 500180-IN | 82 | 22 | Unchanged. It sits above the US banks (≤78) on a country/franchise difference: adjusted EPS never fell (worst year +12.2%) through India's NPA/NBFC cycles and COVID, and nominal growth in INR is 10–11%. |
| AUTO-GB | 80 | 18 | Unchanged. Arithmetic gives 82; held at the cyclical cap (FY21 −40%). It sits above CARG (75). |
| IOS-DE | 80 | 20 | Unchanged. Just below GDDY (82): shorter record and majority control. |
| TEL-US | 78 | 12 | Unchanged. Cyclical; level with XYL/ATMU (78). |
| VIRP-FR | 78 | 12 | Unchanged. Arithmetic gives ~81; held lower for its 2017 −65% year and EM/FX exposure. It sits above ZTS (70). |
| BCG-GB | 77 | 18 | Unchanged. Cyclical and short record; next to CARG (75). |
| 511196-IN | 75 | 3 | Unchanged. Monoline/PSU haircut; between EWBC and CFR. FY1 +3.7% breaks Test 3. |
| EVD-DE | 74 | 7 | Unchanged. Cyclical with no buybacks; just under BKNG and PLNT. |
| MC-FR | 72 | 1 | Unchanged. Cyclical; just under DECK (75). FY1 −1.1% breaks Test 3. |
| HWDN-GB | 70 | 1 | Unchanged. Below POOL/LII on two −30% years in six. FY1 +4.2% breaks Test 3. |

**Pass all three:** none. The highest P2 among Test-1 passers is 84% (WKL) and the highest P3 is 30% (G24).

**Near-misses** (P2 ≥85%, P3 ≥45% or 2 of 3 tests passed): none among the 14 Test-1 passers. Every one passes 1 of 3.

**Would-be candidates if the FCF basis were accepted.** All three are Test 1 FAIL on `fcf_check`, and NTM P/E is above 15x for each (data/stage1_universe.csv):

| Ticker | NTM P/E | P2 / P3 | If the FCF basis were accepted |
|---|---|---|---|
| ADYEN-NL | 20.5x | 85 / 37 | 1/3, and a Test 2 near-miss (`near_miss` = Y in the JSON) |
| HLMA-GB | 24.0x | 84 / 33 | 1/3 |
| EVD-DE | 17.2x | 74 / 7 | 1/3 |

None of the three would pass all three tests.

**Files.** `_results_final.jsonl` holds 17 lines with before and after values, `tests_passed`, `near_miss`, `fcf_fail_would_be_candidate` and `calibration_note`. `ADYEN-NL.md` has an updated RESULT line and a `## Calibration note`.
