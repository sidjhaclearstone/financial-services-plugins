# EUROPE & INDIA — Stage 4 driver analysis (KEEP names)

Follow `/home/user/financial-services-plugins/buffett_test/scripts/stage4_prompt.md` (template, tests, calibration anchors, JSON line) with these overrides:
- Working dir: `/home/user/financial-services-plugins/buffett_test/intl`. Data scripts: `BT_DATA=data python3 ../scripts/summarize.py <TICKER>`. Write analyses to `analyses/<KEY>.md` (KEY = ticker with '.'→'_', e.g. NOVN-CH) and append JSON lines to `analyses/_results.jsonl`.
- Your tickers: `data/stage4_plan.json` → `groups[NN]`. Final triage reasons: `triage.csv`. Reply: `intl s4 group NN: done [T1 P2=..% P3=..%; ...]`.
- request_id `b7e1c2a0-0204-4a1b-9c1d-intls4groupNN`. Qualitative evidence: FactSet_UnstructuredContent (ALL_TRANSCRIPTS/ALL_NEWS; ALL_FILINGS covers SEC filers only), max 2 calls per company.
- **Currency:** EPS history, consensus and the Test 2/Test 3 probabilities are in the company's **reporting currency** (state it, e.g. "EPS in EUR"). Valuation (NTM P/E, FCF yield, market cap) is in USD from `data/stage1_universe.csv`. In Section 6 add one line on FX translation risk where relevant.
- Header line must show: region/country, Test 1 phase (1 = FCF yield ≥6%, 2 = P/E <15x), FCF yield and NTM P/E.
- JSON line adds: "region", "country", "phase", "fcf_yield", "currency" and "triage":"KEEP".
- Section 3 (what the market doubts): explain the high FCF yield / low P/E, including any country, governance or state-ownership discount.
- Calibration: stay consistent with the US anchors — skim 2 comparable US analyses in `../analyses/` (see `../analyses/_results_final_v2.jsonl`) before setting probabilities.
- **FCF check (Phase 1):** for names whose FCF yield ≥6% rests on NTM consensus while LTM FCF yield is far lower (HLMA, ADYEN, EVD flagged by the reviewer), reconcile the two (customer float, working capital, capex timing). If the ≥6% cannot be supported, say so in the header, set "fcf_check":"FAIL" in the JSON line (Test 1 then fails on FCF; note whether P/E <15x rescues it), else "fcf_check":"OK".
