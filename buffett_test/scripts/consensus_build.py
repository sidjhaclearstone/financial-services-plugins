"""Parse central consensus raw files -> data/consensus.json  {ticker: {METRIC: {relPeriod: record}}}
Usage: python3 scripts/consensus_build.py FILE [FILE ...]"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from fsload import load
BASE = os.path.join(os.path.dirname(__file__), '..', 'data')
p = os.path.join(BASE, 'consensus.json')
out = json.load(open(p)) if os.path.exists(p) else {}
n = 0
for f in sys.argv[1:]:
    for r in load(f):
        t = r.get('requestId'); m = r.get('metric')
        if not t or not m: continue
        rel = str(r.get('relativePeriod'))
        rec = {k: r.get(k) for k in ('fiscalYear', 'fiscalEndDate', 'estimateDate', 'mean', 'median', 'standardDeviation', 'high', 'low', 'estimateCount', 'up', 'down')}
        if m == 'EPS_LTG': out.setdefault(t, {})[m] = rec
        else: out.setdefault(t, {}).setdefault(m, {})[rel] = rec
        n += 1
json.dump(out, open(p, 'w'))
print('consensus records', n, 'tickers', len(out))
