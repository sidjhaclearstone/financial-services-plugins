#!/usr/bin/env python3
"""Stage 1b (v2 re-run) of the Buffett-style screen: WIDER Test 1.

Test 1 v2: PASS if (0 < NTM P/E < 18) OR (FCF yield >= 6%).
Only names NOT already a Stage 1 PASS (data/stage1_universe.csv) are processed here.

Inputs (data/):
  v2_candidates.json               ticker -> {name, fsym_id, routes}  (screens a/b/c union, minus v1 PASS)
  raw/v2_ntm_eps.txt               FactSet EstimatesConsensus NTMA EPS
  raw/v2_ntm_fcfps.txt             FactSet EstimatesConsensus NTMA FCFPS
  raw/v2_ntm_ffo.txt               FactSet EstimatesConsensus NTMA FFO
  raw/v2_px_*.txt                  FactSet GlobalPrices close (19-Oct-2026; 16-Oct retry)
  raw/v2_fund_cf_c*.txt            FactSet Fundamentals ANN FF_OPER_CF, FF_CAPEX, FF_COM_SHS_OUT_EPS_DIL
  raw/v2_fund_genind_c*.txt        FactSet Fundamentals FF_GEN_IND (01 Ind, 02 Util, 03 Transp, 04 Bank, 05 Ins, 06 Oth Fin)
  raw/v2_rbics_reit_screen.txt     FactSet RBICS 'REIT' industry-group screen (US, primary, >$1bn)
  reits.json                       v1 REIT list
  stage1_universe.csv              v1 output (for column order and v1 status)
Outputs (data/):
  stage1b_universe.csv, stage1b_summary.json, v2_new_passes.txt
"""
import csv
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stage1_build import load_rows, num  # reuse v1 parsers

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(BASE, "data")
R = os.path.join(D, "raw")

PE_MAX, PE_NEAR = 18.0, 19.0
FCF_MIN, FCF_NEAR = 0.06, 0.055
GEN_IND = {"01": "Industrial", "02": "Utility", "03": "Transportation",
           "04": "Bank", "05": "Insurance", "06": "Other Financial"}
REIT_WORDS = ("REIT", "Realty", "Properties", "Property", "Trust", "Residential")


def by_id(path):
    return {r["requestId"]: r for r in load_rows(path)}


def main():
    cands = json.load(open(os.path.join(D, "v2_candidates.json")))
    v1 = {r["ticker"]: r for r in csv.DictReader(open(os.path.join(D, "stage1_universe.csv")))}
    v1_cols = list(next(iter(v1.values())).keys())

    eps = by_id(os.path.join(R, "v2_ntm_eps.txt"))
    fcfps = by_id(os.path.join(R, "v2_ntm_fcfps.txt"))
    ffo = by_id(os.path.join(R, "v2_ntm_ffo.txt"))

    px = {}
    for p in sorted(glob.glob(os.path.join(R, "v2_px_*.txt"))):
        for r in load_rows(p):
            t, v, dt = r.get("requestId"), num(r.get("price")), r.get("date")
            if t is None or v is None or dt is None:
                continue
            if t not in px or dt > px[t][1]:
                px[t] = (v, dt)

    # latest FY with CFO, capex and diluted shares all present
    cf = {}
    for p in sorted(glob.glob(os.path.join(R, "v2_fund_cf_c*.txt"))):
        for r in load_rows(p):
            if r.get("value") is None:
                continue
            cf.setdefault(r["requestId"], {}).setdefault(r.get("fiscalEndDate"), {})[r["metric"]] = (
                float(r["value"]), (r.get("audit") or {}).get("card", {}).get("link"))
    gen = {}
    for p in sorted(glob.glob(os.path.join(R, "v2_fund_genind_c*.txt"))):
        for r in load_rows(p):
            if r.get("value") is None:
                continue
            t, fe = r["requestId"], r.get("fiscalEndDate") or ""
            if t not in gen or fe > gen[t][1]:
                gen[t] = (str(r["value"]), fe)

    rbics_reits = set(json.load(open(os.path.join(R, "v2_rbics_reit_screen.txt")))["reits"])
    v1_reits = set(json.load(open(os.path.join(D, "reits.json")))["reits"])

    extra = ["ntm_fcfps", "fcf_yield_ntm", "fcf_yield_ltm", "fcf_yield_used", "fcf_basis",
             "pe_route", "fcf_route", "test1_v2",
             "gen_ind", "ltm_fy_end", "ltm_cfo_musd", "ltm_capex_musd", "ltm_dil_shs_m",
             "screen_routes", "v1_test1"]
    cols = v1_cols + extra
    out = []
    for t in sorted(cands):
        c = cands[t]
        e, f, fc = eps.get(t, {}), ffo.get(t, {}), fcfps.get(t, {})
        g_code = gen.get(t, (None, None))[0]
        g_name = GEN_IND.get(g_code, g_code)
        bank_ins = g_code in ("04", "05")
        e_mean, f_mean, fc_mean = num(e.get("mean")), num(f.get("mean")), num(fc.get("mean"))
        name = c["name"] or ""
        is_reit = (t in rbics_reits or t in v1_reits or
                   (f_mean is not None and g_code == "06" and any(w in name for w in REIT_WORDS)))
        price, pdate = px.get(t, (None, None))
        eps_date = e.get("estimateDate") or "2026-10-19"
        notes = []

        if is_reit and f_mean is not None:
            basis, earn = "FFO", f_mean
            notes.append(f"FactSet EstimatesConsensus NTMA FFO as of {f.get('estimateDate') or eps_date} (REIT: P/E on FFO)")
        else:
            basis, earn = "EPS", e_mean
            if e_mean is not None:
                notes.append(f"FactSet EstimatesConsensus NTMA EPS as of {eps_date}")
            if is_reit:
                notes.append("REIT without FFO consensus; EPS used")
        if price is not None:
            notes.append(f"FactSet GlobalPrices close {pdate}")

        # P/E
        pe = price / earn if (price is not None and earn is not None and earn > 0) else None

        # FCF yields
        y_ntm = fc_mean / price if (price is not None and fc_mean is not None and price > 0) else None
        y_ltm, fy_end, cfo, capex, shs = None, None, None, None, None
        years = cf.get(t, {})
        for fe in sorted((k for k in years if k), reverse=True):
            m = years[fe]
            if all(k in m for k in ("FF_OPER_CF", "FF_CAPEX", "FF_COM_SHS_OUT_EPS_DIL")):
                cfo, capex, shs = m["FF_OPER_CF"][0], m["FF_CAPEX"][0], m["FF_COM_SHS_OUT_EPS_DIL"][0]
                fy_end = fe
                break
        if price is not None and shs and shs > 0 and cfo is not None:
            y_ltm = (cfo - abs(capex)) / (shs * price)
        if y_ntm is not None:
            y_used, fbasis = y_ntm, "NTM consensus FCFPS"
            notes.append("FactSet EstimatesConsensus NTMA FCFPS")
        elif y_ltm is not None:
            y_used, fbasis = y_ltm, "LTM FactSet CFO−capex"
            notes.append(f"FCF yield = FactSet FF_OPER_CF − |FF_CAPEX| FY ending {fy_end} / (FF_COM_SHS_OUT_EPS_DIL × price)")
        else:
            y_used, fbasis = None, ""

        pe_route = pe is not None and 0 < pe < PE_MAX
        # Other Financial (FF_GEN_IND 06) non-REITs = brokers, lenders, asset managers: reported CFO
        # mixes in customer/loan balances, so the LTM CFO-capex fallback is not accepted for them
        oth_fin_ltm = (g_code == "06" and not is_reit and fbasis.startswith("LTM"))
        fcf_ok = y_used is not None and not bank_ins and not oth_fin_ltm
        if oth_fin_ltm:
            notes.append("Other Financial non-REIT: LTM CFO−capex not meaningful, FCF route not applied")
        fcf_route = fcf_ok and y_used >= FCF_MIN
        if bank_ins and y_used is not None:
            notes.append(f"{g_name} (FF_GEN_IND {g_code}): FCF yield not meaningful, P/E route only")

        has_earn = earn is not None
        if price is None or (not has_earn and not fcf_ok):
            test = "MISSING"
            miss = [x for x, v in (("price", price), ("earnings", earn),
                                   ("usable FCF", y_used if fcf_ok else None)) if v is None]
            notes.append("missing " + ", ".join(miss))
        elif pe_route or fcf_route:
            test = "PASS"
        elif (pe is not None and PE_MAX <= pe < PE_NEAR) or (fcf_ok and FCF_NEAR <= y_used < FCF_MIN):
            test = "NEAR_MISS"
        else:
            test = "FAIL"
            if has_earn and earn <= 0:
                notes.append("non-positive NTM earnings")

        # v1 rule (P/E < 15, near-miss 15-16) for the inherited test1 column
        if price is None or earn is None:
            v1t = "MISSING"
        elif earn <= 0:
            v1t = "FAIL"
        else:
            v1t = "PASS" if pe < 15 else ("NEAR_MISS" if pe < 16 else "FAIL")

        rnd = lambda x, n=5: None if x is None else round(x, n)
        out.append({
            "ticker": t, "name": c["name"], "fsym_id": c["fsym_id"],
            "is_reit": is_reit, "price_usd": price, "price_date": pdate,
            "ntm_eps_mean": e_mean, "ntm_eps_median": num(e.get("median")),
            "ntm_eps_std": num(e.get("standardDeviation")), "ntm_eps_high": num(e.get("high")),
            "ntm_eps_low": num(e.get("low")), "ntm_eps_count": e.get("estimateCount"),
            "ntm_ffo_mean": f_mean, "earnings_basis": basis,
            "ntm_pe": rnd(pe, 3), "test1": v1t, "source_note": "; ".join(notes),
            "ntm_fcfps": fc_mean, "fcf_yield_ntm": rnd(y_ntm), "fcf_yield_ltm": rnd(y_ltm),
            "fcf_yield_used": rnd(y_used), "fcf_basis": fbasis,
            "pe_route": "Y" if pe_route else "N", "fcf_route": "Y" if fcf_route else "N",
            "test1_v2": test, "gen_ind": g_name, "ltm_fy_end": fy_end,
            "ltm_cfo_musd": cfo, "ltm_capex_musd": capex, "ltm_dil_shs_m": shs,
            "screen_routes": "+".join(c["routes"]),
            "v1_test1": v1.get(t, {}).get("test1", "not in v1 universe"),
        })

    with open(os.path.join(D, "stage1b_universe.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for r in out:
            w.writerow({k: ("" if v is None else v) for k, v in r.items()})

    P = [r for r in out if r["test1_v2"] == "PASS"]
    cnt = {k: sum(1 for r in out if r["test1_v2"] == k) for k in ("PASS", "NEAR_MISS", "FAIL", "MISSING")}
    summary = {
        "as_of": "2026-10-19",
        "test": "Test 1 v2: PASS if 0<NTM P/E<18 OR FCF yield>=6% (NTM consensus FCFPS/price, else LTM CFO-|capex| / diluted shs x price); "
                "NEAR_MISS 18<=P/E<19 or 5.5%<=FCF yield<6%; banks/insurers P/E route only; REITs P/E on NTM FFO where available",
        "scope": "candidates = union of screens (a) FY2 P/E 0-20, (b) FF_FCF_YLD>=4, (c) FY1 P/FCF 0-25, minus v1 Stage 1 PASS names",
        "candidates": len(out), **cnt,
        "pass_pe_route_only": sum(1 for r in P if r["pe_route"] == "Y" and r["fcf_route"] == "N"),
        "pass_fcf_route_only": sum(1 for r in P if r["pe_route"] == "N" and r["fcf_route"] == "Y"),
        "pass_both_routes": sum(1 for r in P if r["pe_route"] == "Y" and r["fcf_route"] == "Y"),
        "pass_fcf_basis_ntm": sum(1 for r in P if r["fcf_route"] == "Y" and r["fcf_basis"].startswith("NTM")),
        "pass_fcf_basis_ltm": sum(1 for r in P if r["fcf_route"] == "Y" and r["fcf_basis"].startswith("LTM")),
        "fcf_basis_counts": {b: sum(1 for r in out if r["fcf_basis"] == b)
                             for b in ("NTM consensus FCFPS", "LTM FactSet CFO−capex", "")},
        "banks_insurers_fcf_excluded": [r["ticker"] for r in out if r["gen_ind"] in ("Bank", "Insurance")],
        "other_fin_ltm_fcf_excluded": [r["ticker"] for r in out if "Other Financial non-REIT" in r["source_note"]],
        "reit_count": sum(1 for r in out if r["is_reit"]),
        "reits_on_ffo_basis": [r["ticker"] for r in out if r["is_reit"] and r["earnings_basis"] == "FFO"],
        "v1_nonpass_rechecked": {r["ticker"]: r["test1_v2"] for r in out if r["v1_test1"] != "not in v1 universe"},
        "non_latest_price_date": {r["ticker"]: r["price_date"] for r in out
                                  if r["price_date"] and r["price_date"] != "2026-10-19"},
        "missing_tickers": [r["ticker"] for r in out if r["test1_v2"] == "MISSING"],
        "near_miss_tickers": [r["ticker"] for r in out if r["test1_v2"] == "NEAR_MISS"],
    }
    json.dump(summary, open(os.path.join(D, "stage1b_summary.json"), "w"), indent=1, ensure_ascii=False)
    with open(os.path.join(D, "v2_new_passes.txt"), "w") as fh:
        fh.write("\n".join(r["ticker"] for r in P) + "\n")
    print(f"candidates={len(out)} PASS={cnt['PASS']} (PE-only {summary['pass_pe_route_only']}, "
          f"FCF-only {summary['pass_fcf_route_only']}, both {summary['pass_both_routes']}) "
          f"NEAR_MISS={cnt['NEAR_MISS']} FAIL={cnt['FAIL']} MISSING={cnt['MISSING']}")


if __name__ == "__main__":
    main()
