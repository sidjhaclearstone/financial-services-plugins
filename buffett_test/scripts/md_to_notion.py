"""Convert a GitHub-markdown report to Notion-flavoured markdown (pipe tables -> <table>, escape specials). Usage: md_to_notion.py IN OUT 'callout text'"""
import re, sys
src = open(sys.argv[1]).read().split('\n')
def esc(s):
    parts = re.split(r'(`[^`]*`)', s); out = []
    for p in parts:
        if p.startswith('`') and p.endswith('`') and len(p) > 1: out.append(p); continue
        for ch in ['\\', '<', '>', '$', '~', '{', '}', '^', '|']: p = p.replace(ch, '\\' + ch)
        out.append(p)
    return ''.join(out)
sep = re.compile(r'^\s*\|[\s:\-|]+\|\s*$')
res = []; i = 0
while i < len(src):
    l = src[i]
    if i == 0 and l.startswith('# '): i += 1; continue
    if l.strip().startswith('|') and i + 1 < len(src) and sep.match(src[i + 1]):
        rows = []
        while i < len(src) and src[i].strip().startswith('|'):
            if not sep.match(src[i]): rows.append([c.strip() for c in src[i].strip().strip('|').split('|')])
            i += 1
        res.append('<table header-row="true">')
        for r in rows:
            res.append('\t<tr>'); res += ['\t\t<td>' + esc(c) + '</td>' for c in r]; res.append('\t</tr>')
        res.append('</table>'); continue
    if l.strip() == '---': res.append('---')
    else:
        m = re.match(r'^(\s*)(#+ |- |\d+\. |> )?(.*)$', l)
        res.append(m.group(1).replace('  ', '\t') + (m.group(2) or '') + esc(m.group(3)))
    i += 1
hdr = '<callout icon="📊" color="gray_bg">\n\t' + esc(sys.argv[3]) + '\n</callout>\n'
open(sys.argv[2], 'w').write(hdr + '\n'.join(res))
print('ok', len(hdr) + sum(len(x) for x in res))
