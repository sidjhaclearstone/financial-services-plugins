#!/usr/bin/env python3
"""Stage 1 (universe + Test 1) of the Buffett-style screen for EUROPE and INDIA.

Same logic as the US v2 run (scripts/stage1b_build.py, assumptions A23-A32), adapted:
  Test 1 PASS if FCF route (FCF yield >= 6%) OR P/E route (0 < NTM P/E < 15).
  phase = "1" if FCF route, "2" if P/E route only.
  NEAR_MISS: not PASS and (5.5% <= FCF yield < 6% on an eligible basis, or 15 <= P/E < 16).
  MISSING: no price, or no NTM earnings and no eligible FCF yield.
  Banks/insurers (FF_GEN_IND 04/05): P/E route only.
  Other Financial (06) non-REITs and REITs: FCF route only on NTM consensus FCFPS (no LTM fallback).
  REITs: P/E on NTM FFO where available.

Inputs (intl/data/):
  candidates.csv                    union of prefilter screens (a) P/FCF FY1 0-25, (b) FF_FCF_YLD>=4, (c) P/E FY2 0-17
  raw/s1_*_screen_*.txt             FactSet CompanyScreener pages (base-universe totals in the 'meta' block)
  raw/s1_ntm_eps_c*.txt             FactSet EstimatesConsensus NTMA EPS (USD)
  raw/s1_ntm_fcfps_c*.txt           FactSet EstimatesConsensus NTMA FCFPS (USD)
  raw/s1_ntm_ffo.txt                FactSet EstimatesConsensus NTMA FFO (USD), REIT-like names only
  raw/s1_px_*.txt                   FactSet GlobalPrices close USD (19-Oct-2026; 16-Oct retry)
  raw/s1_fund_cf_c*.txt             FactSet Fundamentals ANN FF_OPER_CF, FF_CAPEX, FF_COM_SHS_OUT_EPS_DIL (USD)
  raw/s1_fund_genind_c*.txt         FactSet Fundamentals FF_GEN_IND
  raw/s1_entity_c*.txt              FactSet EntityReference (HQ country, RBICS)
Outputs (intl/data/):
  stage1_universe.csv, entity_info.csv, stage1_summary.json,
  phase1_passes.txt, phase2_passes.txt, test1_passes.txt
"""
import csv
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stage1_build import load_rows, num  # reuse v1 parsers

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "intl")
D = os.path.join(BASE, "data")
R = os.path.join(D, "raw")

AS_OF = "2026-10-19"
PE_MAX, PE_NEAR = 15.0, 16.0
FCF_MIN, FCF_NEAR = 0.06, 0.055
GEN_IND = {"01": "Industrial", "02": "Utility", "03": "Transportation",
           "04": "Bank", "05": "Insurance", "06": "Other Financial"}
REIT_GROUPS = ("Equity REITs", "Mortgage REITs", "Property Owners")
BASE_UNIVERSE = {"Europe": 1544, "India": 534}  # CompanyScreener limit-1 'total', base criteria only
COLS = ["ticker", "name", "fsym_id", "region", "country", "is_reit", "price_usd", "price_date",
        "ntm_eps_mean", "ntm_eps_std", "ntm_eps_count", "ntm_ffo_mean", "earnings_basis", "ntm_pe",
        "ntm_fcfps", "fcf_yield_ntm", "fcf_yield_ltm", "fcf_yield_used", "fcf_basis", "gen_ind",
        "fcf_route", "pe_route", "phase", "test1", "source_note"]


def by_id(pattern):
    out = {}
    for p in sorted(glob.glob(os.path.join(R, pattern))):
        for r in load_rows(p):
            if r.get("requestId"):
                out[r["requestId"]] = r
    return out


def main():
    cands = list(csv.DictReader(open(os.path.join(D, "candidates.csv"))))

    eps = by_id("s1_ntm_eps_c*.txt")
    fcfps = by_id("s1_ntm_fcfps_c*.txt")
    ffo = by_id("s1_ntm_ffo.txt")

    px = {}
    for p in sorted(glob.glob(os.path.join(R, "s1_px_*.txt"))):
        for r in load_rows(p):
            t, v, dt = r.get("requestId"), num(r.get("price")), r.get("date")
            if t is None or v is None or dt is None or dt > AS_OF:
                continue
            if t not in px or dt > px[t][1]:
                px[t] = (v, dt)

    cf = {}
    for p in sorted(glob.glob(os.path.join(R, "s1_fund_cf_c*.txt"))):
        for r in load_rows(p):
            if r.get("value") is None:
                continue
            cf.setdefault(r["requestId"], {}).setdefault(r.get("fiscalEndDate"), {})[r["metric"]] = float(r["value"])
    gen = {}
    for p in sorted(glob.glob(os.path.join(R, "s1_fund_genind_c*.txt"))):
        for r in load_rows(p):
            if r.get("value") is None:
                continue
            t, fe = r["requestId"], r.get("fiscalEndDate") or ""
            if t not in gen or fe > gen[t][1]:
                gen[t] = (str(r["value"]), fe)

    ent = {}
    for p in sorted(glob.glob(os.path.join(R, "s1_entity_c*.txt"))):
        for r in load_rows(p):
            ent[r["requestId"]] = r
    with open(os.path.join(D, "entity_info.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["ticker", "entity_name", "hq_country", "incorporation_country", "country_of_risk",
                    "rbics_economy", "rbics_sector", "rbics_subsector", "rbics_industry_group",
                    "ultimate_parent", "website"])
        for c in cands:
            e = ent.get(c["ticker"], {})
            w.writerow([c["ticker"], e.get("entityProperName"), e.get("headquartersCountry"),
                        e.get("incorporationCountry"), e.get("countryOfRisk"), e.get("rbicsEconomyClassification"),
                        e.get("rbicsSectorClassification"), e.get("rbicsSubsectorClassification"),
                        e.get("rbicsIndustryGroupClassification"), e.get("ultimateParentName"), e.get("website")])

    cand_entities = {ent[c["ticker"]]["fsymEntityId"]: c["ticker"] for c in cands
                     if c["ticker"] in ent and ent[c["ticker"]].get("fsymEntityId")}

    out = []
    for c in cands:
        t = c["ticker"]
        e_ = ent.get(t, {})
        e, f, fc = eps.get(t, {}), ffo.get(t, {}), fcfps.get(t, {})
        g_code = gen.get(t, (None, None))[0]
        g_name = GEN_IND.get(g_code, g_code or "")
        bank_ins = g_code in ("04", "05")
        e_mean, f_mean, fc_mean = num(e.get("mean")), num(f.get("mean")), num(fc.get("mean"))
        ig = e_.get("rbicsIndustryGroupClassification") or ""
        is_reit = ig in REIT_GROUPS
        price, pdate = px.get(t, (None, None))
        est_date = e.get("estimateDate") or fc.get("estimateDate") or ""
        notes = []

        if is_reit and f_mean is not None:
            basis, earn = "FFO", f_mean
            notes.append(f"FactSet EstimatesConsensus NTMA FFO as of {f.get('estimateDate') or est_date} (REIT-like, RBICS '{ig}': P/E on FFO)")
        else:
            basis, earn = "EPS", e_mean
            if e_mean is not None:
                notes.append(f"FactSet EstimatesConsensus NTMA EPS as of {est_date}")
            if is_reit:
                notes.append(f"REIT-like (RBICS '{ig}') without FFO consensus; EPS used")
        if price is not None:
            notes.append(f"FactSet GlobalPrices close {pdate} (USD)")

        pe = price / earn if (price is not None and earn is not None and earn > 0) else None

        y_ntm = fc_mean / price if (price is not None and fc_mean is not None and price > 0) else None
        y_ltm, fy_end = None, None
        years = cf.get(t, {})
        for fe in sorted((k for k in years if k), reverse=True):
            m = years[fe]
            if all(k in m for k in ("FF_OPER_CF", "FF_CAPEX", "FF_COM_SHS_OUT_EPS_DIL")):
                cfo, capex, shs = m["FF_OPER_CF"], m["FF_CAPEX"], m["FF_COM_SHS_OUT_EPS_DIL"]
                if price is not None and shs and shs > 0:
                    y_ltm, fy_end = (cfo - abs(capex)) / (shs * price), fe
                break
        if y_ntm is not None:
            y_used, fbasis = y_ntm, "NTM consensus FCFPS"
            notes.append("FactSet EstimatesConsensus NTMA FCFPS")
        elif y_ltm is not None:
            y_used, fbasis = y_ltm, "LTM FactSet CFO-capex"
            notes.append(f"FCF yield = FactSet FF_OPER_CF - |FF_CAPEX| FY ending {fy_end} / (FF_COM_SHS_OUT_EPS_DIL x price)")
        else:
            y_used, fbasis = None, ""

        ntm_only = (g_code == "06" or is_reit)
        ltm_blocked = ntm_only and fbasis.startswith("LTM")
        fcf_ok = y_used is not None and not bank_ins and not ltm_blocked
        if ltm_blocked:
            notes.append(("REIT-like" if is_reit else "Other Financial non-REIT") +
                         ": LTM CFO-capex not accepted, FCF route not applied")
        if bank_ins and y_used is not None:
            notes.append(f"{g_name} (FF_GEN_IND {g_code}): FCF yield not meaningful, P/E route only")

        fcf_route = fcf_ok and y_used >= FCF_MIN
        pe_route = pe is not None and 0 < pe < PE_MAX
        phase = "1" if fcf_route else ("2" if pe_route else "")

        has_earn = earn is not None
        if price is None or (not has_earn and not fcf_ok):
            test = "MISSING"
            miss = [x for x, v in (("price", price), ("earnings", earn),
                                   ("usable FCF", y_used if fcf_ok else None)) if v is None]
            notes.append("missing " + ", ".join(miss))
            phase = ""
        elif phase:
            test = "PASS"
        elif (pe is not None and PE_MAX <= pe < PE_NEAR) or (fcf_ok and FCF_NEAR <= y_used < FCF_MIN):
            test = "NEAR_MISS"
        else:
            test = "FAIL"
            if has_earn and earn <= 0:
                notes.append("non-positive NTM earnings")

        if fcf_ok and y_used is not None and y_used > 0.25:
            notes.append("CHECK: FCF yield >25%, verify data")
        if pe is not None and pe < 4:
            notes.append("CHECK: P/E <4x, verify data")
        upid = e_.get("ultimateParentId")
        if upid and upid != e_.get("fsymEntityId") and upid in cand_entities:
            notes.append(f"subsidiary of listed {e_.get('ultimateParentName')} ({cand_entities[upid]}) - low free float")
        if t[:1].isdigit() and t.endswith("-BE"):
            notes.append("Euronext Brussels Expert Market line (illiquid, unlisted-style)")
        tk_cty = t.rsplit("-", 1)[-1]
        hq = e_.get("headquartersCountry") or ""
        if tk_cty not in (hq, "UK" if hq == "GB" else hq) and not (tk_cty == "GB" and hq in ("JE", "GG", "IM")):
            notes.append(f"primary listing {tk_cty}, HQ {hq}")

        rnd = lambda x, n=5: None if x is None else round(x, n)
        out.append({
            "ticker": t, "name": c["name"], "fsym_id": c["fsym_id"], "region": c["region"],
            "country": hq, "is_reit": is_reit, "price_usd": price, "price_date": pdate,
            "ntm_eps_mean": e_mean, "ntm_eps_std": num(e.get("standardDeviation")),
            "ntm_eps_count": e.get("estimateCount"), "ntm_ffo_mean": f_mean, "earnings_basis": basis,
            "ntm_pe": rnd(pe, 3), "ntm_fcfps": fc_mean, "fcf_yield_ntm": rnd(y_ntm),
            "fcf_yield_ltm": rnd(y_ltm), "fcf_yield_used": rnd(y_used), "fcf_basis": fbasis,
            "gen_ind": g_name, "fcf_route": "Y" if fcf_route else "N", "pe_route": "Y" if pe_route else "N",
            "phase": phase, "test1": test, "source_note": "; ".join(notes),
        })

    with open(os.path.join(D, "stage1_universe.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        for r in out:
            w.writerow({k: ("" if r[k] is None else r[k]) for k in COLS})

    def stats(rows, region=None):
        P = [r for r in rows if r["test1"] == "PASS"]
        p2 = [r for r in P if r["phase"] == "2"]
        return {
            "base_universe": BASE_UNIVERSE.get(region, sum(BASE_UNIVERSE.values())),
            "candidates": len(rows),
            "PASS": len(P),
            "phase1": sum(1 for r in P if r["phase"] == "1"),
            "phase2": len(p2),
            "both_routes": sum(1 for r in P if r["fcf_route"] == "Y" and r["pe_route"] == "Y"),
            "phase1_fcf_basis_ntm": sum(1 for r in P if r["phase"] == "1" and r["fcf_basis"].startswith("NTM")),
            "phase1_fcf_basis_ltm": sum(1 for r in P if r["phase"] == "1" and r["fcf_basis"].startswith("LTM")),
            "near_miss": sum(1 for r in rows if r["test1"] == "NEAR_MISS"),
            "fail": sum(1 for r in rows if r["test1"] == "FAIL"),
            "missing": sum(1 for r in rows if r["test1"] == "MISSING"),
            "banks_insurers_in_phase2": sum(1 for r in p2 if r["gen_ind"] in ("Bank", "Insurance")),
            "reits_flagged": sum(1 for r in rows if r["is_reit"]),
            "reits_pass": sum(1 for r in P if r["is_reit"]),
        }

    regions = ("Europe", "India")
    summary = {
        "as_of": AS_OF,
        "test": "Test 1: PASS if FCF yield >=6% (Phase 1; NTM consensus FCFPS/price, else LTM (CFO-|capex|)/(diluted shs x price); "
                "banks/insurers excluded; Other Financial & REITs NTM basis only) or 0<NTM P/E<15 (Phase 2; REITs on FFO). "
                "NEAR_MISS 15<=P/E<16 or 5.5%<=eligible FCF yield<6%.",
        "prefilters": "(a) FE_VALUATION_MCAP_FCF_MEAN FY1 0-25, (b) FF_FCF_YLD>=4, (c) FE_VALUATION_PE_MEAN FY2 0-17; "
                      "base = FactSet HQ country in region, ISON_SECONDARY=0, FF_MKT_VAL>$1bn (USD)",
        **{reg: stats([r for r in out if r["region"] == reg], reg) for reg in regions},
        "total": stats(out),
        "non_latest_price_date": {r["ticker"]: r["price_date"] for r in out if r["price_date"] and r["price_date"] != AS_OF},
        "missing_tickers": [r["ticker"] for r in out if r["test1"] == "MISSING"],
        "near_miss_tickers": [r["ticker"] for r in out if r["test1"] == "NEAR_MISS"],
        "check_flags": [r["ticker"] for r in out if "CHECK:" in r["source_note"] and r["test1"] == "PASS"],
    }
    json.dump(summary, open(os.path.join(D, "stage1_summary.json"), "w"), indent=1, ensure_ascii=False)

    def ordered(phase):
        lst = []
        for reg in regions:
            rows = [r for r in out if r["region"] == reg and r["test1"] == "PASS" and r["phase"] == phase]
            if phase == "1":
                rows.sort(key=lambda r: -r["fcf_yield_used"])
            else:
                rows.sort(key=lambda r: r["ntm_pe"])
            lst += [r["ticker"] for r in rows]
        return lst

    p1, p2 = ordered("1"), ordered("2")
    for fn, lst in (("phase1_passes.txt", p1), ("phase2_passes.txt", p2), ("test1_passes.txt", p1 + p2)):
        with open(os.path.join(D, fn), "w") as fh:
            fh.write("\n".join(lst) + "\n")
    for reg in regions + ("total",):
        s = summary[reg]
        print(f"{reg}: base {s['base_universe']} cand {s['candidates']} PASS {s['PASS']} (P1 {s['phase1']}, P2 {s['phase2']}, both {s['both_routes']}) "
              f"NEAR {s['near_miss']} FAIL {s['fail']} MISSING {s['missing']} bank/ins P2 {s['banks_insurers_in_phase2']}")


if __name__ == "__main__":
    main()
