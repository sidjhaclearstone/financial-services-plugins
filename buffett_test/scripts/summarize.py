"""Compute compact Buffett-triage stats for tickers from data/<T>.json (+ data/consensus.json, data/stage1_universe.csv).
Usage: python3 scripts/summarize.py BANF-US MZTI-US ...   -> writes data/<T>_summary.json and prints a compact block per ticker."""
import json, os, sys, csv, math
sys.path.insert(0, os.path.dirname(__file__))
from fsload import tkey
BASE = os.path.join(os.path.dirname(__file__), '..', 'data')

def series(d, m):
    s = d.get('fundamentals', {}).get(m, {})
    return {int(y): v['v'] for y, v in s.items() if v.get('v') is not None}

def cagr(a, b, n):
    if a is None or b is None or n <= 0 or a <= 0 or b <= 0: return None
    return (b / a) ** (1 / n) - 1

def pct(x): return None if x is None else round(100 * x, 1)

def load_stage1():
    out = {}
    for fn in ('stage1_universe.csv', 'stage1b_universe.csv'):   # v2 file adds 15-18x and FCF-yield passes
        p = os.path.join(BASE, fn)
        if os.path.exists(p):
            for r in csv.DictReader(open(p)):
                if fn == 'stage1_universe.csv' or r['ticker'] not in out or out[r['ticker']].get('test1') != 'PASS':
                    out[r['ticker']] = r
    return out

def load_cons():
    p = os.path.join(BASE, 'consensus.json')
    return json.load(open(p)) if os.path.exists(p) else {}

def summarize(t, s1, cons):
    d = json.load(open(os.path.join(BASE, tkey(t) + '.json')))
    eps = series(d, 'FF_EPS_DIL'); rev = series(d, 'FF_SALES'); ebit = series(d, 'FF_EBIT_OPER')
    ni = series(d, 'FF_NET_INC'); fcf = series(d, 'FF_FREE_CF'); sh = series(d, 'FF_COM_SHS_OUT_EPS_DIL')
    # FactSet FF_FREE_CF is AFTER dividends (OCF - capex - cash divs); use OCF - |capex| where available (FMP freeCashFlow is already pre-dividend)
    ocf = series(d, 'FF_OPER_CF'); cpx = series(d, 'FF_CAPEX')
    fcf.update({y: ocf[y] - abs(cpx[y]) for y in ocf if y in cpx})
    mgn = series(d, 'FF_EBIT_OPER_MGN'); roic = series(d, 'FF_ROIC'); roe = series(d, 'FF_ROE')
    nd = series(d, 'FF_NET_DEBT'); ebitda = series(d, 'FF_EBITDA_OPER'); acq = series(d, 'FF_ACQ_BUS_CF')
    bb = series(d, 'FF_STK_PURCH_CF'); dv = series(d, 'FF_DIV_CF'); epsx = series(d, 'FF_EPS_DIL_BEF_UNUSUAL')
    adj = {int(y): v['v'] for y, v in d.get('adj_eps_actual', {}).items() if v.get('v') is not None}
    yrs = sorted(set(eps) | set(adj))
    last = max(yrs) if yrs else None
    def ser_cagr(s, n):
        if not s: return None
        L = max(s); F = L - n
        return cagr(s.get(F), s.get(L), n) if F in s else None
    def growth_years(s):
        ys = sorted(s); g = []
        for y in ys:
            if y - 1 in s and s[y - 1] and s[y - 1] > 0:
                g.append((y, s[y] / s[y - 1] - 1))
        g = g[-10:]
        return sum(1 for _, x in g if x >= 0.07), len(g), g
    base = adj if len(adj) >= 6 else eps
    basis = 'adjusted (FactSet actuals)' if base is adj else 'GAAP diluted'
    n7, nobs, g = growth_years(base)
    worst = min(g, key=lambda x: x[1]) if g else None
    o = {'ticker': t, 'name': d.get('name') or d.get('entity', {}).get('name'), 'last_fy': last,
         'rbics': ' / '.join(filter(None, [d.get('entity', {}).get(k) for k in ('rbics_sector', 'rbics_subsector', 'rbics_indgrp')])),
         'mkt_cap_usd_m': d.get('market_value_usd_m'),
         'eps_basis_for_growth': basis,
         'eps_cagr_10y': pct(ser_cagr(base, 10)), 'eps_cagr_5y': pct(ser_cagr(base, 5)),
         'gaap_eps_cagr_10y': pct(ser_cagr(eps, 10)),
         'rev_cagr_10y': pct(ser_cagr(rev, 10)), 'rev_cagr_5y': pct(ser_cagr(rev, 5)),
         'shares_cagr_10y': pct(ser_cagr(sh, 10)),
         'years_eps_growth_ge7': f'{n7}/{nobs}', 'worst_eps_year': (worst[0], pct(worst[1])) if worst else None,
         'eps_series': {y: round(base[y], 2) for y in sorted(base)[-11:]},
         'gaap_eps_series': {y: round(eps[y], 2) for y in sorted(eps)[-11:]},
         'rev_series_m': {y: round(rev[y]) for y in sorted(rev)[-11:]},
         'ebit_margin_series': {y: round(mgn[y], 1) for y in sorted(mgn)[-11:]}}
    if mgn:
        ms = [mgn[y] for y in sorted(mgn)[-11:]]; lm = mgn[max(mgn)]
        o['ebit_margin_latest'] = round(lm, 1); o['ebit_margin_10y_avg'] = round(sum(ms) / len(ms), 1)
        o['ebit_margin_10y_max'] = round(max(ms), 1); o['ebit_margin_10y_min'] = round(min(ms), 1)
        o['margin_pctile_in_history'] = round(100 * sum(1 for x in ms if x <= lm) / len(ms))
    if base:
        bl = base[max(base)]; bmax = max(base[y] for y in sorted(base)[-11:])
        o['latest_eps_vs_10y_max'] = round(bl / bmax, 2) if bmax > 0 else None
    def ratio_sum(a, b, n=10):
        ys = [y for y in sorted(b)[-n:] if y in a]
        sa = sum(a[y] for y in ys); sb = sum(b[y] for y in ys)
        return round(sa / sb, 2) if sb and sb > 0 else None
    o['fcf_conversion_5y'] = ratio_sum(fcf, ni, 5); o['fcf_conversion_10y'] = ratio_sum(fcf, ni, 10)
    o['acq_to_fcf_10y'] = ratio_sum({y: abs(v) for y, v in acq.items()}, fcf, 10)
    o['buyback_to_fcf_10y'] = ratio_sum({y: abs(v) for y, v in bb.items()}, fcf, 10)
    o['div_to_fcf_10y'] = ratio_sum({y: abs(v) for y, v in dv.items()}, fcf, 10)
    if nd and ebitda:
        L = max(nd); o['net_debt_m'] = round(nd[L]); o['net_debt_ebitda'] = round(nd[L] / ebitda[L], 2) if ebitda.get(L) else None
    if roic: o['roic_latest'] = round(roic[max(roic)], 1); o['roic_10y_avg'] = round(sum(roic[y] for y in sorted(roic)[-10:]) / len(sorted(roic)[-10:]), 1)
    if roe: o['roe_latest'] = round(roe[max(roe)], 1); o['roe_10y_avg'] = round(sum(roe[y] for y in sorted(roe)[-10:]) / len(sorted(roe)[-10:]), 1)
    if adj and eps:
        common = [y for y in sorted(adj) if y in eps][-5:]
        gaps = [(adj[y] / eps[y] - 1) for y in common if eps[y] and eps[y] > 0]
        o['adj_vs_gaap_gap_5y_avg_pct'] = pct(sum(gaps) / len(gaps)) if gaps else None
        o['adj_vs_gaap_gap_latest_pct'] = pct(adj[common[-1]] / eps[common[-1]] - 1) if common and eps[common[-1]] and eps[common[-1]] > 0 else None
    r1 = s1.get(t, {})
    o['ntm_pe'] = round(float(r1['ntm_pe']), 2) if r1.get('ntm_pe') not in (None, '') else None
    o['is_reit'] = r1.get('is_reit'); o['price'] = r1.get('price_usd')
    if r1.get('fcf_yield_used') not in (None, ''):
        o['fcf_yield'] = round(100 * float(r1['fcf_yield_used']), 1); o['test1_route'] = ('PE' if r1.get('pe_route') == 'Y' else '') + ('+FCF' if r1.get('fcf_route') == 'Y' else '')
    c = cons.get(t, {})
    for m in ('EPS', 'SALES', 'FFO'):
        cm = c.get(m)
        if not cm: continue
        row = {}
        for rel in ('0', '1', '2', '3'):
            x = cm.get(rel)
            if x: row[f'FY{rel}'] = {'fy': x.get('fiscalYear'), 'mean': None if x.get('mean') is None else round(x['mean'], 3), 'std': None if x.get('standardDeviation') is None else round(x['standardDeviation'], 3), 'hi': x.get('high'), 'lo': x.get('low'), 'n': x.get('estimateCount')}
        o[f'cons_{m}'] = row
        try:
            g12 = cm['2']['mean'] / cm['1']['mean'] - 1; g23 = cm['3']['mean'] / cm['2']['mean'] - 1
            o[f'cons_{m}_growth_FY2_FY3'] = (pct(g12), pct(g23))
            if '0' in cm and cm['0'].get('mean'): o[f'cons_{m}_growth_FY1'] = pct(cm['1']['mean'] / cm['0']['mean'] - 1)
        except Exception: pass
    if c.get('EPS_LTG'): o['eps_ltg'] = c['EPS_LTG'].get('mean')
    o['missing'] = d.get('missing', []); o['fmp_backup'] = list(d.get('fmp_backup', {}).keys())
    json.dump(o, open(os.path.join(BASE, tkey(t) + '_summary.json'), 'w'), indent=0)
    return o

def compact(o):
    keys = ['ntm_pe', 'fcf_yield', 'test1_route', 'mkt_cap_usd_m', 'is_reit', 'eps_basis_for_growth', 'eps_cagr_10y', 'eps_cagr_5y', 'rev_cagr_10y', 'shares_cagr_10y', 'years_eps_growth_ge7', 'worst_eps_year', 'latest_eps_vs_10y_max', 'ebit_margin_latest', 'ebit_margin_10y_avg', 'ebit_margin_10y_max', 'margin_pctile_in_history', 'fcf_conversion_10y', 'acq_to_fcf_10y', 'buyback_to_fcf_10y', 'net_debt_ebitda', 'roic_10y_avg', 'roe_10y_avg', 'adj_vs_gaap_gap_5y_avg_pct', 'cons_EPS_growth_FY1', 'cons_EPS_growth_FY2_FY3', 'eps_ltg']
    s = f"## {o['ticker']} | {o.get('name')} | {o.get('rbics')}\n"
    s += '; '.join(f'{k}={o.get(k)}' for k in keys if o.get(k) is not None) + '\n'
    s += f"EPS: {o['eps_series']}\n"
    if o.get('ebit_margin_series'): s += f"EBITm: {o['ebit_margin_series']}\n"
    return s

if __name__ == '__main__':
    s1 = load_stage1(); cons = load_cons()
    for t in sys.argv[1:]:
        try: print(compact(summarize(t, s1, cons)))
        except Exception as e: print(f'## {t} SUMMARY ERROR: {e}')
