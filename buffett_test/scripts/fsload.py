"""Load a raw FactSet/FMP MCP tool result file (plain JSON, or [{"type":"text","text":...}] wrapper) -> list of records."""
import json, sys

def load(path):
    t = open(path).read().strip()
    # strip any non-JSON preamble
    i = min([k for k in (t.find('{'), t.find('[')) if k >= 0] or [0])
    t = t[i:]
    d = json.loads(t)
    if isinstance(d, list) and d and isinstance(d[0], dict) and 'text' in d[0] and 'type' in d[0]:
        out = []
        for part in d:
            try:
                out += _records(json.loads(part['text']))
            except Exception:
                pass
        return out
    return _records(d)

def _records(d):
    if isinstance(d, dict):
        if 'data' in d and isinstance(d['data'], list):
            return d['data']
        return [d]
    if isinstance(d, list):
        return d
    return []

def tkey(ticker):
    """File-safe key: BRK.B-US -> BRK_B"""
    t = ticker.upper()
    if t.endswith('-US'):
        t = t[:-3]
    return t.replace('.', '_').replace('/', '_')

if __name__ == '__main__':
    r = load(sys.argv[1]); print(len(r)); print(r[:2])
