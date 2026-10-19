# Assumptions & judgment calls log
Run date: 2026-10-19 (unattended). All data FactSet unless stated; FMP = Financial Modeling Prep backup.

## Preflight
- A1. FactSet CompanyScreener, EstimatesConsensus, Fundamentals, GlobalPrices all callable (AAPL-US test calls OK). FMP available (AAPL quote OK, 342.94 = FactSet close 19-Oct-2026).
- A2. Notion approach page read OK → approach_summary.md.
- A3. Outputs written to /home/user/financial-services-plugins/buffett_test/ (a sub-folder of the repo, to keep the plugin repo clean).
- A4. `ISON_SECONDARY` lives in the FactSet *Entity* content set (not Fundamentals); screener call adjusted accordingly.

## Stage 1
- A5. Screener returned 826 names (prompt expected ~790); all 826 carried forward to NTM recompute.
- A6. NTM P/E = FactSet close (19-Oct-2026, USD) / FactSet NTMA consensus mean EPS (USD). REITs: NTMA consensus FFO/share where available (else EPS, flagged).
- A7. Consensus convention (verified on AAPL-US): FactSet relativePeriod 0 = last reported FY (actual), 1 = FY1 (first unreported year), 2 = FY2, 3 = FY3.

## Stage 2
- A8. "Adjusted EPS" history = FactSet Estimates *actuals* (broker/street basis) from the surprise endpoint (`surpriseAfter`), annual. GAAP = FactSet FF_EPS_DIL. Where ≥6 years of adjusted actuals exist, growth stats use adjusted; otherwise GAAP.
- A9. FCF = FactSet FF_FREE_CF (CFO – capex). Acquisition spend = FF_ACQ_BUS_CF. Buybacks = FF_STK_PURCH_CF. Net debt/EBITDA computed as FF_NET_DEBT / FF_EBITDA_OPER for the latest FY (FactSet FF_DEBT_EBITDA_OPER is *gross* debt/EBITDA, also stored).
- A10. Segment revenue not pulled per company (optional in brief; tool cost high). Business description and RBICS from FactSet EntityReference.
- A11. For banks/insurers EBIT, EBITDA, FCF and net debt are not meaningful; triage and analysis for financials rely on EPS, ROE, book-value growth (where known) and qualitative credit/underwriting judgement.
- A12. Stage 1 result: 780 PASS (0<NTM P/E<15), 33 near-miss (15–16x), 13 fail, 0 missing. 17 REITs (P/E on NTM FFO for 5 with FFO consensus — NLY, MRP, GLPI, IIPR, VICI; on EPS for 12 mortgage REITs without FFO consensus).
- A13. Six names in the US-HQ universe have primary listings abroad (1316-HK, 1910-HK, 2507-HK, RWC-AU, GQG-AU, LNW-AU); retained because they meet the FactSet HQ=US + primary-listing definition. The three HK names use the 16-Oct-2026 close (no 19-Oct print).
- A14. Very low P/Es (e.g. FMCC 0.8x, FNMA 1.3x, ALIT 1.7x) are carried as-is from FactSet; they are dealt with on business merits in triage (GSE conservatorship, one-off items) rather than discarded as data errors.
- A15. FactSet FF_FREE_CF is net of dividends; FCF used in stats = FF_OPER_CF − |FF_CAPEX| (fallback FF_FREE_CF). Adjusted-EPS snapshots anchored on 19-Oct each year so non-December FYs are captured.
- A16. Pilot batch 00 triaged BANF, MZTI, QDEL; MZTI is not a Test 1 PASS (NTM P/E ≥15) so its triage row is dropped from the final Triage tab.
- A17. Batch 09: FactSet GlobalPrices market_value timed out (408) after retries for all 20 names; market cap backfilled centrally at the end (FactSet retry, else FMP).
- A18. Market value removed from per-batch pulls from batch 19 onward (repeated 408 timeouts); central backfill for all names.
- A19. Stage 3 first pass (39 batch workers): KEEP 59 / TOO HARD 153 / NO 568 of 780. A single reviewer then re-checked all KEEP and TOO HARD verdicts side by side for cross-batch consistency (triage/review_overrides.csv, triage/review_notes.md); final triage.csv applies those overrides.
- A20. Consistency review demoted 23 KEEPs (12 banks at peak-NIM earnings with no ≥7% route; capital-markets earners RJF, AMP, BNY, HLNE; recent transformations BRO, UMBF; cyclical peaks LII, CRH; DHI, PLMR, ALH, VERX, TBBK) and promoted ADBE (consistency with INTU). Final KEEP = 37 (95% discarded — stricter than the ~85–90% guide; accepted rather than loosened, because the demotions follow the brief's own discard rules).
- A21. To give the near-miss watchlist coverage, Stage 4 is also run on the reviewer's next 5 reinstatement candidates (FFIN, CFR, BANF, LII, DHI), labelled "borderline (TOO HARD at triage)". Stage 4 workers take 5 names each (not 20) for depth.
- A22. Market cap: FactSet market_value for 777 names; FMP for DEC, OTF (FactSet null) and ALM (FactSet returned CAD).

## v2 re-run (Test 1 = NTM P/E <18x OR FCF yield ≥6%)
- A23. Candidate screens (FactSet CompanyScreener, USD, base = US HQ, primary listing, FF_MKT_VAL>$1bn): (a) FY2 FE_VALUATION_PE_MEAN 0–20 → 1,172; (b) FF_FCF_YLD ≥4 (latest) → 794 (field worked; no fallback needed); (c) added FY1 FE_VALUATION_PFCF_MEAN 0–25 (forward FCF yield ≥4%) → 632, because FF_FCF_YLD is built on FF_FREE_CF (net of dividends) and would miss high-payout names. Union 1,419; minus 780 v1 PASS = 639 candidates (incl. all 46 v1 near-miss/fail names). 54 of the new PASSes came only via screen (c).
- A24. v1 PASS names are not reprocessed and stay PASS; stage1b_universe.csv holds only the 639 candidates. Its `test1` column re-applies the v1 rule (P/E<15) for reference; the v2 verdict is `test1_v2`.
- A25. NTM P/E = FactSet close 19-Oct-2026 (USD) / NTMA consensus mean EPS (REITs: NTMA FFO where available, 50 REITs). 16-Oct close used only for ACVA; the other 48 ids with no 19-Oct print had no 16-Oct print either (acquired/delisted names still in the screener, e.g. BERY, DFS, HOLX, WBD, EA) → MISSING.
- A26. FCF yield used = NTMA consensus mean FCFPS / price (420 names); fallback LTM = (FF_OPER_CF − |FF_CAPEX|) / (FF_COM_SHS_OUT_EPS_DIL × price), latest FY ending 2025-01-01 to 2026-10-19 where all three are reported (171 names). FF_FREE_CF not used (net of dividends).
- A27. Banks/insurers identified by FactSet FF_GEN_IND (04 Bank, 05 Insurance; 17 candidates incl. UNH, which FactSet classes as Insurance): FCF route set N, P/E route only.
- A28. Extension: Other Financial (FF_GEN_IND 06) non-REITs (brokers, lenders, asset managers, e.g. IBKR, SOFI, BULL, AXP) do not get the LTM CFO−capex fallback, since their CFO includes customer/loan balances (IBKR LTM showed 67%). Their NTM consensus FCFPS is still accepted (AFRM, DAVE pass that way).
- A29. REIT flag = FactSet RBICS industry group containing 'REIT' (121 US names >$1bn, rescreened) ∪ v1 reits.json ∪ (NTM FFO consensus non-null + FF_GEN_IND 06 + REIT-type word in name). 52 candidates flagged; 47 of them PASS (mostly P/FFO <18x), all flagged for triage.
- A30. NEAR_MISS = not PASS and (18 ≤ P/E < 19 or 5.5% ≤ FCF yield < 6%, on an FCF basis the name is eligible for). MISSING = no price, or no NTM earnings and no eligible FCF. Non-positive NTM earnings with no FCF pass = FAIL.
- A31. FCF-only passes on the LTM basis (13, e.g. BCRX, AGNT, MBC, RHLD, GLIBK) can be one-off cash items (royalty sales, working-capital releases). They are kept as Test 1 PASSes and left for triage to judge on the merits, as in A14.
- A32. Result: 639 candidates → 348 new PASS (161 P/E-only, 68 FCF-only [55 NTM, 13 LTM basis], 119 both), 74 near-miss, 164 fail, 53 missing. Of the 46 v1 near-miss/fail names, 42 now PASS. List: data/v2_new_passes.txt; raw pulls: data/raw/v2_*.txt.
