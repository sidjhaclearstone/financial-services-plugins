# EUROPE & INDIA — Stage 2 (data pull) + Stage 3 (Buffett triage) — batch worker instructions

Working dir: `/home/user/financial-services-plugins/buffett_test/intl`. Run every script with the data dir set, e.g.
`BT_DATA=data python3 ../scripts/summarize.py <ids>` and `BT_DATA=data python3 ../scripts/ingest_batch.py ...`. As-of 2026-10-19.
You process ONE batch of ≤20 tickers in FactSet format (e.g. `NOVN-CH`, `RELX-GB`, `INFY-IN`). Write all outputs to files.
**Final reply: ONE line only**: `intl batch NN: ingested X/Y, KEEP=a TOO_HARD=b NO=c, missing=[...]`.

Never paste bulk data into your reasoning or reply. Big tool results are auto-saved to a file whose path the response gives — pass that path to the ingest script. Small inline results: save them exactly with a heredoc to `data/raw/<batch>_<kind>.json` and pass that path.

Load tools: ToolSearch `select:mcp__FactSet_AI-Ready_Data__FactSet_Fundamentals,mcp__FactSet_AI-Ready_Data__FactSet_EntityReference,mcp__FactSet_AI-Ready_Data__FactSet_EstimatesConsensus`. `request_id` = `b7e1c2a0-0203-4a1b-9c1d-intlbatchNN` on every FactSet call.

## Currency convention (important)
- Valuation (P/E, FCF yield, market cap) is already computed in USD in `data/stage1_universe.csv` — do not recompute.
- History and growth must be in the company's **reporting currency** so FX moves do not distort EPS growth: Fundamentals `currency="DOC"`; adjusted-EPS actuals and consensus `currency="ESTIMATE"`. Say "reporting currency (EUR/GBP/CHF/INR …)" when you cite numbers.

## A. Data pull — batch all ids into each call
1. **Fundamentals** (data_type=fundamentals, periodicity=ANN, fiscalPeriodStart=2015-01-01, fiscalPeriodEnd=2026-10-19, currency=DOC, audit=AUDIT_CARD). Pre-validated metric codes (do NOT call FactSet_Metrics). 3 calls with all ids:
   - G1: FF_SALES, FF_EBIT_OPER, FF_EBIT_OPER_MGN, FF_EBITDA_OPER, FF_NET_INC, FF_EPS_DIL, FF_EPS_DIL_BEF_UNUSUAL
   - G2: FF_COM_SHS_OUT_EPS_DIL, FF_ROIC, FF_ROE, FF_FREE_CF, FF_OPER_CF, FF_CAPEX
   - G3: FF_NET_DEBT, FF_DEBT_EBITDA_OPER, FF_DIV_CF, FF_STK_PURCH_CF, FF_ACQ_BUS_CF
   On size errors split ids in half. Failed call: retry twice, then continue. (Indian companies with March year-ends: FY2026 = year to Mar-2026.)
2. **Entity reference** (EntityReference, entity_reference, all ids, ≤50): description + RBICS + country.
3. **Adjusted EPS actuals**: EstimatesConsensus estimate_type=surprise, metrics ["EPS"], periodicity ANN, startDate 2015-10-19, endDate 2026-10-19, frequency "AY", currency "ESTIMATE", all ids. REITs (is_reit in stage1_universe.csv): second call with ["FFO"] for those ids and pass it to ingest too.
4. Market value: SKIP (taken from stage 1).
5. Ingest: `BT_DATA=data python3 ../scripts/ingest_batch.py --fund G1 --fund G2 --fund G3 --entity E --surprise S`
6. Gaps → FMP backup only if a company has no FactSet fundamentals/EPS at all (ToolSearch `select:mcp__Financial_Modelling_Prep__statements`; FMP symbols: NOVN.SW, RELX.L, SAP.DE, INFY.NS etc.; reported currency). Map into data/<KEY>.json as in the US run (KEY = ticker as file name with '.'→'_', e.g. NOVN-CH). Max ~5 names; otherwise mark missing. Re-run summarize after.

## B. Buffett triage (Stage 3)
Read the compact summaries (`BT_DATA=data python3 ../scripts/summarize.py <ids>`), each `entity.description`, `approach_summary.md` (PM's specialness test) and the US calibration notes `../triage/review_notes.md` + `../triage/review_notes_v2.md` (principles applied in the US run — apply the same strictness). Verdicts:
- **KEEP** — forecastable 5–10 years out with reasonable confidence, durable economics, plausible route to ≥7%/yr EPS growth in reporting currency.
- **TOO HARD** — may be fine but cannot be forecast with confidence.
- **NO** — fails a Buffett test, or cheap-but-ordinary with no specialness.
Discard where: earnings set mainly by commodity prices, rate/credit cycles, or capital-markets activity; earnings at/near a cyclical peak (latest_eps_vs_10y_max, margin_pctile_in_history); a credible 5-yr technology/regulatory/litigation/single-customer threat; growth from acquisitions or leverage; balance sheet that could not survive a recession; too hard to understand.
Additional Europe/India lenses (judge, don't apply mechanically):
- **State ownership / policy risk** (Indian PSUs, European state-controlled utilities/telcos/defence): earnings subject to government pricing or dividend policy → usually TOO HARD unless the record proves otherwise.
- **Promoter/group governance (India)**: related-party dealings, pledged shares, complex group structures → TOO HARD/NO.
- **Regulated returns** (utilities, airports, toll roads): forecastable but growth usually <7% → typically NO on growth, unless rate base growth clearly supports ≥7% EPS.
- **FX translation**: a European company earning mostly in USD/EM currencies — judge growth in reporting currency and note translation risk.
- **FCF-route names (Phase 1)**: check FCF is recurring (not working-capital release, asset sales, or capex holiday).
Do NOT exclude whole sectors mechanically. Be strict: expect ~5–10% KEEP (1–2 per 20; 0 is fine; >4 means too lenient).

Write `triage/batch_NN.csv` with header `ticker,name,verdict,reason,flags` — one row per ticker; reason = one specific sentence (cite numbers, in reporting currency); flags from {REIT, DATA_GAP, FMP_BACKUP, ADJ_GAAP_GAP, LOW_COVERAGE, FCF_ROUTE, STATE_OWNED, GOVERNANCE, FX}. Every ticker must have a row.
Finally: `python3 -c "import json;p=json.load(open('progress.json'));p.setdefault('batches',{})['NN']='done';json.dump(p,open('progress.json','w'),indent=1)"` (create progress.json if missing).
