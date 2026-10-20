# Triage calibration review — intl Phase 2 (NTM P/E <15x, FCF yield <6% or n/a)

**Scope:** 387 names in batches 31–50. Every KEEP (7) and TOO HARD (76) was compared side by side within its industry using `summarize.py` stats (reporting currency). Each was also checked against the US v1/v2 standard (`../triage/review_notes*.md`). NO rows were spot-checked only for bank, insurer and HFC consistency.
**Result:** KEEP goes from 7 to **5** (1.3% of 387). There are 2 overrides: 2 demotions and 0 promotions (`review_overrides_p2.csv`).

## Demotions
| Name | Why (US precedent) |
|---|---|
| **CB** (Chubb) | Its stats match TRV, which the US run held TOO HARD: 10y CAGR 9.8% for both, worst year −29.5% vs −32.1%, and EPS at 1.0x its max after the hard market. ROE is 11.1%, below ORI's 13.3%. EPS grew only 4.4%/yr through 2016–21, and growth includes deals (ACE–Chubb, Cigna Asia). Keeping it would also be inconsistent with ZURN, which has a better record (14.5% CAGR, 14.9% ROE, worst year −7.9%) and stays TOO HARD with HNR1, MUV2, TLX and ALV. The Greenberg/underwriting quality is real: CB is the first candidate if more names are needed. |
| **AAK** | Peak margin after a sharp run-up (RPM/VMI/MOD rule): margin rose from 5.1% to 10.6% in two years and is at the 91st pctile, EPS jumped +66% in 2023, and cocoa-driven CBE demand also helped (HSY). 10y FCF conversion is 0.32 and LTG is 5%. |

## KEEPs confirmed
- **HDFC Bank: passes the JPM test.** EPS grew 14.27 to 33.37 over FY17–22 at low rates and India never had a NIM windfall. It had no down year through the 2016 AQR, IL&FS and COVID, and 10y avg ROE is 16.6%.
  - The HDFC Ltd merger (Jul-2023) is now 3+ years old, so it is not a pending transformation like COF/UMBF.
  - Correction to the worker's "9/9 years ≥7%": FY24 is missing from the series. EPS went from FY23 39.51 to FY25 43.45 (~4.9%/yr, merger dilution, shares +4.2%/yr), then +12.2% in FY26. Consensus is +16%.
  - Deep-dive items: LDR normalisation, deposit growth versus loan growth, and NIM recovery from about 3.4–3.5%. ICICI and Kotak fail Test 1, so they are not in this phase. Axis (NO; EPS 34.6 to 1.1 over FY15–17) and Federal/City Union (TOO HARD; ROE 11.7–13.0%) confirm HDFC Bank as the only best-in-class Indian bank here.
- **Can Fin Homes: the only HFC with a long, clean through-cycle record.** It has 8/10 growth years, a worst year of −2.4% (IL&FS), ~20% ROE, no dilution and zero M&A, which is the AGM/SFBS analogue.
  - Peers: LIC Housing and PNB Housing are NO; Aptus and Aadhar are TOO HARD on short records.
  - Deep-dive items:
    - The FY26 +26% to INR 81.5 looks like a funding-cost (repo-cut) NIM tailwind, and consensus FY27 is only +3.7%.
    - AUM growth has slowed to ~10%.
    - There is a Canara Bank (PSU) promoter.
    - The ~INR 38cr Ambala branch fraud is <1% of net worth and immaterial, but it is a controls item, as is the 2022 CEO exit.
- **WTW:** kept for consistency with AON (P1 KEEP) and MRSH.
  - Worst year was −0.9%, 10y CAGR is 10.3%, net debt is 1.4x and buybacks are 97% of FCF.
  - The 100th-pctile margin (23.4% vs 16.0% avg) reflects transformation savings plus the Willis Re exit, not the cycle. Unlike BRO there is no transformational deal; Newfront is small.
  - Deep-dive items: ROIC is 6.3% because of goodwill, which is weak against AON's 15.3%, and P&C softening.
- **Howden:** margin is at the 27th pctile (not a peak), ROIC is 27% and net debt is 0.7x. Consensus is +11%/+9.6% on the depot rollout. It is kept like POOL/TSCO. The deep-dive test is the 6.1% 10y CAGR and UK RMI.
- **Virbac:** margin at the 82nd pctile is stable against its 5y average of ~14.5%, and growth is mostly organic, with consensus +13%/+11%/+10%. Bolt-ons run at acq/FCF 0.8 (Sasaeah, Globion), which the deep dive must size against organic growth (ABT/COR rule).

## No promotions
- No TOO HARD name is as forecastable as the kept names. Each fails a stated rule:
  - Banks at a NIM peak and/or with sovereign/FX risk: TLV, BGEO, TBCG, OTP, BKT, KBC, EBS, BG.
  - Reinsurers and P&C at a hard-market peak: HNR1, MUV2, TLX, ZURN, ADM, ALV.
  - Short or untested credit records: Aptus, Five-Star, Avarda, Optima, Aadhar, HDB.
  - Gold-price peak: Muthoot.
  - Merger dilution and wholesale funding: Shriram (ROE 14.9%, shares +4.9%/yr).
  - Capital-markets earnings: IG, XTB, SQN, UBS, STJ, BMED.
  - Government or single-customer exposure: QQ, Indus Towers, Vusion.
- Diageo and UMG fail the HSY/WMG precedents.
- Consistency note: KBC (flat EPS through zero rates, 10y CAGR 4.8%) and BKT have the same profile as SHB/NDA/SWED/INGA, which are NO. Both are TOO HARD; whether they should be NO does not affect the KEEP set.

**Next candidates if more names are needed:** CB, then ZURN, then AAK.
