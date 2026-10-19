# Stage 2 (data pull) + Stage 3 (Buffett triage) — batch worker instructions

Working dir: `/home/user/financial-services-plugins/buffett_test`. As-of date 2026-10-19.
You process ONE batch of ~20 US-listed tickers (FactSet format, e.g. `BANF-US`). Write all outputs to files.
**Your final reply must be ONE line only**: `batch NN: ingested X/Y, KEEP=a TOO_HARD=b NO=c, missing=[...]`.

Never paste bulk data into your reasoning or reply. Big tool results are auto-saved to a file whose path the tool response gives you — pass that path to the ingest script. If a result comes back inline (small), save it yourself with a heredoc to `data/raw/<batch>_<kind>.json` exactly as returned and pass that path.

Load tools first: ToolSearch `select:mcp__FactSet_AI-Ready_Data__FactSet_Fundamentals,mcp__FactSet_AI-Ready_Data__FactSet_EntityReference,mcp__FactSet_AI-Ready_Data__FactSet_EstimatesConsensus,mcp__FactSet_AI-Ready_Data__FactSet_GlobalPrices`. Use `request_id` = `b7e1c2a0-0003-4a1b-9c1d-batchNN` (NN = batch number) on every FactSet call. `mkdir -p data/raw`.

## A. Data pull (Stage 2) — batch all ids into each call
1. **Fundamentals** (FactSet_Fundamentals, data_type=fundamentals, periodicity=ANN, fiscalPeriodStart=2015-01-01, fiscalPeriodEnd=2026-10-19, currency=USD, audit=AUDIT_CARD). Metric codes are pre-validated (do NOT call FactSet_Metrics). Make 3 calls with all batch ids, one per group:
   - G1: FF_SALES, FF_EBIT_OPER, FF_EBIT_OPER_MGN, FF_EBITDA_OPER, FF_NET_INC, FF_EPS_DIL, FF_EPS_DIL_BEF_UNUSUAL
   - G2: FF_COM_SHS_OUT_EPS_DIL, FF_ROIC, FF_ROE, FF_FREE_CF, FF_OPER_CF, FF_CAPEX
   - G3: FF_NET_DEBT, FF_DEBT_EBITDA_OPER, FF_DIV_CF, FF_STK_PURCH_CF, FF_ACQ_BUS_CF
   If a call errors on size, split the ids in half. On any failed call: retry twice, then continue.
2. **Entity reference** (FactSet_EntityReference, data_type=entity_reference, all ids in one call): business description + RBICS.
3. **Adjusted EPS actuals** (FactSet_EstimatesConsensus estimate_type=surprise, metrics=["EPS"], periodicity=ANN, startDate=2015-10-19, endDate=2026-10-19, frequency="AY", currency=USD, all ids). If REITs are in the batch (see `data/stage1_universe.csv` column is_reit) make a second call with metrics=["FFO"] for the REIT ids only and save it — pass it to ingest with `--surprise` too (FFO actuals overwrite EPS actuals for REITs — that is intended).
4. **Market value**: SKIP (backfilled centrally by the orchestrator; omit --mv).
5. Ingest: `python3 scripts/ingest_batch.py --fund G1PATH --fund G2PATH --fund G3PATH --entity EPATH --surprise SPATH --mv MPATH`
6. **Gaps → FMP backup**: run `python3 scripts/summarize.py <ids>` and check each block. If a company has no FactSet fundamentals at all, or no EPS history, use FMP (ToolSearch `select:mcp__Financial_Modelling_Prep__statements,mcp__Financial_Modelling_Prep__company`): `statements income-statement` / `cashflow-statement` (symbol without -US, period=annual, limit=11). Save raw to data/raw/, then with a short python snippet map into that ticker's data/<T>.json under `fundamentals` using the same FF_ codes (FF_SALES=revenue, FF_EBIT_OPER=operatingIncome, FF_NET_INC=netIncome, FF_EPS_DIL=epsDiluted, FF_COM_SHS_OUT_EPS_DIL=weightedAverageShsOutDil/1e6, FF_FREE_CF=freeCashFlow/1e6, FF_STK_PURCH_CF=commonStockRepurchased/1e6, FF_DIV_CF=dividendsPaid/1e6, FF_ACQ_BUS_CF=acquisitionsNet/1e6; revenue etc. in USD millions), record `"fmp_backup": {"fundamentals": "FMP statements, pulled 2026-10-19"}`, and append any still-missing items to `missing`. Max ~5 FMP names per batch; otherwise mark missing and move on. Re-run summarize.py after.
7. Segment revenue: not pulled per batch (optional; skip).

## B. Buffett triage (Stage 3)
Read the compact summaries (`python3 scripts/summarize.py <ids>` output) plus each company's `entity.description` in data/<T>.json. Also read `approach_summary.md` (the PM's "specialness" test). For each name give **one** verdict:
- **KEEP** — a business you could forecast 5–10 years out with reasonable confidence, durable economics, AND a plausible route to ≥7%/yr EPS growth. These go to deep driver analysis.
- **TOO HARD** — may be fine but you cannot forecast it with confidence (complexity, opaque, binary outcomes, recent transformation).
- **NO** — fails a Buffett test below, or is a cheap-but-ordinary business with no specialness (approach_summary.md: "bargains that are not special are a no").

Discard (TOO HARD or NO) where:
- earnings are set mainly by things no one can forecast: commodity prices (energy, metals, chemicals, ag, refiners, miners, steel), interest-rate/credit cycles (spread-dependent lenders, mortgage, subprime), capital-markets activity (brokers, IB, asset managers driven by markets);
- current earnings are at or near a cyclical peak (use latest_eps_vs_10y_max, margin_pctile_in_history vs the 10-year history: e.g. EPS ≥0.95× 10y max AND margin in top decile after a sharp run-up in a cyclical industry);
- a credible technology, regulatory, litigation or single-customer threat exists within 5 years (e.g. GLP-1s, AI disintermediation, drug patent cliffs, government reimbursement, tobacco/opioid litigation, one dominant customer);
- growth has come from acquisitions or leverage rather than the core business (acq_to_fcf_10y high, shares rising, net_debt_ebitda high);
- the balance sheet could not comfortably survive a recession (net_debt_ebitda > ~3.5x for a cyclical, or > ~5x for a defensive; for banks/insurers judge capital/credit quality qualitatively);
- the business is too hard to understand well enough to forecast.
Do NOT exclude whole sectors mechanically — Buffett owns banks, insurers, railroads. A disciplined, low-cost-deposit, conservatively underwritten bank or a disciplined P&C underwriter with a long record can be KEEP; judge each business. Be strict: expect only ~10–15% KEEP overall (about 2–3 per batch of 20; 0 is fine; >5 means you are too lenient). Use your knowledge of the company to supplement the data, but rely on the data where they conflict and say so.

Write `triage/batch_NN.csv` (create `triage/` dir) with header `ticker,name,verdict,reason,flags` — one row per ticker; `reason` = one sentence, specific (cite a number where useful, e.g. "EPS 0.98x 10y peak with margin at 10y high in a commodity chemical"); quote the field with double quotes; `flags` = semicolon list from {REIT, DATA_GAP, FMP_BACKUP, ADJ_GAAP_GAP, LOW_COVERAGE} as applicable. Every ticker in the batch must have a row (use verdict `NO` + reason "insufficient data" + DATA_GAP only if essentially nothing could be retrieved).

Finally update `progress.json` safely: `python3 -c "import json;p=json.load(open('progress.json'));p.setdefault('batches',{})['NN']='done';json.dump(p,open('progress.json','w'),indent=1)"` (replace NN).
