#!/usr/bin/env python3
"""Stage 1 of the Buffett-style screen: NTM P/E test (< 15x).

Inputs (data/):
  universe_screen.json            ticker, name, fsym_id
  _ntm_eps_raw.txt                FactSet EstimatesConsensus NTMA EPS
  _ntm_ffo_raw.txt                FactSet EstimatesConsensus NTMA FFO
  _px_raw_1.txt, _px_raw_2.txt    FactSet GlobalPrices close 2026-10-19
  _px_raw_retry*.txt              optional FactSet price retries
  _fmp_backup.json                optional FMP fallback {ticker: {price, price_date, ntm_eps, note}}
  reits.json                      REIT list
Outputs (data/):
  stage1_universe.csv, stage1_summary.json, test1_passes.txt
"""
import csv
import glob
import json
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(BASE, "data")


def load_rows(path):
    """Parse a raw tool result: {"data":[...]}, [...], or [{"type":"text","text":"<json>"}]."""
    with open(path) as f:
        obj = json.load(f)
    rows = []

    def walk(o):
        if isinstance(o, dict):
            if "data" in o and isinstance(o["data"], list):
                rows.extend(o["data"])
            elif o.get("type") == "text" and "text" in o:
                walk(json.loads(o["text"]))
            elif "requestId" in o:
                rows.append(o)
        elif isinstance(o, list):
            for x in o:
                walk(x)

    walk(obj)
    return rows


def num(x):
    try:
        return None if x is None else float(x)
    except (TypeError, ValueError):
        return None


def main():
    uni = json.load(open(os.path.join(D, "universe_screen.json")))["universe"]
    eps = {r["requestId"]: r for r in load_rows(os.path.join(D, "_ntm_eps_raw.txt"))}
    ffo = {r["requestId"]: r for r in load_rows(os.path.join(D, "_ntm_ffo_raw.txt"))}

    # latest available close per id across all price files
    px = {}
    px_files = sorted(glob.glob(os.path.join(D, "_px_raw_*.txt")))
    for p in px_files:
        for r in load_rows(p):
            t, v, dt = r.get("requestId"), num(r.get("price")), r.get("date")
            if t is None or v is None or dt is None:
                continue
            if t not in px or dt > px[t][1]:
                px[t] = (v, dt)

    reits = set(json.load(open(os.path.join(D, "reits.json")))["reits"])
    fmp_path = os.path.join(D, "_fmp_backup.json")
    fmp = json.load(open(fmp_path)) if os.path.exists(fmp_path) else {}

    cols = ["ticker", "name", "fsym_id", "is_reit", "price_usd", "price_date",
            "ntm_eps_mean", "ntm_eps_median", "ntm_eps_std", "ntm_eps_high", "ntm_eps_low",
            "ntm_eps_count", "ntm_ffo_mean", "earnings_basis", "ntm_pe", "test1", "source_note"]
    out = []
    for u in uni:
        t = u["ticker"]
        e = eps.get(t, {})
        f = ffo.get(t, {})
        is_reit = t in reits
        price, pdate = px.get(t, (None, None))
        e_mean = num(e.get("mean"))
        f_mean = num(f.get("mean"))
        eps_date = e.get("estimateDate") or "2026-10-19"
        notes = []
        if is_reit and f_mean is not None:
            basis, earn = "FFO", f_mean
            notes.append(f"FactSet EstimatesConsensus NTMA FFO as of {f.get('estimateDate') or eps_date}")
        else:
            basis, earn = "EPS", e_mean
            if e_mean is not None:
                notes.append(f"FactSet EstimatesConsensus NTMA EPS as of {eps_date}")
            if is_reit:
                notes.append("REIT without FFO consensus; EPS used")
        if price is not None:
            notes.append(f"FactSet GlobalPrices close {pdate}")

        # FMP backup for missing pieces
        b = fmp.get(t)
        if b and (price is None or earn is None):
            if price is None and num(b.get("price")) is not None:
                price, pdate = num(b["price"]), b.get("price_date")
                notes.append(f"FMP backup price {pdate}")
            if earn is None and num(b.get("ntm_eps")) is not None:
                basis, earn = "EPS", num(b["ntm_eps"])
                e_mean = earn
                notes.append("FMP backup NTM EPS (" + b.get("note", "FY1/FY2 time-weighted") + ")")

        if price is None or earn is None:
            pe, test = None, "MISSING"
            notes.append("missing " + ", ".join(x for x, v in (("price", price), ("earnings", earn)) if v is None))
        elif earn <= 0:
            pe, test = None, "FAIL"
            notes.append("non-positive NTM earnings")
        else:
            pe = price / earn
            test = "PASS" if pe < 15 else ("NEAR_MISS" if pe < 16 else "FAIL")

        out.append({
            "ticker": t, "name": u.get("name"), "fsym_id": u.get("fsym_id"),
            "is_reit": is_reit, "price_usd": price, "price_date": pdate,
            "ntm_eps_mean": e_mean, "ntm_eps_median": num(e.get("median")),
            "ntm_eps_std": num(e.get("standardDeviation")), "ntm_eps_high": num(e.get("high")),
            "ntm_eps_low": num(e.get("low")), "ntm_eps_count": e.get("estimateCount"),
            "ntm_ffo_mean": f_mean, "earnings_basis": basis,
            "ntm_pe": None if pe is None else round(pe, 3), "test1": test,
            "source_note": "; ".join(notes),
        })

    with open(os.path.join(D, "stage1_universe.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for r in out:
            w.writerow({k: ("" if v is None else v) for k, v in r.items()})

    cnt = {k: sum(1 for r in out if r["test1"] == k) for k in ("PASS", "NEAR_MISS", "FAIL", "MISSING")}
    summary = {
        "as_of": "2026-10-19",
        "test": "NTM P/E < 15 (NEAR_MISS 15-16); REITs on NTM FFO where available",
        "total": len(out), **cnt,
        "reit_count": sum(1 for r in out if r["is_reit"]),
        "reits_on_ffo_basis": [r["ticker"] for r in out if r["is_reit"] and r["earnings_basis"] == "FFO"],
        "fmp_backups": [r["ticker"] for r in out if "FMP backup" in r["source_note"]],
        "non_latest_price_date": {r["ticker"]: r["price_date"] for r in out
                                  if r["price_date"] and r["price_date"] != "2026-10-19"},
        "missing_tickers": [r["ticker"] for r in out if r["test1"] == "MISSING"],
        "near_miss_tickers": [r["ticker"] for r in out if r["test1"] == "NEAR_MISS"],
    }
    json.dump(summary, open(os.path.join(D, "stage1_summary.json"), "w"), indent=1)
    with open(os.path.join(D, "test1_passes.txt"), "w") as fh:
        fh.write("\n".join(r["ticker"] for r in out if r["test1"] == "PASS") + "\n")
    print(f"PASS={cnt['PASS']} NEAR_MISS={cnt['NEAR_MISS']} FAIL={cnt['FAIL']} MISSING={cnt['MISSING']} "
          f"REITs={summary['reit_count']} FMP={len(summary['fmp_backups'])}")


if __name__ == "__main__":
    main()
