"""Print which commits the benchmark data file holds (the baseline github-action-benchmark compares against)."""
import json, os, sys
path, label = sys.argv[1], sys.argv[2]
if not os.path.exists(path):
    print(f"{label}: no data file"); sys.exit(0)
d = json.load(open(path))
for suite, entries in d.get("entries", {}).items():
    desc = ", ".join(f"{e['commit']['id'][:8]}={e['benches'][0]['value']}" for e in entries)
    print(f"{label}: suite '{suite}' has {len(entries)} entr{'y' if len(entries)==1 else 'ies'}: {desc}")
