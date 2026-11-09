"""Write a zb-style ci-cd.json (customBiggerIsBetter) for one zot benchmark job.
Values are requests per sec that project-zot/zot logged at 68e541d9 (2026-11-08):
single node = run 42522459529, cluster bolt = job 128859188156, cluster redis = job 128859188141."""
import json, sys
NAMES = ["Get Catalog", "Push Monolith 1MB", "Pull 1MB", "Pull 100MB"]
VALUES = {
    "single": [33.850914, 79.91464, 560.8485, 44.248013],
    "bolt": [2.9622521, 4.645171, 20.575314, 3.1102972],
    "redis": [2.7980447, 3.5538752, 15.4032545, 4.038711],
}
kind = sys.argv[1]
print(json.dumps([{"name": n, "unit": "requests per sec", "value": v, "range": "3"}
                  for n, v in zip(NAMES, VALUES[kind])], indent=2))
