"""Merge raw FactSet results for a batch into data/<TICKER>.json.
Usage: python3 scripts/ingest_batch.py --fund F1 [--fund F2 ...] [--entity F] [--surprise F] [--mv F] [--fmp TICKER:KIND:FILE ...]
All paths may be repeated. Records are keyed by 'requestId' (the ticker passed in, e.g. BANF-US)."""
import json, os, sys, argparse, datetime
sys.path.insert(0, os.path.dirname(__file__))
from fsload import load, tkey
BASE = os.environ.get('BT_DATA') or os.path.join(os.path.dirname(__file__), '..', 'data')  # BT_DATA=intl/data for the Europe/India run
TODAY = '2026-10-19'

def path_for(t): return os.path.join(BASE, tkey(t) + '.json')

def get(t, cache):
    if t not in cache:
        p = path_for(t)
        cache[t] = json.load(open(p)) if os.path.exists(p) else {'ticker': t, 'fundamentals': {}, 'adj_eps_actual': {}, 'entity': {}, 'sources': {}, 'missing': [], 'fmp_backup': {}}
    return cache[t]

ap = argparse.ArgumentParser()
ap.add_argument('--fund', action='append', default=[])
ap.add_argument('--entity', action='append', default=[])
ap.add_argument('--surprise', action='append', default=[])
ap.add_argument('--mv', action='append', default=[])
a = ap.parse_args()
cache = {}
for f in a.fund:
    for r in load(f):
        t = r.get('requestId');
        if not t or r.get('metric') is None: continue
        d = get(t, cache)
        fy = str(r.get('fiscalYear'))
        d['fundamentals'].setdefault(r['metric'], {})[fy] = {'v': r.get('value'), 'end': r.get('fiscalEndDate'), 'cur': r.get('currency'), 'formula': (r.get('audit') or {}).get('card', {}).get('formula')}
        d['sources']['fundamentals'] = f'FactSet Fundamentals ANN (USD), pulled {TODAY}'
for f in a.entity:
    for r in load(f):
        t = r.get('requestId');
        if not t: continue
        d = get(t, cache)
        d['entity'] = {'name': r.get('entityProperName'), 'description': r.get('businessDescription'), 'rbics_econ': r.get('rbicsEconomyClassification'), 'rbics_sector': r.get('rbicsSectorClassification'), 'rbics_subsector': r.get('rbicsSubsectorClassification'), 'rbics_indgrp': r.get('rbicsIndustryGroupClassification'), 'country_of_risk': r.get('countryOfRisk')}
        d['name'] = d.get('name') or r.get('entityProperName')
        d['sources']['entity'] = f'FactSet EntityReference, pulled {TODAY}'
for f in a.surprise:
    for r in load(f):
        t = r.get('requestId');
        if not t or r.get('fiscalYear') is None: continue
        d = get(t, cache)
        d['adj_eps_actual'][str(r['fiscalYear'])] = {'v': r.get('surpriseAfter'), 'end': r.get('fiscalEndDate'), 'consensus_before': r.get('surpriseBefore'), 'date': r.get('surpriseDate')}
        d['sources']['adj_eps'] = f'FactSet EstimatesConsensus surprise (actual EPS, broker/adjusted basis, USD), pulled {TODAY}'
for f in a.mv:
    for r in load(f):
        t = r.get('requestId');
        if not t: continue
        d = get(t, cache)
        v = r.get('currentMarketValue', r.get('marketValue', r.get('value')))
        if v is None:
            for k, val in r.items():
                if 'value' in k.lower() and isinstance(val, (int, float)): v = val
        d['market_value_usd_m'] = v; d['market_value_date'] = r.get('date')
        d['sources']['market_value'] = f'FactSet GlobalPrices market_value (USD m), pulled {TODAY}'
for t, d in cache.items():
    json.dump(d, open(path_for(t), 'w'), indent=0)
print('ingested', len(cache), 'tickers')
