"""Print which runs ./cache/benchmark-data.json holds, and the entry github-action-benchmark
compares with (the last entry whose commit differs from this run's commit)."""
import json, os, sys
label, path = sys.argv[1], "cache/benchmark-data.json"
KIND = {33.850914: "single", 2.9622521: "bolt", 2.7980447: "redis"}
if not os.path.exists(path):
    print(f"{label}: no data file"); sys.exit(0)
entries = json.load(open(path)).get("entries", {}).get("Benchmark", [])
desc = ", ".join(f"{KIND.get(e['benches'][0]['value'], '?')}@{e['commit']['id'][:8]}" for e in entries)
print(f"{label}: suite 'Benchmark' has {len(entries)} entries: {desc}")
if label == "RESTORED":
    prev = [e for e in entries if e["commit"]["id"] != os.environ["GITHUB_SHA"]]
    if prev:
        p, cur = prev[-1], json.load(open("ci-cd.json"))[0]["value"]
        pv = p["benches"][0]["value"]
        print(f"{label}: compare target {KIND.get(pv, '?')}@{p['commit']['id'][:8]}: "
              f"Get Catalog previous {pv} vs current {cur}; alert needs previous/current > 2, "
              f"i.e. current < {pv / 2:.2f}")
    else:
        print(f"{label}: no entry from another commit, nothing to compare")
