# Buffett-style screen of US equities over $1bn: final report

**As of 19-Oct-2026.** This is a screen, not a recommendation. It contains no buy/sell views or position sizes.

**Sources and conventions used throughout**
- **NTM P/E:** FactSet close on 19-Oct-2026 divided by the FactSet NTM consensus mean EPS on 19-Oct-2026.
- **Market cap:** FactSet GlobalPrices market value, 16-Oct-2026, which was the latest FactSet print when the data were pulled.
- **EPS history:** FactSet adjusted ("street") actuals for FY2015–FY2025.
- **Consensus growth (FY1, FY2, FY3):** FactSet consensus, 19-Oct-2026.
- **P(Test 2) and P(Test 3):** these are analyst estimates, not data. They come from `analyses/<TICKER>.md` after calibration (`analyses/_results_final.jsonl`). Treat them as roughly ±5–10 points.
- All percentages are rounded to whole numbers.

---

## 1. Bottom line

- **Funnel:** the FactSet screener returned 826 US-HQ names over $1bn. Of these, 780 pass Test 1 (NTM P/E between 0 and 15x). Triage kept 37, and 5 borderline names were added, giving 42 full analyses.
- **No company passes all three tests.** All 42 pass Test 1 only. None reaches 90% on Test 2 or 50% on Test 3.
- **Three near-misses,** all 85% on Test 2:
  - **ADBE:** P(Test 2) 85%, P(Test 3) 37%
  - **CPAY:** 85% and 30%
  - **TRU:** 85% and 25%

  Each is 5 points short on Test 2 but 13–25 points short on Test 3.
- **Why Test 2 fails:** a stock below 15x nearly always carries a specific, nameable threat, and one credible threat caps the probability at about 85%.
  - The 10 highest-scoring names all have one. Four face AI substitution (ADBE, INTU, GDDY, BLKB). TRU faces regulation and the credit cycle. CPAY faces fuel, FX and dependence on acquisitions. TMUS faces wireless price competition.
- **Why Test 3 fails:** the test demands ≥7% EPS growth in every one of five years, which almost certainly includes a recession year.
  - Of the 515 Test 1 passes with a full 10-year record, only ADBE grew EPS ≥7% in every year (FactSet).
  - 39 of the 42 analysed names had at least one year of falling EPS in their available history (up to 10 years).
- **Uncertainty:** the 5-point Test 2 shortfall for the near-misses is within estimation error. The Test 3 shortfall is not.

---

## 2. Method and assumptions

**The three tests**

| Test | Pass condition |
|---|---|
| 1. Price | 0 < NTM P/E < 15 (REITs on NTM FFO where FactSet has FFO consensus). 15–16x is recorded as a near-miss. |
| 2. Earnings resilience | P(EPS in FY1+5 ≥ 1.30 × FY1 consensus) ≥ 90%. This needs only about 5.4%/yr. |
| 3. Consistency | P(EPS grows ≥7% in every one of the next 5 years, including a recession year) ≥ 50%. |

**Data sources.** All data are from FactSet, pulled 19-Oct-2026:
- CompanyScreener for the universe;
- GlobalPrices for prices and market value;
- EstimatesConsensus for NTM and FY0–FY3 consensus and adjusted EPS actuals;
- Fundamentals for FY2015–FY2025, with an audit formula stored for each value;
- EntityReference for business descriptions and RBICS;
- UnstructuredContent for transcripts and news (at most 2 queries per company).

FMP was a backup only, used for 3 market caps. The PM's "specialness" test comes from the Notion approach page and is summarised in `approach_summary.md`.

**Triage.**
- 39 batch workers gave each of the 780 Test 1 passes one verdict:
  - **KEEP:** forecastable 5–10 years out, durable economics, and a plausible route to ≥7% EPS growth.
  - **TOO HARD:** cannot be forecast with confidence.
  - **NO:** fails a test, or is a bargain with nothing special about it.
- A name was discarded for any of the following:
  - earnings set by commodity prices, rate or credit cycles, or capital markets;
  - EPS near a cyclical peak;
  - a credible threat within 5 years (technology, regulatory, litigation or single customer);
  - growth bought through acquisitions or leverage;
  - a balance sheet that could not survive a recession;
  - a business too complex to forecast.
- No sector was excluded wholesale.
- A single reviewer then checked every KEEP and TOO HARD side by side. This produced 24 overrides: 23 demotions, plus the promotion of ADBE for consistency with INTU.

**Analysis and calibration.** Each of the 42 write-ups (`analyses/<TICKER>.md`) covers:
- a 10-year EPS decomposition;
- a normal-year forward driver stack measured against 7%;
- why the market doubts the stock;
- a list of threats with probabilities, which gives P(Test 2);
- a year-by-year probability chain, which gives P(Test 3);
- earnings quality.

The workers used shared anchors:
- one credible threat puts Test 2 at about 70–85%;
- a wide-moat compounder scores about 88–95% on Test 2;
- a typical compounder scores 20–40% on Test 3.

A calibration pass compared peers and changed 9 Test 2 probabilities. None crossed a threshold. GEHC fell from 85% to 80%, which removed it from the near-miss list.

**Key assumptions** (the full A1–A22 list is in `assumptions.md`)
- **FY1 (A7):** the first unreported fiscal year.
- **EPS basis (A8):** FactSet street (adjusted) actuals are used where at least 6 years exist, GAAP otherwise. Tests 2 and 3 are judged on the adjusted consensus basis.
- **FCF (A15):** operating cash flow − capex. FactSet's FF_FREE_CF is net of dividends.
- **Banks and insurers (A11):** judged on EPS, ROE and credit or underwriting quality.
- **Extreme P/Es (A14):** FMCC 0.8x, FNMA 1.3x and ALIT 1.7x were kept as reported and judged on the business.
- **Discard rate (A20):** 95% of names were discarded, stricter than the 85–90% guide. This was accepted rather than loosened.
- **Borderline names (A21):** FFIN, CFR, BANF, LII and DHI were analysed as "borderline" to widen the watchlist.

---

## 3. Funnel

| Stage | Count | Source |
|---|---|---|
| FactSet screen (US HQ, primary listing, mkt cap >$1bn, FactSet P/E 0–15) | 826 | FactSet CompanyScreener, 19-Oct-2026 |
| Test 1 PASS (recomputed NTM P/E 0–15x) | 780 | FactSet close and NTM consensus, 19-Oct-2026 |
| Test 1 near-miss (15–16x), not analysed | 33 | as above |
| Test 1 fail (≥16x or negative/blank NTM EPS) | 13 | as above |
| Triage, first pass: KEEP / TOO HARD / NO | 59 / 153 / 568 | `triage/batch_*.csv` |
| Triage, after consistency review: KEEP / TOO HARD / NO | 37 / 175 / 568 | `triage.csv` |
| Stage 4 analyses (37 KEEP + 5 borderline) | 42 | `analyses/` |
| Pass Test 2 (P ≥ 90%) | 0 | `_results_final.jsonl` |
| Pass Test 3 (P ≥ 50%) | 0 | `_results_final.jsonl` |
| **Pass all three tests** | **0** | |

---

## 4. Passes all three tests

**None.**

All 42 analysed names pass Test 1 and fail Tests 2 and 3.

- **Test 2:** the highest probability is 85% (ADBE, CPAY, TRU), against a 90% bar.
- **Test 3:** the highest is 37% (ADBE), against a 50% bar.
- **The pattern:** businesses with no credible five-year threat score 90% or more on Test 2, but they are rarely priced below 15x. Every name priced below 15x that triage kept carries at least one identifiable risk the market is discounting, and the analyses found that risk real in each case.
- **Test 3 is the binding constraint.** Even the upside cases written into the analyses take no name above about 45% (ADBE). So the best outcome currently plausible for any name is 2 of 3 tests.

### Closest to passing (top 10 analysed names, ranked by P(Test 2), then NTM P/E)

| Ticker | Name | NTM P/E | Mkt cap $bn | 10y EPS CAGR % | FY1 / FY2 / FY3 cons. growth % | P(Test 2) % | P(Test 3) % | Key uncertainty |
|---|---|---|---|---|---|---|---|---|
| ADBE | Adobe | 9.0 | 95.4 | 26 | 17 / 13 / 13 | 85 | 37 | Does genAI expand Adobe's market or deflate creative seats? Net new ARR fell 38% y/y in Q3 FY26, and there is a new CEO. |
| CPAY | Corpay | 13.1 | 26.3 | 13 | 28 / 15 / 18 | 85 | 30 | How much of the 20%+ EPS algorithm is organic rather than acquisitions, fuel and FX? |
| TRU | TransUnion | 13.7 | 14.2 | 15 | 12 / 13 / 15 | 85 | 25 | Do US mortgage and credit-score economics stay with the bureaus through a credit slowdown? |
| GL | Globe Life | 10.3 | 13.0 | 13 | 8 / 5 / 9 | 83 | 8 | Can American Income grow agents without renewed regulatory attack on its sales practices? |
| PRI | Primerica | 10.5 | 8.7 | 20 | 10 / 8 / 10 | 83 | 20 | Does sales-force recruiting recover after the 2027 convention? |
| INTU | Intuit | 13.8 | 86.9 | 16 | 36 / 13 / 13 | 83 | 30 | Is AI a feature Intuit sells or a substitute for DIY tax, given current share losses? |
| TMUS | T-Mobile US | 11.7 | 170.7 | 28 | 12 / 28 / 20 | 82 | 27 | Does wireless pricing stay rational as cable MVNOs and satellite direct-to-device enter? |
| GDDY | GoDaddy | 12.2 | 13.4 | n/a | 19 / 23 / 12 | 82 | 28 | Do AI site-builders erode new-domain and A&C demand? |
| BLKB | Blackbaud | 9.1 | 2.3 | 12 | 18 / 14 / n/a | 80 | 18 | Does AI turn the nonprofit data moat into upsell or into churn? |
| GEHC | GE HealthCare | 13.1 | 31.4 | n/a | 7 / 10 / 11 | 80 | 18 | Can 4–5% organic growth become about 10% EPS growth via margin, despite tariffs and China? |

Notes on the table:
- **10y EPS CAGR:** FactSet adjusted actuals for FY2015–FY2025.
  - GDDY: n/a, because its 7-year record is distorted by a FY2023 tax benefit.
  - GEHC: n/a, because it was spun off in Jan-2023. GAAP EPS grew 5% a year over 2019–25.
- **INTU:** FY1 growth of 36% is a definition break, not a real increase. Stock-based compensation is now included in non-GAAP EPS, so FY2026 actuals are not like-for-like (`analyses/INTU.md`).
- **BLKB:** has no FY3 consensus.

---

## 5. Near-misses: watchlist for pre-dislocation diligence

All three already pass Test 1 comfortably, so price is not what holds them back. Tests 2 and 3 are about earnings. A lower share price helps only indirectly, by raising the buyback yield that feeds future EPS growth.

**ADBE (Adobe)**

*Business.* Adobe sells:
- Creative Cloud (creative software, including the Firefly AI tools);
- Document Cloud (Acrobat/PDF);
- Experience Cloud (marketing software).

About 95% of revenue is recurring subscription (company disclosure, approximate).

*Why it trades at 9.0x.* The market prices Adobe as a possible genAI casualty:
- Canva, Figma and model-native tools are taking the low end of the creative market.
- AI language models could erode the PDF franchise.
- Net new ARR fell 38% y/y in Q3 FY26, and RPO/cRPO fell sequentially (FactSet StreetAccount, Sep-2026).
- The CEO has changed.

*What the analysis found.*
- **Track record:** among the 515 Test 1 passes with a full 10-year record, Adobe is the only one with 10 out of 10 years of ≥7% EPS growth. Its worst year was FY2022 at +10%, its 10-year EPS CAGR is 26%, and its net debt is only $53m, about 0.0x EBITDA (FactSet).
- **Test 2 bar:** the bar is $31.82 (1.30 × FY1 consensus of $24.48). FY3 consensus of $31.42 is already almost there (FactSet consensus, 19-Oct-2026). With shares shrinking about 5% a year, Adobe passes Test 2 as long as adjusted net income does not fall by FY2031.
- **Test 2 failure risk** is about 15%. The main source is genAI commoditisation, which the analysis gives a 12% probability, with net income falling 15–25%.
- **Test 3:** the chain 0.98 × 0.85 × 0.78 × 0.76 × 0.75 gives 37%.

*What would need to change.* Two pieces of evidence would lift Test 2 to about 90%:
- net new ARR stabilises or grows in FY2027;
- operating margin stays around 36% or better under the new CEO.

Test 3 would still reach only about 45%. To pass it, Adobe would need to show it can grow EPS ≥7% in a weak year. That rests on buybacks contributing about 7 points a year (at a roughly 10% FCF yield) while organic net income holds flat. Adobe has never been tested in this way with its current growth rate.

**CPAY (Corpay)**

*Business.* Corpay has three main lines:
- corporate payments (accounts-payable automation and cross-border FX);
- fleet fuel cards;
- lodging payments.

It is run by its founder, Ron Clarke, who combines buybacks with serial acquisitions.

*Why it trades at 13.1x.* The market doubts the quality of the growth:
- fleet-card fee practices (FTC litigation filed in 2019);
- sensitivity to fuel prices and FX;
- slow long-run erosion of fuel-card volumes as fleets move to electric vehicles;
- dependence on acquisitions.

FY2026 consensus of +28% is flattered by acquisitions, fuel prices and a weak dollar (CFO, May-2026, per FactSet transcript).

*What the analysis found.*
- **Organic growth** has been 10–11% for five straight quarters.
- **Test 2 bar:** $35.64. FY3 consensus of $37.09 is already above it (FactSet consensus, 19-Oct-2026).
- **Test 2 failure risk** is about 15%. The main source is a recession plus a fuel-price collapse in the final year.
- **Test 3:** EPS grew ≥7% in 8 of the last 10 years. The two misses were 2020 (−6%) and 2023 (+5%), so P(Test 3) is 30%.

*What would need to change.*
- **Test 2:** two more years of ≥10% organic growth with FX volatility normalising would lift it to 88–90%.
- **Test 3:** Corpay would need to show ≥7% EPS growth through a recession or a fuel-price drop without leaning on acquisitions. Only a downturn can prove that.

*Earnings-quality caveat.* Adjusted EPS was 42% above GAAP in FY2025. Gross debt/EBITDA is 4.0x, compared with 0.45x on a net basis, because the company holds customer deposits (FactSet Fundamentals FY2025).

**TRU (TransUnion)**

*Business.* TransUnion is one of three US credit bureaus. It also has growing fraud, marketing-analytics and India/international businesses.

*Why it trades at 13.7x.*
- Lending volumes are cyclical: adjusted EPS fell 7% in 2023.
- Regulators are pressuring mortgage credit-score and tri-merge economics, and FICO is pushing direct licensing.
- Data-services stocks were de-rated in 2026 on fears of AI commoditisation.
- Net debt/EBITDA is 2.9x (FactSet FY2025).

*What the analysis found.*
- **Test 2 bar:** $6.28. FY3 consensus of $6.31 is already at it (FactSet consensus, 19-Oct-2026).
- **Test 2 failure risk** is about 15%. It is spread across five threats; the largest are a late-window credit recession (about 5 points) and a regulatory hit to mortgage and score pricing (about 3 points).
- **Test 3:** EPS growth missed 7% in both 2022 (+5%) and 2023 (−7%) when the rate shock hit originations. The analysis puts the chance of avoiding a credit shock over five years at about 50%, which gives P(Test 3) of 25%.

*What would need to change.* Test 2 would rise to 90% or more with:
- clear evidence that mortgage and score economics stay with the bureaus;
- organic growth of ≥7%;
- EBIT margin rising from 20.1% back toward its 2017 peak of 24.0% (FactSet);
- leverage below 2.5x, with buybacks resuming.

Test 3 needs non-mortgage volumes to grow through a credit downturn. In 2023 they did not.

*Earnings-quality caveat.* TRU has the biggest gap of the three: adjusted EPS averaged 122% above GAAP over 5 years. The 10-year average ROIC is 4.5%.

### Next tier: P(Test 2) of 80–84% after calibration

The "upside case" column is the Test 2 probability each analysis says the named evidence would produce.

| Ticker | P(Test 2) % | P(Test 3) % | Single thing that would need to change | Upside case P(Test 2) |
|---|---|---|---|---|
| GL | 83 | 8 | Two years of mid-single-digit agent and sales growth at American Income, plus closure of the remaining EEOC matter. The SEC and DOJ closed their probes in Jul-2025 (FactSet news). | not quantified |
| PRI | 83 | 20 | Life-licensed sales force returns to 3–5% growth after the 2027 convention. | ~88% |
| INTU | 83 | 30 | Two filing seasons of stable TurboTax DIY share. | 88–90% |
| TMUS | 82 | 27 | Churn stabilises and ARPA grows ≥3% through 2027. | ~88% |
| GDDY | 82 | 28 | A&C bookings back to double-digit, with Airo driving new-customer growth. | ~88% |
| BLKB | 80 | 18 | Gross dollar retention reaches 92%, plus AI revenue in 2027. | 85–88% |
| GEHC | 80 | 18 | Adjusted EBIT margin of 16%+ by FY2027, with mid-single-digit organic growth and China stable. | >90% (analysis, before calibration cut it to 80%) |

No upside case lifts any of these names to 50% on Test 3. GL's FY2 consensus of +5% is already below 7%.

**Test 1 near-misses: NTM P/E of 15–16x, not analysed (33)**

MORN, DPZ, CCC, SEIC, NNI, BX, PHAT, STX, DOCU, WAY, NXT, MZTI, AMKR, WERN, OPCH, URGN, AAMI, VECO, EXEL, RUSHA, DELL, WDAY, XYZ, ZM, NOV, NVDA, HOG, GNRC, AIR, INCY, PFGC, EXTR, DIOD.

These are ordered by NTM P/E (FactSet, 19-Oct-2026). They were neither triaged nor analysed. A move of up to about 6% in price or NTM EPS would bring them inside Test 1.

---

## 6. Full results: all 42 analysed names

Ranked by P(Test 2), then NTM P/E.
- **Tests passed:** all 42 pass Test 1 only.
- **Specialness:** "Good–track" means "good business, track for a dislocation"; "Special" means "super special" in the PM's test.
- **Calibration change:** shows the before→after Test 2 probability where it moved.

| Ticker | Triage | NTM P/E | P(Test 2) % | P(Test 3) % | Tests passed | Confidence | Specialness | Calibration change |
|---|---|---|---|---|---|---|---|---|
| ADBE | KEEP | 9.0 | 85 | 37 | 1/3 | M | Good–track | N |
| CPAY | KEEP | 13.1 | 85 | 30 | 1/3 | M | Good–track | N |
| TRU | KEEP | 13.7 | 85 | 25 | 1/3 | M | Good–track | N |
| GL | KEEP | 10.3 | 83 | 8 | 1/3 | M | Good–track | N |
| PRI | KEEP | 10.5 | 83 | 20 | 1/3 | M | Special | N |
| INTU | KEEP | 13.8 | 83 | 30 | 1/3 | M | Special | Y (80→83) |
| TMUS | KEEP | 11.7 | 82 | 27 | 1/3 | M | Special | N |
| GDDY | KEEP | 12.2 | 82 | 28 | 1/3 | M | Good–track | N |
| BLKB | KEEP | 9.1 | 80 | 18 | 1/3 | M | Good–track | N |
| GEHC | KEEP | 13.1 | 80 | 18 | 1/3 | M | Good–track | Y (85→80) |
| AGM | KEEP | 8.8 | 78 | 14 | 1/3 | L | Good–track | N |
| PBH | KEEP | 10.2 | 78 | 4 | 1/3 | M | Good–track (borderline not special) | N |
| SFBS | KEEP | 11.2 | 78 | 17 | 1/3 | M | Good–track | N |
| CBSH | KEEP | 12.1 | 78 | 3 | 1/3 | M | Good–track | N |
| BKNG | KEEP | 13.6 | 78 | 25 | 1/3 | M | Special | N |
| ATMU | KEEP | 13.8 | 78 | 12 | 1/3 | M | Good–track | N |
| EWBC | KEEP | 11.0 | 76 | 8 | 1/3 | M | Good–track | N |
| BFAM | KEEP | 12.1 | 76 | 27 | 1/3 | M | Good–track | N |
| CARG | KEEP | 10.5 | 75 | 20 | 1/3 | M | Good–track | N |
| DECK | KEEP | 10.9 | 75 | 15 | 1/3 | M | Good–track | N |
| BRC | KEEP | 12.2 | 75 | 18 | 1/3 | L | Good–track | N |
| HAYW | KEEP | 12.6 | 75 | 10 | 1/3 | L | Good–track | Y (72→75) |
| CFR | Borderline | 12.9 | 75 | 4 | 1/3 | M | Good–track | Y (72→75) |
| HII | KEEP | 13.1 | 75 | 10 | 1/3 | M | Good–track | N |
| DORM | KEEP | 13.3 | 75 | 1 | 1/3 | M | Good–track | N |
| FCN | KEEP | 14.0 | 75 | 2 | 1/3 | M | Good–track | N |
| POOL | KEEP | 14.6 | 75 | 2 | 1/3 | M | Good–track | N |
| PLNT | KEEP | 14.8 | 75 | 12 | 1/3 | M | Good–track | N |
| CSL | KEEP | 14.2 | 74 | 12 | 1/3 | M | Good–track | Y (70→74) |
| BOOT | KEEP | 12.4 | 73 | 16 | 1/3 | M | Good–track | N |
| COO | KEEP | 12.4 | 73 | 5 | 1/3 | M | Good–track | N |
| SFM | KEEP | 10.9 | 72 | 2 | 1/3 | M | Good–track | Y (65→72) |
| LII | Borderline | 14.1 | 72 | 3 | 1/3 | M | Good–track | N |
| ORI | KEEP | 12.2 | 70 | 2 | 1/3 | M | Good–track | N |
| ZTS | KEEP | 12.5 | 70 | 1 | 1/3 | M | Special | N |
| AOS | KEEP | 14.8 | 70 | 1 | 1/3 | M | Good–track | Y (68→70) |
| BSX | KEEP | 13.4 | 68 | 3 | 1/3 | M | Good–track | Y (65→68) |
| FFIN | Borderline | 14.2 | 67 | 3 | 1/3 | M | Good–track | N |
| JPM | KEEP | 13.1 | 65 | 3 | 1/3 | M | Special | Y (62→65) |
| DHI | Borderline | 11.9 | 62 | 1 | 1/3 | M | Good–track | N |
| BANF | Borderline | 13.5 | 40 | 2 | 1/3 | L | Good–track | N |
| PGR | KEEP | 13.2 | 37 | 1 | 1/3 | M | Special | N |

Summary of the distribution:
- **Test 2:** median 75%; 10 of 42 names are at 80% or above.
- **Test 3:** 8 names are at 25% or above, and 22 are at 10% or below.
- **Specialness:** 7 names are rated Special (PRI, INTU, TMUS, BKNG, ZTS, JPM, PGR). None of the 7 scores above 83% on Test 2.
- **Banks and insurers:** none scores above 20% on Test 3. PGR is the lowest name overall on Test 2 (37%), because FY2 consensus is −12% as its combined ratio normalises.

---

## 7. Where the discards came from (approximate)

The 743 discards are the 568 NO plus 175 TOO HARD verdicts.

**How the buckets were built.** Each discard was put into one bucket by keyword-matching its triage reason (and any reviewer override) in Python. Buckets were checked in the order listed below, and a name went into the first bucket it matched.
- Many reasons cite several causes. For example, "peak margin" often appears alongside "ND/EBITDA 4x". The counts show the dominant cause, not every cause.
- Expect misclassification of about ±10–15% per bucket.

| Primary reason (approx.) | NO | TOO HARD | Total | Typical examples |
|---|---|---|---|---|
| Rate / credit / underwriting cycle (banks, mortgage, consumer lenders, P&C/life, homebuilders) | 144 | 58 | 202 | KEY, FULT, PHM, SIGI, UPBD |
| Disruption / regulatory / litigation threat (AI, GLP-1, reimbursement, patents, wildfire, PBM reform) | 91 | 47 | 138 | UHS, HRB, HE, BMY, CI |
| Commodity prices (energy, metals, chemicals, agriculture, paper) | 112 | 7 | 119 | DVN, HAL, STLD, NEM, CBT |
| Capital-markets activity (brokers, asset/wealth managers, BDCs) | 53 | 15 | 68 | MS, SCHW, BEN, RJF, OBDC |
| Cyclical peak | 56 | 11 | 67 | TEX, CRUS, WGO, AGCO |
| No specialness / no route to ≥7% growth (utilities, staples, telecoms) | 54 | 0 | 54 | MKC, CLX, VZ, AVA |
| Too complex / mid-transformation | 13 | 30 | 43 | FNMA, DIS (spin), ALGN, FDX |
| Acquisition / leverage-driven growth | 29 | 5 | 34 | HSIC, NWL, XRAY, TFX |
| Balance sheet | 14 | 1 | 15 | AES, UGI, SIRI, BBWI |
| Unclassified | 2 | 1 | 3 | GIII, RPD, ARLO |
| **Total** | **568** | **175** | **743** | |

Source: `triage.csv`, final verdicts; the grouping is approximate.

Balance sheet and acquisition-driven growth rank low as *primary* reasons, but they appear as secondary reasons in many more rows.

---

## 8. Data gaps and low-confidence names

**Data issues** (sources: `data/data_gaps.json`, `assumptions.md`)

- **Market cap timeouts:**
  - FactSet's GlobalPrices market value calls repeatedly timed out (HTTP 408). They failed for all 20 names in batch 09 and were dropped from the per-batch pulls from batch 19 onward (A17–A18).
  - 577 names were backfilled centrally. The final source is FactSet for 777 of the 780 names, dated 16-Oct-2026 for nearly all of them. FMP was used for DEC and OTF (FactSet returned null) and for ALM (FactSet returned CAD) (A22).
  - Several write-ups quote FMP market caps for 19-Oct-2026, which differ from FactSet by up to 4%. No test result depends on this.
- **FCF definition:** FactSet's FF_FREE_CF is net of dividends. Statistics were recomputed as operating cash flow − capex (A15).
  - One residual: the snapshot table in `analyses/TRU.md` still shows FF_FREE_CF. Its driver stack uses pre-dividend FCF of $662m.
- **Adjusted vs GAAP EPS:** adjusted EPS differs from GAAP by more than 15% for 342 of the 780 names (the ADJ_GAAP_GAP flag).
  - Among the 42 analysed, 15 exceed 15% on a 5-year average, plus BLKB on FY2025. Examples: TRU 122%, BSX 134%, CARG 284%, BFAM 73%, COO 62%.
- **Thin analyst coverage:** 38 names have fewer than 3 FY1 estimates, and 28 carry a LOW_COVERAGE flag at triage.
  - Among the analysed names: BANF (1–3 analysts), AGM (3), BRC (2).
- **Short EPS history:** 59 names have fewer than 8 years of EPS history.
  - Among the analysed names: ATMU (5 years, carve-out), GEHC (spun Jan-2023), HAYW (since 2019), GDDY (7 years), CARG (8 years).
  - 265 of the 780 lack a full 10-year growth record.
- **REITs:** FactSet has FFO consensus for only 5 of the 17 REITs. The 12 mortgage REITs use EPS, which is their usual metric anyway. All 17 were NO at triage.
- **Foreign-listed US-HQ names:** six names (1316-HK, 1910-HK, 2507-HK, RWC-AU, GQG-AU, LNW-AU).
  - The three Hong Kong listings use the 16-Oct-2026 close.
  - RWC-AU failed Test 1. The other five were discarded at triage.
- **Other gaps:**
  - 7 names had a DATA_GAP flag (FCNCA, WGO, NLY, DX, FOR, ANAB, NIQ); all were discarded.
  - Segment revenue was not pulled (A10).
  - Qualitative evidence was capped at 2 FactSet queries per company.
- **FY1 consensus distortions:** these raise or lower the Test 2 bar (1.30 × FY1).
  - INTU: change in how SBC is treated.
  - JPM: a ~$5.6bn Visa/equity gain in Q2-26.
  - AGM: ~$30m of investment tax credits.
  - CPAY: FY1 flattered by acquisitions, fuel and FX.

**Low-confidence analyses**

| Ticker | P(Test 2) % | P(Test 3) % | Why confidence is low |
|---|---|---|---|
| BANF | 40 | 2 | Only 1–3 analysts in consensus. FY2/FY3 growth is 4% and 2%. |
| AGM | 78 | 14 | 3 analysts. The EPS decomposition is estimated. FY1 is inflated by investment tax credits. Leverage is about 30x (structural, but it needs a capital review). |
| HAYW | 75 | 10 | History only since 2019. Adjusted EPS fell 53% in 2023, and the 10-year CAGR cannot be computed. |
| BRC | 75 | 18 | The transformational Honeywell PSS acquisition ($1.4bn). 2 analysts. |

None of the four is within 5 points of a threshold, so the low confidence does not change the headline result.

**Top 3 data issues**

1. **Adjusted vs GAAP EPS gap.** It affects 342 of 780 names, including all three near-misses (ADBE 34%, CPAY 34%, TRU 122% on 5-year averages). Tests 2 and 3 are judged on adjusted consensus EPS. If GAAP were the basis, TRU and CPAY in particular would look materially worse.
2. **FY1 consensus is not always a clean base.** One-off gains (JPM, AGM), definition changes (INTU) and acquisition, fuel or FX effects (CPAY) move the 1.30 × FY1 bar. The analyses adjusted for these by hand, as estimates.
3. **Thin coverage and short histories.** 38 names have fewer than 3 FY1 estimates and 59 have fewer than 8 years of EPS. Four analysed names, including GDDY and GEHC from the top 10, have no 10-year EPS CAGR. That weakens the Test 3 cross-check against history.

---

## 9. Files

All files are in `/home/user/financial-services-plugins/buffett_test/`.

- **`Buffett_Test_Data.xlsx`:** the data workbook, with these tabs:
  - **Universe:** 813 names with Test 1 result, NTM P/E, price, NTM EPS/FFO, market cap and RBICS.
  - **Triage:** 780 verdicts, reasons and reviewer overrides.
  - **Analysis:** the 42 Stage 4 results.
  - **Sources:** the source and as-of date for each data item.
- **`triage.csv`:** the final Stage 3 verdicts (`verdict`, `reason`, `review_override`, `flags`). Supporting files are `triage/batch_*.csv`, `triage/review_overrides.csv` and `triage/review_notes.md`.
- **`analyses/`:** 42 company write-ups (`<TICKER>.md`), plus `_results_final.jsonl` (after calibration), `_results.jsonl` (before calibration) and `_calibration.md`.
- **`data/`:** the FactSet extract for each company (`<TICKER>.json`, with an audit formula per value), `<TICKER>_summary.json` (consensus), `stage1_universe.csv`, `stage1_summary.json` and `data_gaps.json`.
- **`assumptions.md`:** the full assumptions log, A1–A22.
- **`approach_summary.md`:** the PM's "specialness" test, as applied.
- **Method:** `scripts/stage23_prompt.md` (data pull and triage) and `scripts/stage4_prompt.md` (driver analysis).
