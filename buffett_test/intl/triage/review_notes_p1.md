# Phase 1 calibration review: Europe & India (FCF yield ≥6%)

**Scope:** batches 01–30, 599 names. I compared every KEEP (12) and TOO HARD (136) within its RBICS industry using `summarize.py` stats. I checked each against the US final KEEPs and US overrides (v1/v2) in the same industries. I spot-checked NO rows with strong stats (10y EPS CAGR ≥9%, ROIC ≥12%, ND/EBITDA <2.5x); all 17 were correctly NO (peak cyclicals, commodity names, patent cliffs).
**Result:** KEEP stays at **12** (2.0%). There are 2 overrides (`review_overrides_p1.csv`):
- **DTE-DE** demoted to TOO HARD.
- **LSEG-GB** promoted to KEEP.

## Overrides
- **DTE (demoted).** The 17.1% FCF yield is a consolidation artefact. It includes 100% of T-Mobile US FCF, but DTE owns only about 52%. DTE still passes on P/E (10.2x), so valuation is not the issue. Judged on its own merits, it fails:
  - 10y average ROIC is 3.8%.
  - The margin is at its 100th pctile only because Sprint is consolidated.
  - The ex-US business is a low-growth incumbent with a ~28% state holding.
  - The ≥7% route depends on TMUS buybacks plus EUR/USD translation.
  - The quality asset is already held directly as a US KEEP (TMUS).
  - This matches CDI (an LVMH holdco, TOO HARD).
- **LSEG (promoted).** Refinitiv has been seasoned since Jan-2021. Adjusted EPS grew 8.7%/yr over 2021–25, the worst year in 10 was −1.7%, the margin is at the 45th pctile, ND/EBITDA is 1.73x and consensus is +12–15%. That is as forecastable as WKL (KEEP) and US TRU, which was kept despite an acquisition-driven adj/GAAP gap. Unlike MORN, it has no capital-markets drawdown.

## KEEPs confirmed (specific checks)
- **ADYEN.** EPS rose every year, including through the 2022–23 payments slowdown. It has net cash, no M&A, and is kept like US CPAY. Stripe take-rate pressure is the deep-dive test.
- **LVMH.** It is not at a cyclical peak:
  - EPS is 0.73x the 2023 high.
  - The margin of 21.9% is at its 10y average (22.0%).
  - EPS still compounded 7.5%/yr from 2019 to 2025, through the boom and bust.

  **CDI** stays TOO HARD for different reasons: the Arnault family holds about 97%, there is no consensus, and its 18.7% LTM yield consolidates 100% of LVMH.
- **AON.** NFP (closed Apr-2024) is about 18% of revenue. Leverage is back to 2.3x and EPS rose every year. This follows the MRSH precedent (2.4x) rather than BRO's transformational deal.
- **TEL.** It is kept on the AWI precedent: the margin of 19.3% is a modest drift above its 17.0% average, and the range was 14.6–19.3%. It differs from the auto peers that stay TOO HARD (ALV, APTV, NXPI, CIE, MELE): ROIC is 13.7% and the business is diversified beyond autos.
- **HLMA.** It is kept as instructed; P/E alone is not a demotion reason.
- **Other KEEPs.** The classifieds (AUTO, G24, BCG) match US CARG. IONOS matches US GDDY. WKL matches INTU/ADSK.
- **FCF-route caution for Stage 4.** Three passes rest on NTM consensus FCF per share. On LTM or earnings-based measures they sit below 6%. If Stage 4 cannot verify FCF, demote them, following the US AGX/CHWY precedent.

| Name | NTM FCF yield | LTM FCF yield | Earnings yield | Likely source of the gap |
|---|---|---|---|---|
| HLMA | 6.4% | 3.0% | 4.2% | Unclear; 10y FCF conversion is only 1.04x |
| ADYEN | 6.0% | 3.1% | – | Merchant float |
| EVD | 7.6% | 1.5% | – | Ticket float |

## TOO HARD left unchanged (main consistency groups)
- **AI threat to labour-based billing** (as US EPAM/G/DOX/EXLS): ACN, Infosys, Capgemini, Sopra, Wavestone, Neurones, Sweco, Arcadis, Ipsos.
- **Capital-markets earners** (as US MORN/BX/HLNE): Partners Group, EQT, CVC, ICG, Antin, Bridgepoint, Amundi, DWS, AJ Bell, IntegraFin, Quilter, flatex. Wise is in this group because its earnings depend on interest rates.
- **Acquisition-driven** (as US ROP/AJG/BRO): DSV, Vitec, Addnode, Karnov, Recordati, Rentokil, Elis.
- **Near peak** (as US LII/CRH): PNR, Konecranes, Saint-Gobain, Buzzi, VINCI, DEME, Vidrala, Coats.
- **Regulatory** (credible 5-year threat): Edenred, Pluxee, IEX (market coupling), Evolution, FDJ.
- **Closest misses, in order:** Gamma Communications (FY1 −2.8%, consensus about 7%), Royal Unibrew (5y CAGR 5.4%), Interpump (cyclical: −24% from peak).

## Why India produced no Phase 1 KEEPs
Only 36 of the 599 Phase 1 names are Indian: 30 NO and 6 TOO HARD.
- **What passes the screen.** A ≥6% FCF yield admits mostly cheap cyclicals. 21 of the 30 NOs are state-owned refiners and E&Ps, metals and mining names, or group-controlled commodity or governance cases.
- **What it leaves out.** India's quality consumer franchises trade at 30–60x earnings with FCF yields around 1–4%, so they never reach this phase. The same applies to most IT services and private financials.
- **The two IT names that did pass.** Infosys and Wipro lack a ≥7% route: consensus is +1.8%/+4.2%/+5.0% for Infosys and +3.2%/+3.3%/+7.1% for Wipro. Both are consistent with ACN and US EPAM.
- **Other quality names.** BLS, Firstsource and IEX fail on government-contract, AI or regulatory threats.

Indian compounders, if any, should come through Phase 2, the P/E route (batches 31–50).
