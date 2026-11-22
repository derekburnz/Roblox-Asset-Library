"""Merge partial toolkit_qa reports into the full one: rows and 'Where to look' sections replaced per asset."""
import re, sys
def parse(path):
    text = open(path).read()
    head, _, rest = text.partition("| Asset |")
    table, _, where = rest.partition("## Where to look")
    rows = {}
    order = []
    for line in table.splitlines():
        m = re.match(r"\| (CatCafe_\S+) \|", line)
        if m:
            if m.group(1) not in rows: order.append(m.group(1))
            rows[m.group(1)] = line
    details = {}
    for block in re.split(r"\n(?=### )", where):
        m = re.match(r"\s*### (\S+)", block)
        if m:
            details[m.group(1)] = block.strip("\n")
    return head, rows, order, details
full = sys.argv[1]
head, rows, order, details = parse(full)
for p in sys.argv[2:]:
    _, r, o, d = parse(p)
    for k in o:
        if k not in rows: order.append(k)
        rows[k] = r[k]
        details.pop(k, None)
        if k in d:
            details[k] = d[k]
dorder = [k for k in order if k in details]
out = head + "| Asset | Tris | Draw calls | qa_check errors | warnings | visible overlaps | hidden overlaps | floating parts (gap >= 0.05) |\n|---|---|---|---|---|---|---|---|\n"
out += "\n".join(rows[k] for k in order) + "\n\n## Where to look\n" + ("\n\n".join(details[k] for k in dorder) if dorder else "\nNothing visible.") + "\n"
open(full, "w").write(out)
print(len(order), "rows,", len(dorder), "detail sections")
