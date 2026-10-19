# Stage 4 — Driver analysis worker instructions (KEEP names)

Working dir: `/home/user/financial-services-plugins/buffett_test`. As-of 2026-10-19. You analyse a small group of KEEP names (listed in your task). For each, write `analyses/<KEY>.md` where KEY = ticker without "-US", "." → "_" (e.g. BRK_B). **Final reply: ONE line only**: `s4 group NN: done [T1 P2=..% P3=..%; T2 ...]`.

Inputs per name: `python3 scripts/summarize.py <TICKER>` (compact stats), `data/<KEY>.json` (full 10y FactSet fundamentals incl. audit formulas, description, adjusted EPS actuals), `data/<KEY>_summary.json` (consensus FY0–FY3 EPS/SALES mean/std/hi/lo/count, LTG), `triage/*.csv` (the KEEP reason), `approach_summary.md` (PM's specialness test). You may use **at most 2** extra tool calls per company for qualitative evidence: FactSet_UnstructuredContent (ToolSearch `select:mcp__FactSet_AI-Ready_Data__FactSet_UnstructuredContent`; sources ALL_TRANSCRIPTS/ALL_NEWS, startDate 2025-07-01, endDate 2026-10-19, ids=[ticker], limit 5, a full-sentence query such as "What are management and analysts saying about pricing, volumes and the outlook?") and/or FactSet_EstimatesConsensus guidance. Use request_id `b7e1c2a0-0004-4a1b-9c1d-s4groupNN`. Do not paste raw results back into your reply.

Sourcing rule: every number must say where it came from, e.g. "(FactSet Fundamentals FY2025)", "(FactSet consensus, 19-Oct-2026)", "(FactSet close 19-Oct-2026)", "(FMP)". Your own estimates must be labelled "estimate". If data are thin, say so and lower confidence; do not invent precise figures.

## Template for analyses/<KEY>.md
```
# <Name> (<TICKER>) — Buffett driver analysis
As-of 2026-10-19 | NTM P/E x.x | Mkt cap $x.xbn | RBICS ... | Confidence: High/Medium/Low
Specialness (PM Part 1 test): Special / Good–track for dislocation / Not special — which of {secular growth, widening moat, excellent management/capital allocation, compelling customer value proposition, oligopoly} apply, one sentence.

## Snapshot table  (FY-10 … FY0 EPS, revenue, EBIT margin, diluted shares, FCF, ROIC/ROE; FY1–FY3 consensus EPS mean/hi/lo/std/n)
## 1. Historic EPS growth decomposition (10y)
EPS CAGR = volume + price/mix + acquisitions + margin change + share count + leverage/tax (approximately additive in log terms; show a table with % pts per year, the evidence, and Repeatable? Y/N/Partly). Use revenue CAGR split into organic vs acquired (acq_to_fcf, known deals), margin change from EBIT margin path, share count from diluted shares CAGR, residual = interest/tax/other. State where splits are estimates (e.g. price vs volume when not disclosed).
## 2. Forward driver stack (normal year)
Table: price, volume, operating leverage, buyback yield (= FCF yield × share of FCF going to buybacks, using market cap and recent FCF), other. Sum vs the 7% bar → cushion (pts). Name the one or two drivers carrying the most weight.
## 3. What the market is doubting
Why <15x NTM; is the doubt temporary, wrong, or right — with evidence.
## 4. TEST 2 — P(EPS in FY1+5 ≥ 1.30 × FY1 consensus)
Frame: "what would have to happen for earnings to be lower in five years?" List specific threats each with a rough probability and EPS impact; derive the overall probability (show the arithmetic, e.g. 1 − Σ or product of survival, noting overlap). PASS if ≥ 90%. Note: 30% over 5 years needs only ~5.4%/yr CAGR.
## 5. TEST 3 — P(EPS grows ≥ 7% in EVERY one of the next 5 years)
Must include a recession year: assess recurring revenue %, pricing power, volume sensitivity, and buyback support in a weak year. Cross-check: in how many of the last 10 years did EPS grow ≥ 7% (years_eps_growth_ge7)? Derive probability (e.g. P(no recession hit) × P(each normal year ≥7%)^n ...). PASS if ≥ 50%. Be realistic: very few companies have ≥50%; a firm that grew ≥7% in fewer than 7 of the last 10 years needs strong reasons to score ≥50%.
## 6. Key uncertainty and what would change the view
## 7. Earnings quality
Flag if adjusted EPS differs from GAAP by >15% (adj_vs_gaap_gap) or FCF conversion persistently <80% (fcf_conversion_5y/10y); explain (e.g. amortisation of acquired intangibles, SBC, working capital build). For financials say "FCF conversion not meaningful".
## Verdict line
`RESULT | P(Test2)=xx% (PASS/FAIL) | P(Test3)=xx% (PASS/FAIL) | Tests passed: n/3 | Near-miss: Y/N (within 5 pts of a threshold) | Confidence: H/M/L`
```
After writing the .md, also append one JSON line per name to `analyses/_results.jsonl`:
`{"ticker":..., "name":..., "ntm_pe":..., "mkt_cap_bn":..., "eps_cagr_10y":..., "cons_growth_fy1":..., "cons_growth_fy2":..., "cons_growth_fy3":..., "p_test2":0.xx, "p_test3":0.xx, "test1":"PASS", "test2":"PASS/FAIL", "test3":"PASS/FAIL", "specialness":"...", "key_uncertainty":"<one sentence>", "confidence":"H/M/L", "driver_sum_pct":..., "top_drivers":"...", "earnings_quality_flag":"..."}`
(use `python3 - <<'EOF' ... json.dumps ... EOF` with append mode). Keep each analysis ~700–1,200 words; precise, no fluff.

Calibration anchors (keep probabilities consistent across companies):
- P(Test2) ≥ 90% requires: recurring/non-cyclical demand, demonstrated pricing power, no material 5-yr disruption threat, balance sheet that survives a recession, AND consensus/driver stack comfortably > 5.4%/yr. A wide-moat compounder with 8–10% normal-year EPS growth ≈ 88–95%. A good business with 1 credible threat ≈ 70–85%. Cyclical exposure → usually < 80%.
- P(Test3) ≥ 50% requires an essentially recession-proof EPS line plus ≥7% growth every year (history ≥ 8/10 years ≥7%, including 2020). Typical good compounder: 20–40%. Banks/insurers rarely > 25%.

## Notes added by orchestrator
- Your tickers: `data/stage4_plan.json` → `groups[NN]`. Names also listed in `borderline_analysed` were TOO HARD at triage; analyse them fully but put "Borderline (TOO HARD at triage)" in the header and `"triage":"BORDERLINE"` in the JSON line (else `"triage":"KEEP"`).
- Market cap: use `market_value_usd_m` in data/<KEY>.json; if null (a central backfill may still be running), make one FMP call (ToolSearch `select:mcp__Financial_Modelling_Prep__company`, endpoint market-cap, symbol without -US) and cite "FMP".
- Final triage reasons are in `triage.csv` (columns reason, review_override).
