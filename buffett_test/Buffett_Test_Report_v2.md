# Buffett-style screen of US equities over $1bn: v2 re-run (Test 1 widened)

**As of 19-Oct-2026.** This is a screen, not a recommendation. It contains no buy/sell views or position sizes. It updates `Buffett_Test_Report.md` (v1). Where the method is unchanged, this report refers to v1 rather than repeating it.

**Sources and conventions** (as v1 unless noted)
- **NTM P/E:** FactSet close ÷ FactSet NTM consensus mean EPS (REITs: FFO), both 19-Oct-2026. **FCF yield (new):** FactSet NTM consensus FCF per share ÷ price, 19-Oct-2026; where there is no consensus, latest-fiscal-year (operating cash flow − capex) ÷ (diluted shares × price) from FactSet Fundamentals, labelled "LTM". FCF yield is shown to one decimal because the bar sits at 6%.
- **Market cap:** FactSet GlobalPrices, 16-Oct-2026 (some write-ups quote FMP 19-Oct figures, up to 6% different; no result depends on it). **EPS history and FY1–FY3 consensus:** FactSet, 19-Oct-2026.
- **P(Test 2) and P(Test 3)** are analyst estimates, not data (`analyses/<TICKER>.md`, after joint calibration in `analyses/_results_final_v2.jsonl`); treat them as ±5–10 points. Other percentages are whole numbers.

---

## 1. Bottom line

- **What changed:** Test 1 was widened from NTM P/E <15x to **NTM P/E <18x OR FCF yield ≥6%**. That added 348 passes to v1's 780 (combined 1,128). Triage kept 18 new names; with v1's 42 that makes **60 full analyses**.
- **No company passes all three tests** (same as v1). The best Test 2 score is 88% (BR) against a 90% bar; the best Test 3 score is 40% (BR) against 50%.
- **Five near-misses** (P(Test 2) ≥85%): **BR** (88/40) and **MRSH** (85/25) are new; **ADBE** (85/37), **CPAY** (85/30) and **TRU** (85/25) are unchanged.
- **Key insight: the wider price bar adds better businesses, not passes.** The 18 new names have a median P(Test 2) of 79% (v1: 75%); 50% of them score ≥80% (v1: 24%); 39% are rated "Special" (v1: 17%). The KEEP rate barely moved (5% vs 5%).
- **The binding constraints are unchanged.** Test 2's 90% bar fails every name with one credible five-year threat. Test 3's every-year 7% bar fails nearly everything: only BR and FICO among the 212 new passes with a 10-year record grew EPS ≥7% in all 10 years (3 of 727 across both runs, with ADBE), and 6 of the 18 new names have FY1 consensus below 7%.
- **Uncertainty:** BR's 2-point Test 2 shortfall is within estimation error; its 10-point Test 3 shortfall is not.

---

## 2. What changed in the method

Tests 2 and 3, sources, triage rules, analysis template and calibration anchors are unchanged (v1 §2). v2 changes are A23–A33 in `assumptions.md`.

| Item | v2 rule |
|---|---|
| Test 1 | PASS if 0 < NTM P/E < 18x **or** FCF yield ≥ 6%. A near-miss is a P/E of 18–19x or an FCF yield of 5.5–6% (A30). |
| FCF yield | NTM consensus FCF per share ÷ price (420 candidates); fallback LTM (operating cash flow − capex) ÷ (diluted shares × price), latest FY ending 1-Jan-2025 to 19-Oct-2026 (171). FF_FREE_CF not used: it is net of dividends (A26). |
| Financials | Banks and insurers (FactSet FF_GEN_IND 04/05; 17 candidates incl. UNH): P/E route only (A27). Other non-REIT financials: NTM consensus FCF accepted, but no LTM fallback, since their cash flow includes customer/loan balances (IBKR LTM computed at 67%) (A28). |
| REITs | P/E on NTM FFO where available; all 47 REIT passes use FFO (A25, A29). |
| Prefilters | FactSet CompanyScreener on the v1 base (US HQ, primary listing, >$1bn): (a) FY2 P/E 0–20 → 1,172; (b) FF_FCF_YLD ≥4% → 794; (c) FY1 P/FCF 0–25 → 632, added because (b) uses dividend-net FCF (54 new passes came only via (c)). Union 1,419 less 780 v1 passes = 639 candidates (A23). |
| v1 names | 780 v1 passes not reprocessed; triage and analyses carry over (A24). |

---

## 3. Funnel

| Stage | v1 | v2-added | Combined | Source |
|---|---|---|---|---|
| Names screened | 826 | 639 candidates | 1,419 | FactSet CompanyScreener, 19-Oct-2026 |
| Test 1 PASS | 780 (P/E <15x) | 348 (161 P/E only / 68 FCF only / 119 both) | **1,128** | `data/stage1b_summary.json` |
| Test 1 near-miss | 33 (15–16x) | 74 (v2 definition) | 74 | as above; 42 of v1's 46 near-miss/fail names now pass |
| Test 1 fail | 13 | 164 | 164 | as above |
| Test 1 missing (no price, or no eligible earnings/FCF) | 0 | 53 | 53 | as above |
| Triage first pass: KEEP / TOO HARD / NO | 59 / 153 / 568 | 22 / 88 / 238 | 81 / 241 / 806 | `triage/batch_*.csv` |
| Triage after review: KEEP / TOO HARD / NO | 37 / 175 / 568 | 18 / 92 / 238 | **55 / 267 / 806** | `triage.csv`, `triage_v2_new.csv` |
| Stage 4 analyses | 42 (37 KEEP + 5 borderline) | 18 | **60** | `analyses/` |
| P(Test 2) ≥ 90% | 0 | 0 | 0 | `_results_final_v2.jsonl` |
| P(Test 3) ≥ 50% | 0 | 0 | 0 | as above |
| **Pass all three** | **0** | **0** | **0** | |

**v2 triage review** (`triage/review_notes_v2.md`) applied v1 precedents: it demoted NVR (homebuilder), MORN (capital-markets earnings; EPS −39% in 2022), KNSL (E&S insurer at a hard-market peak), HSY (cocoa, GLP-1) and LOW ($10.1bn levered deal, 3.5x net debt/EBITDA), and promoted AWI (consistency with CSL).

**Joint calibration** (`analyses/_calibration_v2.md`) changed 3 of the 18 new names, all on Test 2: MRSH 87→85, OTIS 84→81 and DPZ 80→77. No v1 value changed, and no value crossed a threshold.

---

## 4. Passes all three tests

**None.** All 60 analysed names pass Test 1 and fail Tests 2 and 3.

- **Test 2:** no name has a five-year path free of a credible threat; one such threat caps the score at about 85% on the shared anchor. Even BR's small threats (fee-schedule reset, tokenisation) cost about 12 points.
- **Test 3:** a five-year window almost certainly holds one weak year. BR, with 10 of 10 years ≥7%, cleared FY2020 by only 0.9 points.
- So the best currently plausible outcome for any name is 2 of 3 tests, and no analysis has an upside case that takes Test 3 to 50%.

### Closest to passing: top 12 of the 60, ranked by P(Test 2), then P(Test 3)

| Ticker | Name | Run | Test 1 route | NTM P/E | FCF yield % | Mkt cap $bn | 10y EPS CAGR % | FY1 / FY2 / FY3 cons. growth % | P(T2) % | P(T3) % | Key uncertainty |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BR | Broadridge | v2 | P/E + FCF | 16.1 | 6.0 (LTM) | 19.8 | 13 | 10 / 10 / 10 | 88 | 40 | Do proxy economics survive tokenisation, pass-through voting and any SEC/NYSE fee review? |
| ADBE | Adobe | v1 | P/E <15 | 9.0 | n/c | 95.4 | 26 | 17 / 13 / 13 | 85 | 37 | Does genAI expand Adobe's market or deflate creative seats? |
| CPAY | Corpay | v1 | P/E <15 | 13.1 | n/c | 26.3 | 13 | 28 / 15 / 18 | 85 | 30 | How much growth is organic rather than acquisitions, fuel and FX? |
| TRU | TransUnion | v1 | P/E <15 | 13.7 | n/c | 14.2 | 15 | 12 / 13 / 15 | 85 | 25 | Do mortgage and score economics stay with the bureaus through a credit slowdown? |
| MRSH | Marsh & McLennan | v2 | P/E + FCF | 16.8 | 6.2 | 89.6 | 12 | 7 / 9 / 10 | 85 | 25 | How much Risk & Insurance organic growth survives a full P&C softening cycle, with margins at a 10-year high? |
| COR | Cencora | v2 | P/E | 17.1 | 5.9 | 65.1 | 12 | 12 / 10 / 10 | 83 | 33 | Does US drug-pricing reform change how wholesalers are paid? |
| INTU | Intuit | v1 | P/E <15 | 13.8 | n/c | 86.9 | 16 | 36 / 13 / 13 | 83 | 30 | Is AI a feature Intuit sells or a substitute for DIY tax? |
| PRI | Primerica | v1 | P/E <15 | 10.5 | n/c | 8.7 | 20 | 10 / 8 / 10 | 83 | 20 | Does sales-force recruiting recover after the 2027 convention? |
| GL | Globe Life | v1 | P/E <15 | 10.3 | n/c | 13.0 | 13 | 8 / 5 / 9 | 83 | 8 | Can American Income keep growing agents without renewed regulatory attack? |
| ADSK | Autodesk | v2 | P/E | 17.5 | 5.9 | 50.1 | 29 | 21 / 13 / 14 | 82 | 30 | Does AI raise revenue per customer or cut AEC/D&M seats? |
| GDDY | GoDaddy | v1 | P/E <15 | 12.2 | n/c | 13.4 | n/a | 19 / 23 / 12 | 82 | 28 | Do AI site-builders erode new-domain and A&C demand? |
| TMUS | T-Mobile US | v1 | P/E <15 | 11.7 | n/c | 170.7 | 28 | 12 / 28 / 20 | 82 | 27 | Does wireless pricing stay rational as cable and satellite enter? |

Notes: "n/c" = not computed (v1 names passed on P/E and v1 pulled no FCF consensus). BR's 6.0% is LTM (FY Jun-2026) and flattered by working capital (analysis estimates ~5.5% normalised); it passes on P/E anyway. AZO (82/25) and ABT (82/13) tie at 82% and fall just outside the 12 (see §5). GDDY has no 10-year CAGR (7-year record); INTU's FY1 is a definition break (v1 §4).

---

## 5. Near-misses: watchlist for pre-dislocation diligence

**BR (Broadridge), new.** BR is the near-monopoly US agent for beneficial-owner proxy and investor communications, plus wealth and capital-markets technology; about 75% of revenue is recurring (analysis estimate). Adjusted EPS grew ≥7% in all 10 years FY2016–26, including FY2020 (+8%) and FY2023 (+9%), compounding at 13%; net debt/EBITDA is 1.7x (FactSet). At 16.1x (history "well above 20x", per the analysis), the market fears AI de-rating, tokenisation bypassing the proxy plumbing, and working-capital-flattered FCF. Test 2's bar is $13.72 (1.30 × FY1 $10.55); FY3 consensus of $12.73 leaves about 2.5% a year to find (FactSet, 19-Oct-2026). Failure risk of ~12% comes from a late-window bear market (~4 pts), a proxy fee or pass-through-voting reset (~3), tokenisation/AI pricing (~3) and client loss or M&A (~2.5). Test 3 is 0.90 × 0.85³ × (0.55 × 0.85 + 0.45 × 0.55) = 40%. *What would need to change:* Test 2 moves above 90% on evidence that BR becomes the communications rail for tokenised securities with no adverse SEC/NYSE fee review. Test 3 needs, on our arithmetic from the same chain, normal-year odds of clearing 7% to rise from ~0.85 to ~0.91, or near-certainty in a bear-market year, i.e. a larger cushion than today's ~9–10% growth against 7%. *Caveat:* adjusted EPS averaged 25% above GAAP over 5 years; FactSet's 0% FY2026 gap is unverified.

**MRSH (Marsh & McLennan), new.** The global #1 broker in a four-firm oligopoly (Marsh, Aon, WTW, Gallagher), plus Consulting. EPS grew ≥7% in 9 of 10 years; the only miss was 2020 (+6.7%) (FactSet). At 16.8x (6.2% NTM FCF yield), the market is pricing a soft P&C/reinsurance market (Risk & Insurance organic growth slowed to +3% in H1 2026, FactSet StreetAccount), a 25.3% EBIT margin at its 10-year high, falling fiduciary interest and 2.4x net debt/EBITDA after McGriff. Test 2's bar is $13.61; FY3 consensus of $12.57 leaves ~2.7% a year. The analysis had 87%; calibration added ~2 points of margin-reversion risk (as for LII, ATMU), giving 85%. Test 3 is 25%: FY1 consensus is +7.4%, barely over the bar ($10.47 vs $10.43, Q4 unreported), so P(FY1) is ~0.75, and a soft market caps growth after that. *What would need to change:* Test 2 reaches ~90% if Risk & Insurance organic growth holds ≥4% with 30–50bp a year of margin expansion through 2027, without margin reverting from its peak. Test 3 needs FY2026 to print ≥7% and EPS to clear 7% through a soft-pricing year; 2015–18 (+11–15% a year) suggests it is possible, but not at today's margin.

**Unchanged from v1** (details in v1 §5; no v2 calibration change):
- **ADBE (85/37):** needs net new ARR to stabilise in FY2027 and operating margin of about 36% or better under the new CEO to reach about 90% on Test 2. Test 3 would still be about 45%.
- **CPAY (85/30):** needs two more years of ≥10% organic growth to reach 88–90% on Test 2. Test 3 needs ≥7% growth through a recession or fuel downturn without acquisitions.
- **TRU (85/25):** needs mortgage and score economics to stay with the bureaus, ≥7% organic growth and leverage below 2.5x. Test 3 needs non-mortgage volumes to grow through a credit downturn; in 2023 they did not.

### Next tier: P(Test 2) of 80–84% after calibration (all 60 names)

| Ticker | Run | P(T2) % | P(T3) % | Single thing that would need to change | Upside-case P(T2) |
|---|---|---|---|---|---|
| COR | v2 | 83 | 33 | Contract renewals on fee-for-service terms that are insensitive to list-price cuts, plus specialty/MSO profit growing ≥10% | "toward 90%" (not quantified) |
| INTU | v1 | 83 | 30 | Two filing seasons of stable TurboTax DIY share | 88–90% |
| PRI | v1 | 83 | 20 | Life-licensed sales force back to 3–5% growth after the 2027 convention | ~88% |
| GL | v1 | 83 | 8 | Two years of mid-single-digit agent growth at American Income, and closure of the EEOC matter | not quantified |
| ADSK | v2 | 82 | 30 | AI/consumption revenue >5% of revenue by FY2029, stable net revenue retention, SBC <10% of revenue | ~88% |
| GDDY | v1 | 82 | 28 | A&C bookings back to double digits, with Airo driving new customers | ~88% |
| TMUS | v1 | 82 | 27 | Churn stabilises and ARPA grows ≥3% through 2027 | ~88% |
| AZO | v2 | 82 | 25 | FY2027 EBIT growth of +8–10% at ~18.5% margin, with buybacks back above $2.5bn a year | ~87% |
| ABT | v2 | 82 | 13 | Libre CGM growth back to ≥15% and net debt below 1x by 2028 | ~87% |
| OTIS | v2 | 81 | 1 | Two clean years of ≥8% EPS growth after a flat 2026, with service retention stable | ~88% (pre-calibration) |
| BLKB | v1 | 80 | 18 | Gross dollar retention reaches 92%, plus AI revenue in 2027 | 85–88% |
| GEHC | v1 | 80 | 18 | Adjusted EBIT margin of 16%+ by FY2027, with China stable | >90% (pre-calibration) |
| PAYX | v2 | 80 | 6 | Two years of ≥6% organic growth with Paycor cross-sell | ~85% |
| SCI | v2 | 80 | 9 | Two years of positive comparable funeral volumes, with leverage held below 4x | ~85% |

Sources: §6 of each `analyses/<TICKER>.md`; v1 §5. No upside case lifts any of these to 50% on Test 3; OTIS's FY1 (−0.2%) and GL's FY2 (+5%) consensus already break it.

**Test 1 near-misses (74, not analysed):** P/E of 18–19x or FCF yield of 5.5–6%. They are listed in `data/stage1b_summary.json` and include NFLX, ICE, SYK, MRK, CHE, ULTA and URI.

---

## 6. v2 new names: the 18 KEEP_V2 analyses

Ranked by P(Test 2), then P(Test 3). All 18 pass Test 1 only (1 of 3 tests). Specialness uses the PM's test from `approach_summary.md`.

| Ticker | Test 1 route | NTM P/E | FCF yield % | P(T2) % | P(T3) % | Specialness (short) | Conf. | Calibration change |
|---|---|---|---|---|---|---|---|---|
| BR | P/E + FCF | 16.1 | 6.0 (LTM) | 88 | 40 | Special: proxy near-monopoly | M | — |
| MRSH | P/E + FCF | 16.8 | 6.2 | 85 | 25 | Special: broker oligopoly | M | 87→85 |
| COR | P/E | 17.1 | 5.9 | 83 | 33 | Good–track: wholesale oligopoly, policy-exposed | M | — |
| ADSK | P/E | 17.5 | 5.9 | 82 | 30 | Special: AEC lock-in; AI and SBC caveats | M | — |
| AZO | P/E | 17.8 | 4.0 | 82 | 25 | Special: capital allocation, parts oligopoly | H | — |
| ABT | P/E | 17.5 | 4.1 (LTM) | 82 | 13 | Good–track: CGM/diagnostics growth | M | — |
| OTIS | P/E + FCF | 16.1 | 6.9 | 81 | 1 | Special: elevator service annuity | M | 84→81 |
| PAYX | FCF only | 18.1 | 6.5 | 80 | 6 | Good–track: SMB payroll, no secular driver | M | — |
| SCI | P/E + FCF | 17.9 | 7.1 | 80 | 9 | Good–track: funeral scale, 3.8x leverage | M | — |
| AXP | P/E | 16.1 | n/a | 78 | 18 | Special: closed-loop premium network; credit-cyclical | M | — |
| XYL | P/E | 17.0 | 5.0 | 78 | 22 | Good–track: secular water | M | — |
| CPRT | P/E | 16.6 | 5.5 | 78 | 4 | Special, moat under test: salvage duopoly | M | — |
| DPZ | P/E + FCF | 15.0 | 6.0 | 77 | 10 | Good–track: aggregators narrowing moat | M | 80→77 |
| AWI | P/E | 17.9 | 5.1 | 76 | 20 | Good–track: ceiling duopoly (promoted at review) | M | — |
| WMS | FCF only | 18.6 | 6.1 | 76 | 1 | Good–track: plastic-pipe conversion | M | — |
| TSCO | P/E | 16.2 | 4.0 | 75 | 1 | Good–track: rural retail | M | — |
| MCD | P/E | 17.8 | 4.6 | 70 | 2 | Good–track: no secular driver | M | — |
| SNA | P/E | 17.4 | 2.9 | 65 | 1 | Good–track: van channel, no secular driver | M | — |

Sources: FactSet (19-Oct-2026) for P/E and FCF yield, from `data/stage1b_universe.csv`; `_results_final_v2.jsonl` for the probabilities.

Notes: AXP's LTM yield (7.3%) is not applied to other financials (A28). FY1 consensus below 7% breaks Test 3 in year one for OTIS, TSCO, WMS, SNA, CPRT and MCD. Only PAYX and WMS depend on the FCF route, and WMS clears 6% by less than 0.1 points.

---

## 7. Where the v2 discards came from (approximate)

The 330 v2 discards are the 238 NO plus 92 TOO HARD verdicts in `triage_v2_new.csv`.

**Method (approximate):** each discard's triage reason was keyword-matched and assigned to the first matching bucket (REITs by flag). Counts show the dominant cause only; expect ±15% misclassification per bucket.

| Primary reason (approx.) | NO | TOO HARD | Total | Typical examples |
|---|---|---|---|---|
| REITs: equity/debt-funded growth, FFO/share well below 7%, leverage | 46 | 1 | 47 | O, ADC, PSA, AMT, SBAC |
| Commodity prices (energy, metals, chemicals, fuel) | 44 | 3 | 47 | FCX, DOW, SLB, EQT, CLF |
| Disruption / regulatory / litigation / customer-concentration threat | 38 | 22 | 60 | AMGN, INCY, UNH, EXLS, PEP (GLP-1) |
| Cyclical peak or cyclical earnings | 42 | 17 | 59 | CMI, STX, PCAR, ZBRA, TGT |
| Unproven: loss-making, short profit record, single product | 19 | 15 | 34 | BCRX, UBER, RDDT, SNAP, GLIBK |
| Rate / credit / underwriting / housing cycle | 14 | 15 | 29 | NVR, KNSL, WRB, AFL, LOW |
| No specialness / no route to ≥7% (mostly utilities) | 22 | 5 | 27 | DUK, XEL, ED, PEG, MZTI |
| Acquisition / leverage-driven growth | 5 | 6 | 11 | FTV, LHX, ICUI, PFGC |
| Capital-markets activity | 4 | 5 | 9 | BLK, BX, MORN, SEIC |
| Balance sheet | 3 | 0 | 3 | GPC, SBGI |
| Too complex / mid-transformation | 0 | 2 | 2 | ECHO, GHC |
| Unclassified | 1 | 1 | 2 | LMT, PTON |
| **Total** | **238** | **92** | **330** | |

Compared with v1, REITs and loss-making/unproven names are new large buckets. Acquisition-led growth and transformations are mostly secondary reasons (e.g. AJG, ROP, CARR, DD).

**FCF-route names:** of the 68 FCF-only passes, 2 were kept (PAYX, WMS; both with 10-year FCF conversion above 1x), 16 were TOO HARD and 50 NO, including all 13 on the LTM basis. Typically the business is loss-making or newly profitable (~30 of 66 reasons), or the FCF rests on consensus, working capital, prepayments, SBC or one-offs (~26; overlapping keyword counts). KEEP rates by route: P/E only 7% (11/161), both 4% (5/119), FCF only 3% (2/68).

---

## 8. Data gaps and low-confidence names (v2-specific)

**Data issues** (sources: `data/stage1b_summary.json`, `data/stage1b_universe.csv`, `assumptions.md` A23–A33)

- **53 MISSING:** 48 have no FactSet price on 16 or 19-Oct-2026 (acquired or delisted names still in the screener, e.g. BERY, DFS, HOLX, WBD, EA). 5 are financials with a price but no NTM EPS consensus, which cannot use the FCF route: FINN, FMBL, L (Loews), JOE, NHC. ACVA uses the 16-Oct close (A25).
- **13 FCF-only passes on trailing FCF** (AGNT, AGX, BCRX, GLIBK, MBC, MDXG, MQ, NRP, PTCT, PTEN, RHLD, SEPN, YOU) may reflect one-off cash (royalty sales, working-capital releases). Kept as passes for triage to judge (A31); all 13 were discarded.
- **47 REITs on P/FFO** (FactSet NTM FFO; 33 also pass on FCF). All discarded (46 NO, 1 TOO HARD).
- **Financials on P/E only:** 8 bank/insurer passes; 19 other financials, 10 of which had an LTM yield not applied. Among analysed names this affects only AXP (7.3% LTM), which passes on P/E.
- **Thin history:** GLIBK (recent GCI spin) has 3 years of standalone EPS ending in a −$7.76 GAAP loss and FCF conversion of ~0.1x; RHLD has 2 years, both negative, and an FMP market cap (as does SUNB). Both TOO HARD. OTIS has only 5 years of standalone adjusted EPS.
- **Market cap:** FactSet for 346 of 348 new passes (345 at 16-Oct, 1 at 19-Oct); FMP 19-Oct for RHLD and SUNB.
- **Adjusted vs GAAP EPS** (5-year average gap) among new names: ADSK 90%, COR 57%, XYL 27%, BR 25%, ABT 21%. AXP's FY1 includes a GBT gain (analysis flag).
- **v1 issues** (adjusted/GAAP gap, thin coverage, short histories, INTU/JPM/AGM/CPAY FY1 distortions) still apply (v1 §8).

**Low-confidence analyses.** None of the 18 v2 analyses is rated Low; AZO is the only one rated High. The v1 low-confidence names (BANF, AGM, HAYW, BRC) are unchanged, and none is within 5 points of a threshold.

**Top 3 data issues for v2**

1. **FCF yield mixes forecast (NTM consensus) and trailing (LTM) bases**, and the LTM fallback can capture one-off cash. The route is marginal for WMS (6.07%), DPZ (6.03%) and BR (6.01%); it decides Test 1 only for PAYX and WMS, and a small move would push WMS below the bar.
2. **The adjusted vs GAAP EPS gap.** Tests 2 and 3 are judged on adjusted consensus. Four of the five near-misses exceed the 15% flag: TRU 122%, ADBE 34%, CPAY 34% and BR 25%. Among new names, ADSK (90%) and COR (57%) would look materially worse on GAAP.
3. **Universe leakage and the financials rule.** 53 names could not be tested. Most are gone, but L (Loews) was excluded only for lack of NTM EPS consensus. Other-financials FCF is ignored by design (A28), so an FCF-cheap broker or card network is visible only if its P/E is also below 18x.

---

## 9. Files

All files are in `/home/user/financial-services-plugins/buffett_test/`.

- **`Buffett_Test_Data_v2.xlsx`:** tabs **Universe** (1,202 names: 1,128 PASS with route, FCF yield, NTM P/E, price, NTM EPS/FFO, market cap and RBICS, plus 74 near-misses), **Triage** (1,128 final verdicts: 55 KEEP / 267 TOO HARD / 806 NO), **Analysis** (60 Stage 4 results with history statistics) and **Sources** (source and as-of date per data item).
- **`triage_v2_new.csv`:** final verdicts for the 348 new names (supporting: `triage/batch_41–58.csv`, `triage/review_overrides_v2.csv`, `triage/review_notes_v2.md`). v1 verdicts remain in `triage.csv`.
- **`analyses/`:** 60 write-ups (`<TICKER>.md`), `_results_final_v2.jsonl` (after joint calibration) and `_calibration_v2.md`.
- **`data/`:** `stage1b_universe.csv` (639 candidates with `pe_route`, `fcf_route`, `fcf_yield_used`, `fcf_basis`), `stage1b_summary.json`, `v2_new_passes.txt`, per-company `<TICKER>.json` / `_summary.json`, and `data_gaps.json` (v1).
- **`assumptions.md`:** A1–A33 (v2 items A23–A33). **`Buffett_Test_Report.md`:** v1 report, for unchanged method detail.
