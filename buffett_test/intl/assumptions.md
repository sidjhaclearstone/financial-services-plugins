# Europe & India run — assumptions (19-Oct-2026)

Stage 1 (universe + Test 1). Logic copied from the US v2 run (`../scripts/stage1b_build.py`, US assumptions A23–A32) and adapted as below. Build script: `../scripts/stage1_intl_build.py`. Raw FactSet pulls: `data/raw/s1_*.txt` (request_id b7e1c2a0-0201-4a1b-9c1d-intlstage1).

## Universe
- I1. Region membership uses FactSet Entity `FREF_ENTITY_COUNTRY_ISO2` (HQ country). EUROPE = AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GG, GR, HR, HU, IE, IM, IS, IT, JE, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK. Russia, Belarus, Ukraine and Turkey are excluded. INDIA = IN. The screener's `IN` operator needs at least 3 values, so India uses `EQ IN`. The HQ country from EntityReference (`headquartersCountry`) agreed with the region for all 1,735 candidates.
- I2. Base universe: HQ in the region, `ISON_SECONDARY = 0` (primary listing only) and `FF_MKT_VAL > 1000` with currencyConversion USD (>$1bn). Base counts are the screener pagination total of a limit-1 search: Europe 1,544, India 534.
- I3. Primary line = whatever FactSet marks as the primary listing (`ISON_SECONDARY = 0`). This keeps one line per entity, with no duplicate entities among the candidates. ADRs/GDRs are secondary lines, so they are excluded automatically. Dual-listed names come through on a single home line: Unilever ULVR-GB, Shell SHEL-GB, RELX REL-GB, Rio Tinto RIO-GB, Glencore GLEN-GB, ArcelorMittal MT-NL, Stellantis STLAM-IT, Airbus AIR-FR, Ferrovial FER-ES, Prosus PRX-NL, Wolters Kluwer WKL-NL, Coca-Cola HBC CCH-GB. For dual-class shares (e.g. ATCO.A vs ATCO.B, INVE.B, HEIO vs HEIA) only the class FactSet flags as primary is kept.
- I4. Some names have a European (or Indian) FactSet HQ but their primary listing is in the US, HK, CA or ZA. There are 82 such names in Europe, e.g. ACN, MDT, ETN, AON, WTW, LIN, CB, TEL, JCI, TT, APTV, NXPI, SPOT, ARM, PDD, 1913-HK Prada, 6160-HK BeOne, EDV-CA, NRP-ZA. India has 3: MMYT-US, RNW-US, WNS-US. They are kept, consistent with US A13 (FactSet HQ + primary-listing definition). None of them were in the US universe, which was US-HQ only, so nothing is counted twice. They are tagged "primary listing XX, HQ YY" in `source_note`.
- I5. The FactSet primary-listing list includes some lines that are hard to invest in. Euronext Brussels Expert Market numeric lines are one example: 1153317-BE Etex, 1153319-BE BNP Paribas Fortis, 1154155-BE BGL BNP Paribas. Listed subsidiaries of other candidates are another: Hindustan Unilever, Nestlé India, DWS, EDPR, Porsche AG, Vår Energi and others, 101 names in total. All are kept mechanically and tagged in `source_note` ("Expert Market" / "subsidiary of listed X – low free float") for triage. Etex passes Phase 1 on LTM FCF.

## Prefilters (candidates)
- I6. Three prefilter screens were run per region (CompanyScreener, USD, limit 500, paginated) and their union taken:
  - (a) FY1 `FE_VALUATION_MCAP_FCF_MEAN` between 0 and 25 (forward P/FCF): Europe 986, India 330.
  - (b) latest `FF_FCF_YLD ≥ 4`: Europe 585, India 119.
  - (c) FY2 `FE_VALUATION_PE_MEAN` between 0 and 17: Europe 883, India 136.

  The union is 1,735 candidates (Europe 1,297, India 438), saved in `data/candidates.csv` with the screens each name hit. The P/E prefilter is set at 17, two turns above the Test 1 limit of 15, so FY2-vs-NTM timing differences don't drop names. The P/FCF prefilter at 25 (≥4% yield) does the same for the 6% FCF route.
- I7. Some pages came back inline rather than auto-saved: Europe screen (b) page 2, the FFO pull, India and others on the last price page, and the 16-Oct price retry. These were rewritten to the raw files field for field, in the same JSON layout.

## Data and currency conventions
- I8. All money is in USD: estimates use `currency=USD`, prices use GlobalPrices `currency=USD`, fundamentals use `currency=USD`, and the screener uses currencyConversion USD. FactSet does the FX conversion, so ratios are effectively local-currency ratios apart from rate-timing differences between estimate, price and fundamentals dates.
- I9. The consensus snapshot is the latest FactSet NTMA consensus. Calls were made with no dates and returned estimateDate 2026-10-20. That is one day after the 19-Oct price date and was accepted as equivalent; no PIT pull was made.
- I10. Price is the 19-Oct-2026 close (single-day calls of ≤500 ids). There are 26 ids with no 19-Oct print:
  - 1913-HK and 6160-HK (Hong Kong was closed on 19-Oct for the Chung Yeung holiday) use the 16-Oct close.
  - The other 24 had no 16-Oct print either. These are acquired, delisted or redomiciled lines that still sit in the screener: Ashtead AHT-GB (primary line moved), Carnival UK CCL-GB, Deliveroo, TI Fluid, Bakkavor, Alpha Group, Beazley, Virgin Money, Dalata, Global Blue, Janus Henderson, Just Eat ADR, JDE Peet's (JDEP), ABOUT YOU, Banca Pop. Sondrio, Minor Hotels, X5, Tatra Banka, Public Property Invest, Piramal Enterprises, Gujarat State Petronet, ICICI Securities, Interise Trust, WNS. All 24 are MISSING.
- I11. NTM P/E = price / NTMA consensus mean EPS. REITs use NTMA FFO where available.
- I12. FCF yield used = NTMA consensus mean FCFPS / price. Fallback LTM = (FF_OPER_CF − |FF_CAPEX|) / (FF_COM_SHS_OUT_EPS_DIL × price), using the latest FY ending 2025-01-01 to 2026-10-19 where all three are reported. Indian March year-ends therefore usually use FY Mar-2026. FactSet FF_FREE_CF is not used because it is net of dividends. For multi-class companies the LTM figure divides total CFO by total diluted shares and multiplies by the primary-class price, which is approximate.

## Test 1 rules (as briefed)
- I13. FCF route: FCF yield used ≥ 6%, which makes the name Phase 1.
  - Banks (FF_GEN_IND 04) and insurers (05) are excluded from the FCF route. That is 191 candidates, P/E route only.
  - Other Financial (06) non-REITs and all REITs may use the NTM consensus FCFPS basis only (no LTM fallback, as in US A28). 74 names had only an LTM yield and lost the FCF route.
- I14. P/E route: 0 < NTM P/E < 15. A name that passes on P/E but not on FCF is Phase 2. "Both routes" = Phase 1 names that also pass on P/E.
- I15. NEAR_MISS = not PASS and either 15 ≤ P/E < 16 or 5.5% ≤ eligible FCF yield < 6%. MISSING = no price, or no NTM earnings and no eligible FCF yield. Non-positive earnings with no FCF pass = FAIL.
- I16. REIT flag: FactSet RBICS industry group = "Equity REITs" or "Property Owners", 74 candidates. European listed property companies (Vonovia, LEG, Swedish property companies, UK REITs, SIIC/SOCIMI/SIIQ) are economically REIT-like, and their EPS includes revaluations, so their P/E is taken on NTMA FFO (EPRA-style recurring earnings). 59 have FFO consensus; the other 15 fall back to EPS and are flagged. 56 REIT-like names PASS, mostly on P/FFO.

## Data-quality flags
- I17. 24 PASS names have extreme values (FCF yield >25% or P/E <4x), e.g. CLARI-FR, WIZZ-GB, CEC-DE, GN-DK, CLVT-US, VOW3-DE, PAH3-DE, SBB.B-SE. They are tagged "CHECK:" in `source_note` and listed in `stage1_summary.json` → `check_flags`. They are kept as PASS and left for triage to verify. Likely causes are recent share-count changes, consensus FCF that includes one-offs, or holding-company structures. This is the same treatment as US A31.
- I18. LTM-basis FCF passes may reflect one-off cash items, as in US A31. They are kept and left to triage: 63 Phase-1 passes are on the LTM basis (Europe 53, India 10).
- I19. EntityReference was pulled for all 1,735 candidates (35 calls, at or under the 40-call limit). It gives HQ country, incorporation country, RBICS economy, sector, subsector and industry group, and ultimate parent. Saved raw (`data/raw/s1_entity_c*.txt`) and flattened to `data/entity_info.csv`.

## Result
- I20. Results by region:
  - Europe: base 1,544 → 1,297 candidates → 869 PASS. That is 563 Phase 1 (444 of them also pass on P/E) and 306 Phase 2, of which 125 are banks or insurers. Also 64 near-miss, 319 fail, 45 missing.
  - India: base 534 → 438 candidates → 117 PASS. That is 36 Phase 1 (18 also pass on P/E) and 81 Phase 2, of which 22 are banks or insurers. Also 16 near-miss, 293 fail, 12 missing.
  - Total: 986 PASS, 80 near-miss, 57 missing.

  The European pass rate (56% of base) is much higher than the US rate. Many European cyclicals, autos, telecoms, utilities and banks trade at a 6%+ forward FCF yield or under 15x. Stage 3 triage will have to carry the "bargain without specialness" filter. Lists: `data/phase1_passes.txt` (sorted by FCF yield, descending), `data/phase2_passes.txt` (sorted by P/E, ascending), `data/test1_passes.txt`. Both orderings are Europe first, then India.
