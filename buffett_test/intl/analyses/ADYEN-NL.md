# Adyen NV (ADYEN-NL) — Buffett driver analysis
As-of 2026-10-19 | Europe / Netherlands | Test 1: Phase 1 (FCF yield ≥6%) — **FCF CHECK FAIL: clean FCF yield ≈5.0–5.5%, not ≥6%. P/E of 20.5x does not rescue it, so Test 1 FAILS.** | FCF yield 6.0% NTM consensus (LTM 3.1%) | NTM P/E 20.5x | Mkt cap $29.4bn (FMP, 19-Oct-2026) | RBICS Specialty Finance / Consumer Finance Services | Triage: KEEP | Confidence: Medium
Valuation figures come from data/stage1_universe.csv (FactSet NTMA consensus and FactSet close, 19-Oct-2026). EPS figures are in EUR.
Specialness (PM Part 1 test): **Special**. Several attributes apply:
- **Excellent founder management:** co-founder Pieter van der Does is still co-CEO. Growth comes organically on a single in-house stack, with no M&A until 2026.
- **Compelling customer value proposition:** one global platform for online and in-store payments, with own banking licences.
- **Secular growth:** payment digitisation, unified commerce and embedded finance.
- **Widening scale moat:** a decade of 20%+ volume growth.

## Snapshot table
| FY (Dec) | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| Adj EPS € (FactSet actuals) | 4.30 | 6.67 | 8.53 | 15.29 | 18.16 | 22.55 | 29.40 | 33.42 |
| Revenue €m (FactSet FF; gross basis to 2022, then net — series break) | 1,653 | 2,657 | 3,641 | 5,995 | 8,936 | 1,863 | 2,260 | 2,673 |
| EBIT margin % (on FF revenue) | 11.0 | 10.1 | 10.6 | 10.3 | 7.7 | 38.9 | 39.4 | 41.6 |
| EBITDA €m | 191 | 290 | 414 | 653 | 756 | 811 | 995 | 1,247 |
| Diluted shares m | 30.5 | 30.5 | 30.7 | 30.7 | 31.0 | 31.2 | 31.3 | 31.6 |
| FCF €m (FactSet; no dividends) | 373 | 180 | −130 | 749 | 1,926 | 1,804 | 1,607 | 907 |
| ROIC % | 27.0 | 27.2 | 23.1 | 28.8 | 25.0 | 23.7 | 23.9 | 21.5 |
(FactSet Fundamentals.) There is no history before 2018 (IPO June 2018). Consensus (FactSet, 19-Oct-2026): FY2026 €38.59 (hi 44.35 / lo 33.52, σ 1.67, n=34). FY2027 €47.05 (56.63/39.00, σ 2.73, n=34). FY2028 €58.15 (70.40/47.26, σ 3.80, n=32). Consensus net revenue is €2.87bn / €3.48bn / €4.18bn. LTG 14.9%.

## 1. Historic EPS growth decomposition (2018→2025, 7 years)
EPS CAGR was 34.0% (29.3% in log terms). Revenue is on a net-revenue basis. Reported net revenue grew from about €0.35bn (2018) to €2.37bn (2025, FactSet FY0 consensus actual). The 2018 base is approximate (estimate).
| Driver | pts/yr (log) | Evidence | Repeatable? |
|---|---|---|---|
| Volume (processed volume, share-of-wallet + new logos) | ~30 | Processed volume +24% y/y in H1-2026 (StreetAccount, 17-Aug-2026) | Partly (decelerating) |
| Price/take rate | ~−3 | Take rate drifts down as large merchants move to lower tiers (CEO, Q2-26 call) | Y (a drag) |
| Acquisitions | 0 | No acquisitions to 2025 (FactSet acq_to_fcf 0.0) | — |
| Margin change | ~−1.4 | EBITDA margin on net revenue fell from about 58% to about 53% (2022–23 hiring wave) (estimate) | N |
| Share count | −0.5 | Diluted shares went from 30.5m to 31.6m | Y (drag) |
| Interest/tax/other | ~+4 | Interest income on €10.6bn net cash after ECB rates normalised (estimate) | N |
EPS grew ≥7% in every year (7/7), including 2020 (+28%). The worst year was 2025 (+13.7%).

## 2. Forward driver stack (normal year, FY2028–31)
| Driver | pts |
|---|---|
| Volume | 15 |
| Take rate (mix) | −1.5 |
| Operating leverage (EBITDA margin >55% targeted for 2028, reaffirmed H1-26) | 1.5 |
| Buybacks (none: "not prioritised over growth", StreetAccount Q1-26) | 0 |
| Interest income/other | −0.5 |
| **Total** | **≈14.5% vs 7% bar → cushion ≈7.5 pts** |
Volume growth carries almost all of the weight.

**FCF check (reviewer flag):** FAIL.
- Consensus NTM FCFPS of $63.06 × 31.6m shares ≈ $1.99bn, about 1.24× NTM net income (EPS $50.90 × 31.6m ≈ $1.61bn).
- Adyen's own FCF metric is EBITDA − capex. It is pre-tax ("FCF conversion 86%", StreetAccount, 17-Aug-2026), and broker FCFPS appears to follow it (estimate).
- FactSet cash-flow FCF swings with merchant settlement float. It was €1.93bn in 2022 against €0.56bn of net income, and €0.91bn in 2025 against €1.06bn. The 10-year conversion of 1.73x is float, not owner earnings.
- A clean owner FCF of net income + D&A − capex (capex about 7% of revenue in 2026 guidance, above D&A) is about 0.95× net income ≈ $1.5bn. That is **≈5.0–5.5% of market cap (estimate)**, not ≥6%. LTM is 3.1%.
- NTM P/E of 20.5x is above 15x, so Phase 2 does not rescue it. **Test 1 FAIL.**

## 3. What the market is doubting
At 20.5x on +15–24% consensus growth, the market doubts three things. (a) Growth may keep slowing. The 2023 de-rating was caused by US pricing competition, and 2025 was the slowest year at +13.7%. (b) The take rate may keep falling as enterprise mix rises, and Stripe/PayPal-Braintree may compete on price. (c) Agentic commerce, stablecoins and network tokenisation may shrink the value of the acquiring layer. Evidence against these doubts: management says "you don't see it back in our data", with take-rate moves driven by mix and not by price (Q2-26 call). Analysts see "sustained 20%+ growth through 2027", with OpenAI among the wins (StreetAccount, 17-Aug-2026). There is no country, governance or state discount; Dutch governance is founder-friendly. The doubt is mostly temporary or wrong on durability, but the valuation is not cheap.

## 4. TEST 2 — P(EPS FY2031 ≥ 1.30 × €38.59 = €50.16)
FY2028 consensus of €58.15 is already 16% above the bar. EPS could fall 14% from FY2028 and still pass. From FY2026, the bar implies only 5.4%/yr against 15–24% consensus.
| Threat | P | EPS impact | Fails bar? |
|---|---|---|---|
| Competitive/take-rate compression (Stripe, pricing war) | 15% | −20 to −30% vs path | 35% → 5% |
| Loss of 1–2 mega-merchants / platform concentration | 10% | −10 to −15% | 20% → 2% |
| Payments disintermediation (agentic, A2A, stablecoin rails) | 8% | −20% | 35% → 3% |
| Interest-rate collapse cuts float income + recession | 15% | −8% | 10% → 1.5% |
| Regulatory/banking-licence or major outage event | 5% | −15% | 30% → 1.5% |
Σ ≈ 13%, which is **P(Test2) ≈ 87% → FAIL (near-miss)**. Demand is non-cyclical and the balance sheet is a fortress. But the company has no demonstrated pricing power (take rate falls) and faces a credible disruption threat, which keeps it just below the 88–95% wide-moat band.

## 5. TEST 3 — P(EPS ≥ +7% in each of FY2027–FY2031)
- Recurring transaction revenue: about 100% usage-based.
- Volume sensitivity is modest: EPS was +28% in 2020 and +19% in the 2022 investment year.
- There are no buybacks to cushion a weak year.
- History: 7 of 7 years at ≥7%, but the record is short.
- Risks to a single year: an investment-heavy year like 2022–23, a large merchant loss, FX translation, and falling interest income.
- Starting growth is 20%+, so each year has a ~13-pt buffer above 7%.

P(no growth-shock year) ≈ 0.55 × P(normal years ≥7%) ≈ 0.95^5 ≈ 0.77 → ≈42%, rounded to **≈40% → FAIL**. This is close to BR (40%), the highest US anchor.

## 6. Key uncertainty and what would change the view
The key uncertainty is whether the take rate stabilises while volume stays at 20%+ through 2028. A stable take rate and an EBITDA margin of >55% delivered in 2028 would lift P(Test2) to 90% or more. A buyback programme would lift both tests. FX translation: Adyen reports in EUR, and a growing share of net revenue comes from North America and APAC. A weaker USD cuts reported EUR growth by about 2–4 pts (estimate). A USD investor holds the opposite exposure.

## 7. Earnings quality
The adjusted-vs-GAAP gap is −0.2% (5-year average), so there are no adjustments of note. FCF conversion (1.73x over 10 years) is **inflated by merchant float and settlement timing**. Use net income as owner earnings. Flag: FCF overstated by float; NTM FCF ≥6% not supported.

`RESULT | P(Test2)=87% (FAIL) | P(Test3)=40% (FAIL) | Tests passed: 0/3 (Test 1 fails FCF check; P/E 20.5x) | Near-miss: Y | Confidence: M`
