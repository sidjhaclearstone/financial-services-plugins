# Stage 4 calibration review (19-Oct-2026)

**Method.** I compared all 42 analyses (`_results.jsonl`, the Test 2/3 sections of each .md, and `scripts/summarize.py` stats: years ≥7%, FY1→FY3 consensus, net debt/EBITDA, margin percentile) within peer sets: banks, insurers, software/platforms, consumer/leisure, industrials and medtech. I applied three yardsticks. (1) **Same threat, similar probability:** an endpoint recession is about 15% for industrials and banks, a rate-cut cycle is about 25–30%, and a scenario where growth falls below the 5.4%/yr bar fails about half the time. (2) **Test 2 must match the driver stack and consensus cushion:** I checked how much growth is still needed after FY3 consensus and whether the survival arithmetic adds up. (3) **Test 3 must match history and recession sensitivity:** I checked years ≥7% (including 2020), the FY1/FY2 consensus, and a common P(no recession in 5 years) of about 0.5–0.6. I moved numbers only where the reasoning or arithmetic was inconsistent. No Test 3 needed changing: every P3 is either broken by FY1/FY2 consensus or within the 20–40% compounder band (banks and insurers ≤25%). The harshness in group 01 was mostly in the arithmetic or the threat framing (BSX, JPM, AOS). PGR (37%) was kept: it needs about 14%/yr after FY3 consensus against a 96% combined-ratio target. FCN (75%) was kept because it sits in line with CARG and PLNT.

**Result.** I changed 9 of 42, all on Test 2 only. None crossed a threshold. GEHC dropped out of the near-miss group.

| Ticker | P2 % | P3 % | Drv %/yr | Calibration |
|---|---|---|---|---|
| ADBE | 85 | 37 | 14.5 | unchanged |
| TRU | 85 | 25 | 11.0 | unchanged |
| CPAY | 85 | 30 | 17.5 | unchanged |
| GL | 83 | 8 | 9.5 | unchanged |
| INTU | 80→**83** | 30 | 13.0 | dropped 3-pt 'basis error' wrongly counted as failure |
| PRI | 83 | 20 | 9.8 | unchanged |
| GDDY | 82 | 28 | 15.5 | unchanged |
| TMUS | 82 | 27 | 11.5 | unchanged |
| GEHC | 85→**80** | 18 | 8.5 | growth-below-bar stall weighted 0.5 (as PLNT/ZTS) |
| BLKB | 80 | 18 | 10.5 | unchanged |
| ATMU | 78 | 12 | 6.9 | unchanged |
| AGM | 78 | 14 | 9.0 | unchanged |
| PBH | 78 | 4 | 7.5 | unchanged |
| CBSH | 78 | 3 | 7.8 | unchanged |
| BKNG | 78 | 25 | 14.3 | unchanged |
| SFBS | 78 | 17 | 10.3 | unchanged |
| BFAM | 76 | 27 | 10.5 | unchanged |
| EWBC | 76 | 8 | 6.7 | unchanged |
| CFR | 72→**75** | 4 | 7.5 | rate-cut failure rate 0.7→0.5 (vs CBSH/EWBC) |
| DECK | 75 | 15 | 12.0 | unchanged |
| POOL | 75 | 2 | 8.8 | unchanged |
| DORM | 75 | 1 | 8.4 | unchanged |
| PLNT | 75 | 12 | 10.0 | unchanged |
| CARG | 75 | 20 | 13.5 | unchanged |
| HAYW | 72→**75** | 10 | 10.5 | arithmetic gave 78%; held at POOL level (volatile, Low conf.) |
| FCN | 75 | 2 | 10.0 | unchanged |
| BRC | 75 | 18 | 7.0 | unchanged |
| HII | 75 | 10 | 10.5 | unchanged |
| CSL | 70→**74** | 12 | 12.0 | endpoint recession 20%→15% (industrial peers) |
| COO | 73 | 5 | 7.8 | unchanged |
| BOOT | 73 | 16 | 13.5 | unchanged |
| LII | 72 | 3 | 8.0 | unchanged |
| SFM | 65→**72** | 2 | 12.5 | arithmetic: own 31% − 3 overlap ⇒ 72% |
| AOS | 68→**70** | 1 | 6.0 | net-cash offset applied upward (survival 0.70) |
| ORI | 70 | 2 | 7.5 | unchanged |
| ZTS | 70 | 1 | 9.3 | unchanged |
| BSX | 65→**68** | 3 | 7.0 | Watchman/PFA treated as one correlated threat (as ZTS) |
| FFIN | 67 | 3 | 6.5 | unchanged |
| JPM | 62→**65** | 3 | 7.5 | endpoint-recession term aligned with banks |
| DHI | 62 | 1 | 9.5 | unchanged |
| BANF | 40 | 2 | 5.0 | unchanged |
| PGR | 37 | 1 | 8.3 | unchanged |

**Passing all three tests:** none. The highest P2 is 85% (ADBE, CPAY, TRU). Each has one credible disruption threat or a cyclical/leverage threat, so none clears the ≥90% anchor. The highest P3 is 37% (ADBE).
**Near-misses** (P2 ≥85% or P3 ≥45%; no name passes 2 of 3): **ADBE** (85/37), **CPAY** (85/30), **TRU** (85/25).
Files: `_results_final.jsonl` (42 lines, with tests_passed, near_miss and calibration_note). The changed .md files have an updated RESULT line and a `## Calibration note` section.
