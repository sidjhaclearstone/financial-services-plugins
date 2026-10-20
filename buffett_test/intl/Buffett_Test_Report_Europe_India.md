# Buffett-style screen of Europe and India equities over $1bn

**As of 19-Oct-2026.** This is a screen, not a recommendation. It contains no buy/sell views or position sizes. It applies the US method (`../Buffett_Test_Report.md` v1, `../Buffett_Test_Report_v2.md` v2) to companies headquartered in Europe and India. Where the method is unchanged, this report refers to the US reports rather than repeating them.

**Sources and conventions**
- **NTM P/E:** FactSet GlobalPrices close in USD, 19-Oct-2026, ÷ FactSet NTM consensus mean EPS in USD (estimate date 20-Oct-2026, accepted as equivalent; I9). For REITs and listed property companies the denominator is NTM FFO (I11, I16).
- **FCF yield:** FactSet NTM consensus FCF per share ÷ price (USD). Where there is no consensus, the fallback is latest-FY (operating cash flow − capex) ÷ (diluted shares × price) from FactSet Fundamentals, labelled "LTM" (I12). FCF yield is shown to one decimal because the bar sits at 6%.
- **Market cap ($bn):** taken from each analysis header. Sources are FMP at 19-Oct-2026, FMP local-currency value × FRED FX at 16-Oct-2026, or FactSet USD close × diluted shares. The >$1bn screen itself used FactSet `FF_MKT_VAL` in USD.
- **Currency:** valuation (P/E, FCF yield, market cap) is in USD. EPS history, 10-year EPS CAGR, FY1–FY3 consensus growth and the Test 2/3 probabilities are in each company's **reporting currency** (Ccy column), from FactSet Fundamentals (currency DOC) and EstimatesConsensus (currency ESTIMATE), pulled 19–20-Oct-2026.
- **P(Test 2), P(Test 3):** these are analyst estimates, not data. They come from `analyses/<KEY>.md` after joint calibration against the 60 US values (`analyses/_results_final.jsonl`, `analyses/_calibration.md`). Treat them as ±5–10 points.
- **Tests (unchanged from the US runs):**
  - Test 2: P(EPS five years out ≥ 1.30 × FY1) ≥ 90%.
  - Test 3: P(EPS growth ≥ 7% in every one of the next five years) ≥ 50%.
- Other percentages are whole numbers. FY1 growth is shown to one decimal where rounding would cross 7%.

---

## 1. Bottom line

- **No company passes all three tests, in either phase.**
  - **Phase 1 (FCF yield ≥6%):** 599 passes produced 12 KEEPs, all European. 3 of the 12 (ADYEN, HLMA, EVD) then failed the Stage 4 FCF check, leaving 9 Test 1 passers.
  - **Phase 2 (P/E <15x, not already in Phase 1):** 387 passes produced 5 KEEPs: HWDN, WTW and VIRP from Europe, Can Fin Homes and HDFC Bank from India.
- **No near-miss among the 14 Test 1 passers.**
  - Best Test 2: WKL 84%. LSEG, AON and WTW are at 83%; G24 and HDFC Bank at 82%.
  - Best Test 3: G24 30%.
  - ADYEN (85/37) would be the only near-miss, but it fails Test 1.
- **Compared with the US:** the US v2 best was BR at 88% (Test 2) and 40% (Test 3), with five names at ≥85%. Here the best passer is 84%, one point below the US near-miss line. The KEEP rate is 2% of passes (17 of 986) against 5% in the US (55 of 1,128).
- **Why Europe passes so many names and keeps so few:** Europe's ≥6% FCF universe is dominated by cyclicals, state-influenced companies and leveraged names. 56% of the European base passes Test 1. About 64% of European Phase 1 discard reasons cite commodity prices or cyclicality, state ownership, or leverage (approximate; §7).
- **Why India yields almost nothing:**
  - India's quality franchises are too expensive for either bar: 30–60x earnings and 1–4% FCF yields (triage review).
  - India's cheap names are PSUs, commodity producers and lenders. About 40% of Indian discard reasons cite state ownership or government policy.
- **Uncertainty:** WKL's 6-point Test 2 shortfall is at the edge of estimation error. Every Test 3 shortfall (≥20 points) is not. The weakest input is the FCF yield itself: a quarter of the Phase 1 KEEPs failed reconciliation.

---

## 2. What changed in the method

Tests 2 and 3, the analysis template, the triage verdict rules and the calibration anchors are unchanged (US v1 §2, v2 §2). Europe/India items are I1–I20 in `assumptions.md`.

| Item | Europe/India rule |
|---|---|
| Test 1, two phases | **Phase 1 (primary):** FCF yield ≥6%. **Phase 2 (secondary):** 0 < NTM P/E < 15x, for names not already in Phase 1. The P/E bar is US v1's 15x, not US v2's 18x. Near-miss: P/E of 15–16x or FCF yield of 5.5–6% (I13–I15). |
| FCF definition | Same as US v2 A26. FactSet `FF_FREE_CF` is not used because it is net of dividends. Banks and insurers are P/E route only (191 candidates). Other financials and REITs may use NTM consensus FCF only, with no LTM fallback; 74 names lost the FCF route this way (I13). |
| FCF check (new) | In Stage 4, every Phase 1 KEEP whose NTM yield rests on consensus while its LTM yield is far lower is reconciled for customer float, working capital and capex timing. If ≥6% cannot be supported, Test 1 fails unless P/E <15x rescues it (`stage4_prompt.md`). |
| Currency | Valuation is in USD (FactSet converts), so ratios are effectively local-currency ratios. Growth and the probabilities are in reporting currency, so FX translation does not distort EPS growth. Each analysis carries an FX-translation line (I8). |
| Triage lenses (new) | (1) state ownership / policy risk; (2) promoter and group governance (India); (3) regulated returns, usually <7% growth; (4) FX translation; (5) whether Phase 1 FCF is recurring. Strictness is the same as the US (`stage23_prompt.md`). |
| Countries | Europe = 34 HQ countries: AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GG, GR, HR, HU, IE, IM, IS, IT, JE, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK. Russia, Belarus, Ukraine and Turkey are excluded. India = IN. HQ is FactSet entity country, primary listing only (I1–I3). |
| Non-home listings | 82 European and 3 Indian HQ names have their primary listing elsewhere (e.g. AON, WTW, TEL, CB on NYSE). They are kept. None was in the US-HQ universe, so nothing is double-counted (I4). |
| Property | European listed property is treated as REIT-like. P/E is taken on NTM FFO for 59 of 74 flagged names (I16). |

---

## 3. Funnel

**Test 1 by region** (FactSet CompanyScreener, GlobalPrices and EstimatesConsensus, 19-Oct-2026; `data/stage1_summary.json`)

| Stage | Europe | India | Total |
|---|---|---|---|
| Base universe (HQ in region, primary listing, >$1bn) | 1,544 | 534 | 2,078 |
| Prefilter candidates | 1,297 | 438 | 1,735 |
| **Test 1 PASS** | **869** (56% of base) | **117** (22%) | **986** |
| – Phase 1: FCF ≥6% (of which also P/E <15x; LTM basis) | 563 (444; 53) | 36 (18; 10) | 599 |
| – Phase 2: P/E <15x only (of which banks/insurers) | 306 (125) | 81 (22) | 387 |
| Near-miss / fail / missing | 64 / 319 / 45 | 16 / 293 / 12 | 80 / 612 / 57 |

**Triage and analysis by region and phase** (`triage.csv`, `triage/review_notes_p1.md`, `triage/review_notes_p2.md`, `analyses/_results_final.jsonl`)

| Stage | Europe P1 | Europe P2 | India P1 | India P2 | Total |
|---|---|---|---|---|---|
| Triage first pass: KEEP / TOO HARD / NO | 12 / 130 / 421 | 5 / 61 / 240 | 0 / 6 / 30 | 2 / 15 / 64 | 19 / 212 / 755 |
| Review changes | DTE out, LSEG in | CB, AAK out | none | none | 4 |
| **Triage final: KEEP / TOO HARD / NO** | **12** / 130 / 421 | **3** / 63 / 240 | **0** / 6 / 30 | **2** / 15 / 64 | **17** / 214 / 755 |
| Stage 4 analyses | 12 | 3 | 0 | 2 | 17 |
| FCF check FAIL (Test 1 fails) | 3 (ADYEN, EVD, HLMA) | n/a | n/a | n/a | 3 |
| Test 1 passers after Stage 4 | 9 | 3 | 0 | 2 | 14 |
| P(Test 2) ≥ 90% / P(Test 3) ≥ 50% | 0 / 0 | 0 / 0 | n/a | 0 / 0 | 0 / 0 |
| **Pass all three** | **0** | **0** | **0** | **0** | **0** |

**Phase 1 review** (`triage/review_notes_p1.md`):
- **DTE demoted to TOO HARD.** Its 17.1% FCF yield is a consolidation artefact: it includes 100% of T-Mobile US FCF, but DTE owns about 52%. Its 10-year average ROIC is 3.8%, and the German state holds about 28%.
- **LSEG promoted to KEEP.** Refinitiv is seasoned, adjusted EPS grew 8.7%/yr over 2021–25, net debt/EBITDA is 1.73x, and the case is consistent with WKL and US TRU.

**Phase 2 review** (`triage/review_notes_p2.md`):
- **CB demoted.** It is at the peak of the P&C cycle, the same profile as US TRV, which the US run held TOO HARD.
- **AAK demoted.** Its margin rose from 5.1% to 10.6% in two years and sits at the 91st percentile, a cyclical peak.
- The reviewer names CB, then ZURN, then AAK as the next candidates.

**Calibration** (`analyses/_calibration.md`) changed only ADYEN: Test 2 87→85%, Test 3 40→37%. No value crossed a threshold.

---

## 4. Phase 1 results (FCF yield ≥6%)

### Pass all three tests

**None.** Every Test 1 passer fails both Test 2 and Test 3, passing 1 of 3 tests. The highest P(Test 2) among the 9 passers is 84% (WKL) and the highest P(Test 3) is 30% (G24).

### Closest: the 12 Phase 1 KEEPs, ranked by P(Test 2), then P(Test 3)

| Ticker | Name | Country | Ccy | Test 1 | FCF yield % | NTM P/E | Mkt cap $bn | 10y EPS CAGR % | FY1 / FY2 / FY3 cons. % | P(T2) % | P(T3) % | Key uncertainty |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADYEN | Adyen | NL | EUR | **FAIL** (FCF check) | 6.0 | 20.5 | 29.4 | 34 (7y) | 16 / 22 / 24 | 85 | 37 | Does the take rate stabilise against Stripe and agentic payment rails? |
| HLMA | Halma | GB | GBP | **FAIL** (FCF check) | 6.4 | 24.0 | 17.2 | 13 | 18 / 11 / 9 | 84 | 33 | Is photonics growth durable or an AI-capex spike? |
| WKL | Wolters Kluwer | NL | EUR | PASS (FCF + P/E) | 7.3 | 13.8 | 21.0 | 11 | 6.6 / 10 / 11 | 84 | 15 | Is genAI a feature WKL monetises or a substitute for its expert content? |
| LSEG | London Stock Exchange Group | GB | GBP | PASS (FCF) | 8.1 | 16.3 | 55.7 | 12 | 15 / 15 / 12 | 83 | 28 | Do AI agents make LSEG data more valuable or commoditise Workspace? |
| AON | Aon | IE (NYSE) | USD | PASS (FCF + P/E) | 6.4 | 14.5 | 61.5 | 11 | 9 / 9 / 16 | 83 | 18 | Does organic growth hold ≥5% through a P&C soft cycle? |
| G24 | Scout24 | DE | EUR | PASS (FCF) | 6.0 | 17.4 | 5.6 | 14 (9y) | 15 / 18 / 17 | 82 | 30 | Does AI search route around ImmoScout24 or through it? |
| AUTO | Autotrader | GB | GBP | PASS (FCF + P/E) | 8.1 | 13.1 | 5.5 | 10 | 13 / 14 / 13 | 80 | 18 | Can revenue per retailer keep rising ~5%/yr despite dealer pushback and AI search? |
| IOS | IONOS | DE | EUR | PASS (FCF) | 6.9 | 15.9 | 5.5 | 25 (7y) | 12 / 25 / 17 | 80 | 20 | Do AI products outpace AI-native site builders, under United Internet control? |
| TEL | TE Connectivity | IE (NYSE) | USD | PASS (FCF) | 6.2 | 16.2 | 61.5 | 9 | 31 / 14 / 11 | 78 | 12 | Does EPS hold through the next auto downturn from an AI-inflated base? |
| BCG | Baltic Classifieds | LT (LSE) | EUR | PASS (FCF) | 6.0 | 16.1 | 0.95 | 16 (3y) | 12 / 18 / 14 | 77 | 18 | How much pricing headroom is left in a small, volume-flat market? |
| EVD | CTS Eventim | DE | EUR | **FAIL** (FCF check) | 7.6 | 17.2 | 6.7 | 11 | 17 / 9 / 10 | 74 | 7 | Can ticketing compound at 6–8% after LA28, with cash returned rather than spent on venues? |
| MC | LVMH | FR | EUR | PASS (FCF) | 6.6 | 16.5 | 217.9 | 12 | −1 / 9 / 9 | 72 | 1 | Is 2024–26 a cyclical trough or a reset to ~5% organic growth? |

Sources:
- FCF yield and NTM P/E: FactSet, 19-Oct-2026 (`data/stage1_universe.csv`).
- 10y EPS CAGR, FY1–FY3 consensus and probabilities: `analyses/_results_final.jsonl`.

Notes:
- **CAGR windows:** "(7y)/(9y)/(3y)" marks a shorter record than 10 years.
- **Test 3 breaks in year one** where FY1 consensus is below 7%: WKL (+6.6%) and MC (−1.1%).
- **Margin above the 6% bar:**
  - G24 (6.03%) and BCG (6.01%) clear 6% by less than 0.05 points. P/E does not rescue either.
  - LSEG's 8.1% NTM yield compares with 3.7% LTM. The analysis accepts it after a capex spike, but only "just" on a trailing basis.
- **Robust to the FCF basis:** only WKL, AUTO and AON also pass on P/E.
- **Specialness** (PM test, `approach_summary.md`): ADYEN, HLMA, WKL, AUTO, AON and MC are rated "Special". All the others are "Good – track for dislocation".

### The three FCF-check failures

These are would-be candidates. Each would pass 1 of 3 tests if its FCF basis were accepted, and none would pass all three (`_calibration.md`).

| Ticker | NTM FCF yield | LTM FCF yield | Reconciled yield (analysis) | NTM P/E | Why the ≥6% basis failed |
|---|---|---|---|---|---|
| ADYEN | 6.0% | 3.1% | ~5.0–5.5% | 20.5x | Cash flow includes merchant settlement float. 10-year FCF conversion is 1.73x; 2022 FCF was €1.93bn against net income of €0.56bn. Net income is the owner-earnings measure. |
| HLMA | 6.4% | 3.0% | ~3.4% | 24.0x | The per-share FCF consensus ($2.92) is about 1.9x aggregate FY Mar-27 FCF consensus (£440m, n=9). That is irreconcilable with ~1.0x FCF conversion; the likely cause is contributor mix (estimate). |
| EVD | 7.6% | 1.5% | ~5.5–6.0% | 17.2x | NTM cash rests on ticket float, the Milan arena capex (>€400m gross) rolling off, and LA28 timing. |

ADYEN matters most. At 85/37 it would be the only Test 2 near-miss in this run. It is level with US CPAY (85/30).

---

## 5. Phase 2 results (P/E <15x)

**Pass all three:** none. All 5 KEEPs pass Test 1 only.

| Ticker | Name | Country | Ccy | FCF yield % | NTM P/E | Mkt cap $bn | 10y EPS CAGR % | FY1 / FY2 / FY3 cons. % | P(T2) % | P(T3) % | Key uncertainty |
|---|---|---|---|---|---|---|---|---|---|---|---|
| WTW | Willis Towers Watson | GB (NYSE) | USD | n/a (5.0 LTM, not applied) | 14.1 | 29.2 | 10 | 16 / 16 / 19 | 83 | 18 | Can Propel and AI lift the margin toward 30% without losing consulting (HWC) revenue? |
| HDFC Bank | HDFC Bank | IN | INR | n/a (bank) | 12.3 | 115.7 | 15 | 8 / 16 / 16 | 82 | 22 | Does ROA recover from ~1.9% under a new CEO as the LDR falls? |
| VIRP | Virbac | FR | EUR | 4.8 | 14.9 | 3.2 | 24 | 13 / 11 / 10 | 78 | 12 | Is the capex-heavy transformation delivered, with margin rising toward 20%? |
| Can Fin Homes | Can Fin Homes | IN | INR | n/a (lender) | 8.1 | 1.0 | 21 | 4 / 13 / 14 | 75 | 3 | Was FY26 a peak-spread year against bank competition? |
| HWDN | Howden Joinery | GB | GBP | 5.9 | 14.0 | 5.6 | 6 | 4 / 11 / 10 | 70 | 1 | Does margin recover to 16–17%, or is ~15% structural? |

Sources: as in §4.

Notes:
- **Financials:** WTW is an "other financial", so LTM FCF is not applied to it (I13). Banks and HFCs are on P/E only.
- **VIRP's P/E** of 14.93x clears the bar by 0.07x. Its 24% CAGR is flattered by a depressed 2015 base; it is 8%/yr from 2014.
- **Test 3 breaks in year one** for HWDN (+4.2%) and Can Fin (+3.7%).
- **Specialness:** HDFC Bank is rated "Special". The other four are "Good – track for dislocation".
- **Review demotions:** CB (12.3x) and AAK (13.1x) were Phase 2 first-pass KEEPs that the review demoted (§3).

---

## 6. Watchlist for pre-dislocation diligence

The names below have P(Test 2) ≥82% in either phase, with ADYEN and HLMA flagged separately. None is a near-miss. Each paragraph covers what would need to change and the nearest US comparable, scored as P(T2)/P(T3) from `../analyses/_results_final_v2.jsonl`.

**WKL – Wolters Kluwer (84/15; Phase 1, 7.3% FCF yield and 13.8x P/E).**
- **Test 2:** recurring organic growth of ≥7% through 2027 with stable retention, plus buybacks back above €1bn, would lift it to 88–90%.
- **Test 3:** FY1 consensus breaks it. The mean is €5.641 against €5.66 needed, so P ≈ 0.40. Excluding FY1, Test 3 would be ~38%.
- **FX:** both historical misses (2018, 2025) were USD-translation years, since ~60% of revenue is in USD (estimate).
- **US comparable:** ADBE (85/37), the same AI-substitution question for a professional-workflow moat. WKL is held 1 point lower for FX.

**LSEG – London Stock Exchange Group (83/28; Phase 1, 8.1% / 16.3x).**
- **Test 2:** FY3 consensus (£6.16) is already 99% of the £6.22 bar. It would move toward 88% on D&A organic growth of ≥6%, delivery of the margin step-up and capex normalising near £1.1bn.
- **Test 3:** limited by a 7/10 record, with misses in 2016 (−1.7%), 2020 (+4.7%) and 2023 (−0.8%).
- **Caveats:** the adjusted-vs-GAAP gap is 135% (Refinitiv amortisation), and LTM FCF yield is 3.7%.
- **US comparable:** TRU (85/25), a data franchise with an acquisition-driven adjusted/GAAP gap. Calibration holds LSEG at the INTU level (83/30).

**AON – Aon (83/18; Phase 1, both routes, 6.4% / 14.5x).**
- **Test 2:** sustained ≥6% organic growth, 50bp+/yr margin expansion and $2bn+/yr buybacks would lift it to ~87%. Organic growth of ≤3%, or another large leveraged deal, would cut it to ~75%.
- **Test 3:** limited by a 6/10 record; EPS never fell.
- **US comparable:** MRSH (85/25). AON is held 2 points lower for a weaker record (6/10 vs 9/10) and 2.3x leverage.

**WTW – Willis Towers Watson (83/18; Phase 2, 14.1x).**
- **Test 2:** FY3 consensus ($27.30) is already 6% above the $25.74 bar. Organic growth of ≥5% through 2027 with visible Propel savings would lift it to ~88%. If HWC organic growth turns negative because of AI, it falls to ~70%.
- **Weaknesses:** ROIC is 6.3% because of goodwill (AON 15.3%), and the margin is at its 10-year high.
- **US comparable:** MRSH (85/25).

**G24 – Scout24 (82/30; Phase 1, 6.03% / 17.4x).**
- **Test 2:** evidence of LLM licensing revenue, with traffic share stable through 2027, would move it to ≥88%.
- **Test 1 caveat:** it clears the bar by 0.03 points. The analysis estimates pre-dividend 2025 FCF at ~5.5% of market cap, rising to ~6% with 2026 EBITDA growth. A small price rise would remove it from Phase 1, and P/E does not rescue it.
- **US comparable:** GDDY (82/28), the same AI-intermediation threat and the calibration anchor. The closest business peer, CARG, scores 75/20.

**HDFC Bank (82/22; Phase 2, 12.3x).**
- **Test 2:** two quarters of NIM expansion plus ≥15% loan growth would lift it to ~86%. A broader governance problem (March 2026 controversy, external CEO from Oct-2026) or an unsecured-credit cycle would cut it to ~70%.
- **Test 3:** FY1 (FY Mar-27) consensus is +8.4% (P ≈ 0.65). The merger years FY24–25 ran ~4.9%/yr.
- **FX:** the INR has historically depreciated ~3%/yr against the USD (estimate).
- **US comparable:** JPM (65/3), the "JPM test" used in triage. The best US banks are CBSH and SFBS at 78. HDFC sits higher because adjusted EPS never fell (worst year +12.2%).

**ADYEN – Adyen (85/37), flagged: Test 1 FAIL.**
- **Test 2:** a stable take rate and an EBITDA margin above 55% delivered in 2028 would take it to ≥90%. A buyback programme would lift both tests.
- **Test 1:** on the ~5.0–5.5% clean yield, the price would need to fall ~8–17% to reach 6%, or ~27% to reach 15x.
- **US comparable:** CPAY (85/30).

**HLMA – Halma (84/33), flagged: Test 1 FAIL on both routes.**
- **Test 2:** if photonics proves durable and non-photonics organic growth holds ≥6%, it rises to ~87%.
- **Test 1:** on a ~3.4% true FCF yield, the price would need to fall ~43% to reach 6%, or ~38% to reach 15x.
- **US comparable:** OTIS (81/1), the calibration anchor. HLMA sits above it because EPS never fell.

---

## 7. Where the discards came from (approximate)

The 969 discards are the 755 NO plus 214 TOO HARD verdicts in `triage.csv`.

**Method (approximate):** each triage reason was keyword-matched to the first matching bucket, checked in this order: REIT flag, state, commodity, capital markets, holding company, rate/credit, governance, disruption, cyclical, acquisition/leverage, unproven, no specialness. Counts show one cause per name; expect ±15% misclassification per bucket. Themes overlap: 350 of 551 European Phase 1 discard reasons (64%) mention cyclicality/peak/commodity, state ownership or leverage somewhere.

| Primary reason (approx.) | P1 Europe | P1 India | P2 Europe | P2 India | Total | Typical examples |
|---|---|---|---|---|---|---|
| Commodity prices (energy, metals, chemicals, shipping, fuel) | 133 | 14 | 43 | 16 | 206 | SHEL, BP, TTE, YAR, Tata Steel, Vedanta, Hindalco |
| Cyclical peak or cyclical earnings | 126 | 4 | 33 | 3 | 166 | VOW3, FRVIA, SGO, PNR, HUSQ.B |
| Rate / credit / underwriting cycle | 15 | 0 | 97 | 22 | 134 | BNP, ISP, UCG, LLOY, HSBA, Axis Bank, Bandhan |
| Disruption / regulatory / litigation / AI | 86 | 4 | 14 | 4 | 108 | CAP, SOP, GSK, BAYN, Infosys, IEX |
| State ownership / government policy | 12 | 8 | 27 | 28 | 75 | ENGI, ORSTED, PKO, ABN, SBI, ONGC, Coal India |
| Acquisition- or leverage-driven growth | 53 | 2 | 10 | 0 | 65 | DTE, TEF, ABI, NG, RTO, OTP |
| REITs / listed property | 30 | 2 | 28 | 1 | 61 | VNA, LEG, URW, LAND, SBB.B |
| Capital-markets activity | 26 | 0 | 27 | 2 | 55 | PGHN, EQT, CVC, ICG, UBSG, DBK |
| No specialness / no route to ≥7% | 34 | 0 | 7 | 0 | 41 | VOD, TELIA, HEIA, BN, AD |
| Holding companies / NAV earnings | 9 | 0 | 11 | 1 | 21 | INVE.B, INDU.A, HAL, PRX, CDI |
| Unproven: losses, short record, turnaround | 12 | 1 | 3 | 0 | 16 | TIT, TUI1, BRBY, UCB |
| Promoter / group governance | 8 | 1 | 2 | 2 | 13 | GRF, JBS, FRAS, Jaiprakash Power |
| Unclassified | 7 | 0 | 1 | 0 | 8 | NOVN, FAGR, SRP |
| **Total** | **551** | **36** | **303** | **79** | **969** | |

Pattern by phase:
- **Phase 1 discards** are mostly commodity, cyclical and leverage cases. They resemble US v2's FCF-route discards, but there are far more of them.
- **Phase 2 discards** are mostly banks, insurers and state-controlled companies.
- **TOO HARD verdicts** concentrate in disruption (45), cyclical (43), rate/credit (35) and capital markets (26).
- **LTM basis:** of the 63 Phase 1 passes on the LTM basis, none was kept (50 NO, 13 TOO HARD).

**India.** India passes Test 1 at 22% of base against Europe's 56%, and almost everything that passes is structurally cheap.
- **Phase 1 (36 names, 0 KEEP).** 21 of the 30 NOs are state-owned refiners and E&Ps, metals and mining names, or group-controlled commodity/governance cases (review note). The two IT names have no ≥7% route:
  - Infosys: TOO HARD; consensus +1.8% / +4.2% / +5.0%.
  - Wipro: NO.
  - IEX, BLS and Firstsource fail on regulatory, government-contract or AI threats.
- **Phase 2 (81 names, 2 KEEP).** It is dominated by lenders (22 banks/insurers) and PSUs:
  - PSU banks (SBI, Bank of Baroda, PNB, Canara and others) have 10-year ROEs of roughly 0–10% and, in several cases, ~20%/yr dilution.
  - Private lenders failed the credit-cycle test (Axis, Bandhan, IndusInd, Yes Bank) or have records too short to judge (Aptus, Five-Star, Aadhar, HDB).
- **State ownership:** about 46 of 115 Indian discards (40%) cite state ownership, PSU status or government pricing. 42 of the 117 Indian passes carry the STATE_OWNED flag.
- **What never reaches the screen:** India's consumer franchises (30–60x, 1–4% FCF yields), most IT services, and ICICI and Kotak (P/E ≥15x) reach neither phase.
- **Implication:** for India, the binding constraint is the price bar, not the quality filter.

---

## 8. Data gaps and low-confidence names

**Data issues** (sources: `data/stage1_summary.json`, `data/stage1_universe.csv`, `assumptions.md`)

- **FCF basis.**
  - 63 Phase 1 passes (Europe 53, India 10) rest on LTM FCF, which can capture one-off cash (I18). All were discarded.
  - Among the 536 NTM-basis passes, 3 of 12 KEEPs failed reconciliation. HLMA's failure is a FactSet per-share consensus defect that may affect other names; it was not checked beyond the KEEPs.
- **Consensus coverage.** 22 of 986 passes have no NTM/FY1 EPS consensus (Europe 19, India 3; e.g. Etex, CDI, Clariane, Odet, Tabak). All are Phase 1 on FCF, so the P/E route and the growth tests could not be checked. All were discarded (20 NO, 2 TOO HARD).
- **Missing and extreme values.**
  - 57 candidates are MISSING: 24 have no price (acquired or delisted lines, e.g. Ashtead's old line, Beazley, JDE Peet's, WNS); the rest have no NTM earnings and no eligible FCF.
  - 24 passes with extreme values (FCF yield >25% or P/E <4x) were tagged CHECK (I17); all were discarded (22 NO, 2 TOO HARD).
- **REITs and property.** 74 names were flagged, and 56 passed (Europe 55, India 1). 50 of the 56 are on P/FFO; 6 fall back to EPS, which includes revaluations. All 56 were discarded.
- **FX.**
  - Valuation uses FactSet-converted USD, with small rate-timing differences between price (19-Oct), estimates (20-Oct) and fundamentals.
  - Analyses convert FMP market caps at FRED 16-Oct rates (1.123 USD/EUR, 1.333 USD/GBP), while some text uses ~1.16 USD/EUR (G24, estimate). No result depends on this.
  - Growth is in reporting currency, so a USD investor also carries translation risk (WKL ~60% USD revenue; HDFC INR ~3%/yr depreciation).
- **Indian March year-ends.** FactSet labels FY Mar-2026 as "2025", so Indian Test 2/3 windows run one label-year later (HDFC Bank's Test 2 is FY32). HDFC Bank's adjusted EPS is missing for FY24 (merger year), and its EPS is adjusted for the Aug-2025 1:1 bonus.
- **Dual listings and non-home HQ names.**
  - 92 passes have a primary listing outside their HQ country. Four are among the 17 KEEPs: AON, TEL and WTW (NYSE, USD reporters) and BCG (Lithuania HQ, London listing).
  - CB (Swiss HQ, NYSE) was demoted in review.
  - These names are compared directly with US peers but were never in the US universe.
- **Low float and illiquid lines.** 101 candidates are listed subsidiaries or Euronext Brussels Expert Market lines (I5); 49 of them passed. One is a KEEP: IONOS, majority-owned by United Internet.
- **Size.** BCG's market cap is $0.95bn on FMP (19-Oct-2026), below the $1bn line, although it passed the FactSet `FF_MKT_VAL` screen.
- **Adjusted vs GAAP EPS (5-year average gap):** LSEG 135%, AON 33%, BCG 24%, G24 21%, WTW 17%, HLMA 16%. Tests 2 and 3 are judged on adjusted consensus.

**Low-confidence analyses.** BCG is rated Low (3-year standalone record, smallest name). All the others are Medium. No low-confidence name is within 5 points of a threshold.

**Top 3 data issues**

1. **The Phase 1 FCF yield is the least reliable input, and it decides membership.**
   - 3 of 12 Phase 1 KEEPs failed the FCF check.
   - G24 (6.03%) and BCG (6.01%) clear the bar by less than 0.05 points, and LSEG's NTM yield (8.1%) is more than double its LTM yield (3.7%).
   - Only WKL, AUTO and AON would pass Test 1 on P/E alone.
2. **Currency mismatch between price and growth.** Tests 2 and 3 are judged in reporting currency, while valuation is in USD. FX caused WKL's two misses, and it is a named threat for LSEG, HLMA and ADYEN. For INR names, USD-equivalent growth runs ~3 points/yr lower (estimate).
3. **Universe and coverage gaps.**
   - 57 names are missing, and 22 passes have no EPS consensus.
   - 101 subsidiary or Expert Market lines need manual handling.
   - Indian March year-ends and HDFC Bank's missing FY24 make the Indian EPS series less continuous than the European ones.

---

## 9. Files

All files are in `/home/user/financial-services-plugins/buffett_test/intl/`.

- **`Buffett_Test_Data_Europe_India.xlsx`:** four tabs.
  - **Universe:** 1,066 names, i.e. the 986 PASS with phase, FCF yield and basis, NTM P/E, price and region, plus 80 near-misses.
  - **Triage:** 986 final verdicts, 17 KEEP / 214 TOO HARD / 755 NO.
  - **Analysis:** the 17 Stage 4 results.
  - **Sources:** source and as-of date for each data item.
- **`triage.csv`:** final verdicts with phase, verdict, reason and `review_override`. Supporting files: `triage/batch_01–50.csv`, `triage/review_notes_p1.md`, `triage/review_notes_p2.md`, `triage/review_overrides_p1.csv`, `triage/review_overrides_p2.csv`.
- **`analyses/`:** 17 write-ups (`<KEY>.md`), `_results_final.jsonl` (after calibration) and `_calibration.md`.
- **`data/`:** `stage1_universe.csv` (1,735 candidates), `stage1_summary.json`, `candidates.csv`, `entity_info.csv`, `phase1_passes.txt`, `phase2_passes.txt`, and per-company `<KEY>.json` / `_summary.json`.
- **`assumptions.md`:** I1–I20. **`stage23_prompt.md`:** the Europe/India triage lenses. **`approach_summary.md`:** the PM's specialness test.
- **US reference:** `../Buffett_Test_Report.md` and `../Buffett_Test_Report_v2.md` (unchanged method); `../analyses/_results_final_v2.jsonl` (US comparables).
