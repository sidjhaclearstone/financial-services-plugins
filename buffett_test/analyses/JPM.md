# JPMorgan Chase & Co. (JPM-US) — Buffett driver analysis
As-of 2026-10-19 | NTM P/E 13.1 | Mkt cap $903.0bn (FactSet market value) | RBICS Banking / United States Banks / United States Commercial Banks | Confidence: Medium
Specialness (PM Part 1 test): **Special** — excellent management and capital allocation (Dimon is named in the PM's own list), a widening scale moat (deposit franchise, technology spend, #1 in investment banking and cards — general knowledge) and a quasi-oligopoly among US money-centre banks. Bank cyclicality is the price of admission.

## Snapshot table
Source: FactSet Fundamentals ANN (USD) and FactSet adjusted EPS actuals, pulled 19-Oct-2026. Revenue = FactSet FF_SALES (gross revenue basis; JPM consensus SALES is on a net-revenue basis). FCF not meaningful for a bank/insurer.

| FY | Adj EPS | GAAP EPS | Revenue $m | Net inc $m | Dil. shares m | FCF $m | ROIC % | ROE % |
|---|---|---|---|---|---|---|---|---|
| 2015 | 6.00 | 6.00 | 97,030 | 23,921 | 3,732.8 | -10,038 | 4.7 | 10.0 |
| 2016 | 6.19 | 6.19 | 105,354 | 24,230 | 3,649.8 | 30,325 | 4.6 | 9.7 |
| 2017 | 6.87 | 6.31 | 114,143 | 24,230 | 3,576.8 | -7,156 | 4.7 | 9.5 |
| 2018 | 9.00 | 8.99 | 131,787 | 32,260 | 3,414.0 | 57,998 | 6.2 | 12.6 |
| 2019 | 10.72 | 10.72 | 141,329 | 36,229 | 3,230.4 | 13,784 | 6.8 | 14.0 |
| 2020 | 8.88 | 8.88 | 125,819 | 28,993 | 3,087.4 | 67,897 | 5.3 | 10.7 |
| 2021 | 15.36 | 15.36 | 126,047 | 48,103 | 3,026.6 | 36,602 | 8.4 | 16.8 |
| 2022 | 12.09 | 12.08 | 157,542 | 37,487 | 2,970.0 | 86,261 | 6.4 | 12.8 |
| 2023 | 16.23 | 16.23 | 239,247 | 49,261 | 2,943.1 | 87,319 | 7.7 | 15.9 |
| 2024 | 18.22 | 19.75 | 278,683 | 58,127 | 2,879.0 | 64,631 | 8.1 | 17.3 |
| 2025 | 20.02 | 20.02 | 279,069 | 56,780 | 2,781.5 | 84,242 | 7.4 | 16.1 |

Consensus (FactSet consensus, 19-Oct-2026):

| | FY | EPS mean | EPS hi | EPS lo | EPS std | n | EPS growth % | Sales mean $m | Sales growth % |
|---|---|---|---|---|---|---|---|---|---|
| FY0 | 2025 | 20.02 | 20.02 | 20.02 |  | 1 |  | 182,447 |  |
| FY1 | 2026 | 24.76 | 25.90 | 23.45 | 0.68 | 28 | +23.7 | 208,517 | +14.3 |
| FY2 | 2027 | 25.59 | 27.17 | 24.05 | 0.74 | 28 | +3.3 | 216,609 | +3.9 |
| FY3 | 2028 | 27.52 | 29.60 | 24.90 | 1.13 | 17 | +7.5 | 227,751 | +5.1 |

FactSet EPS LTG: 10.9%. 10y adj EPS CAGR 12.8%, 5y 17.7%; years EPS growth >=7%: 7/10 (FactSet-derived, summarize.py).

## 1. Historic EPS growth decomposition (10y, 2015–2025)
Adj EPS $6.00 → $20.02 = 12.8% CAGR (12.0%/yr log) (FactSet). Adjusted NI (adj EPS × diluted shares) grew 9.1%/yr. Share shrinkage added 2.9 pts/yr.

| Driver | %pts/yr (log) | Evidence | Repeatable? |
|---|---|---|---|
| Volume (deposits, loans, client assets) | ~4.5 (estimate) | Net revenue ~$94bn (2015, company-reported, estimate from memory) → $182.4bn (FY0, FactSet consensus basis) ≈ 6.6%/yr in total | Y |
| Price / mix (NIM, fee rates) | ~1.6 (estimate) | Mostly the 2022–24 rate cycle; NII ex-markets faces a ~$2bn rate headwind in 2026 (CFO, Feb-2026 business update) | N |
| Acquisitions | ~0.5 (estimate) | First Republic 2023 ($9.9bn acquisition cash flow, FactSet) | N |
| Efficiency / credit (net margin) | ~1.6 (estimate) | ROE 10.0% → 16.1% (FactSet) | Partly |
| Tax | ~0.9 (estimate) | 2018 US tax reform (statutory rate 35% → 21%) | N |
| Share count | +2.9 | Diluted shares 3,733m → 2,782m (FactSet) | Y |
| **Total** | **≈12.0** | | |

Roughly 7.5 of the 12 pts are repeatable (volume, buybacks, part of efficiency). Rates, tax and First Republic were one-offs.

## 2. Forward driver stack (normal year)
| Driver | %pts | Basis |
|---|---|---|
| Volume | +4.5 | estimate. Card loans >6% growth guided for 2026, CIB/AWM loans modest (CFO, Feb-2026) |
| Price (NIM) | −0.5 | estimate. Forward curve implies lower IORB (CFO, Feb-2026). Preliminary FY27 NII ex-markets ~$107bn vs ~$95bn guided for FY26 (StreetAccount, Oct-2026) is a near-term offset |
| Operating leverage | +0.5 | estimate. Q3-26 expenses +12.4% y/y (StreetAccount) — investment phase |
| Buyback yield | +3.0 | FY2025 buybacks $34.6bn / $903bn = 3.8% (FactSet). Q3-26 buybacks were lower as capital went to organic growth; 10y share CAGR −2.9% |
| Other (credit normalisation −0.5; Basel III endgame re-proposal capital relief +0.5) | 0 | estimate |
| **Sum** | **≈7.5** | Cushion vs 7% bar: **~+0.5 pts** |

Top drivers: balance-sheet volume and buybacks. FCF yield is not meaningful for a bank, so buyback yield uses actual repurchases.

## 3. What the market is doubting
13x is a normal multiple for a US money-centre bank, not a dislocation. The doubts:
1. **Peak earnings**: EPS is at 1.0x its 10y high.
2. **FY1 is inflated**: Q2-26 included a ~$5.6bn Visa/equity gain (StreetAccount, Jul-2026), worth roughly $1.5/share after tax (estimate). That is why consensus FY2 is only +3.3%.
3. **Rates and credit**: falling rates compress deposit margins. Credit risk is visible in card normalisation and one-off losses such as ~$170m of Tricolor-related charge-offs (Q3-25 call, StreetAccount).
4. **Succession risk.**
Q3-26 was the "first miss going back four years" (StreetAccount, 14-Oct-2026). Doubts 1–2 are **right** for 2027 growth. The franchise doubt is **wrong**: ROTCE ~23% in Q2-26 (StreetAccount) and NII guided up.

## 4. TEST 2 — P(EPS FY2031 ≥ 1.30 × FY1 = $32.19)
FY1 $24.76 → target $32.19 needs 5.4%/yr. Because FY1 contains the one-off gain, the target is effectively measured against a normalised ~$23.2 (estimate), which needs ~6.8%/yr. From FY2 consensus $25.59 it needs 5.9%/yr; from FY3 consensus $27.52, 5.4%/yr (FactSet consensus). The driver stack of ~7.5% clears this by a thin 1.5–2 pts.

| Threat | P(occurs) | P(sinks target) | Contribution |
|---|---|---|---|
| Recession/credit cycle depresses FY2031 specifically (reserve build, NCOs) | 20% | 75% | 15% |
| Return to near-zero rates, deposit-margin compression | 20% | 50% | 10% |
| Succession / management quality slips | 15% | 30% | 4.5% |
| Disintermediation or regulatory capital hit (stablecoins, private credit, capital rules) | 10% | 40% | 4% |
| Normal-year compounding simply runs 5–6% (thin cushion) | — | — | ~12% |

Survival = 0.85 × 0.90 × 0.955 × 0.96 × 0.88 ≈ 0.62 → **≈62% → FAIL**. This fits the calibration anchor that cyclical exposure usually means <80%. The one-off-inflated FY1 base is a large part of the shortfall.

## 5. TEST 3 — P(EPS grows ≥7% in every one of the next 5 years)
- FY1 2026 +23.7% passes, but only because of the gain. FY2 2027 consensus is +3.3% (range −2.9% to +9.7% vs FY1 mean) (FactSet consensus).
- Recession year: NII is not recurring in a contractual sense, and credit costs rise. History: 2020 −17%, 2022 −21% (FactSet). Buybacks get suspended in stress (2020 buybacks $7.9bn vs $28.1bn in 2019, FactSet).
- History: 7/10 years ≥7%, with two down years.
P ≈ P(2027 ≥7%) 0.15 × P(2028–30 ≥7% incl. any recession) 0.2 ≈ **3% → FAIL**. Banks rarely exceed 25% on this test.

## 6. Key uncertainty and what would change the view
The key question is whether NII ex-markets really steps up to ~$107bn in 2027 while expense growth slows. If it does, 2027 EPS could beat the +3.3% consensus and Test 2 would move toward ~75%. Signs of an earlier credit downturn, or a disorderly succession, would lower it.

## 7. Earnings quality
No flag. Adjusted EPS ≈ GAAP (5y average gap −1.5%, FactSet); FY2024 GAAP $19.75 vs adj $18.22 reflected the earlier Visa gain. **FCF conversion is not meaningful** for a bank. Watch the FY2026 one-off gain embedded in consensus EPS.

## Verdict line
`RESULT | P(Test2)=65% (FAIL) | P(Test3)=3% (FAIL) | Tests passed: 1/3 | Near-miss: N | Confidence: M`

## Calibration note
Stage 4 cross-company calibration (19-Oct-2026): P2 62→65%: endpoint-recession contribution aligned with other banks (≈15% × 0.7 ≈ 10.5% vs 15%); the FY1 one-off gain still raises the effective requirement to ~6.8%/yr, so it stays the lowest large bank; FAIL. Sections 4–5 above are left as the worker wrote them; the verdict line shows the calibrated figure.
