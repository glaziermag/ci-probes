"""Write a minimal pytest-benchmark JSON (the fields github-action-benchmark's pytest parser reads)."""
import json, sys
ops = float(open("dr-bench/value.txt").read().split()[0])
mean = 1.0 / ops
bench = {
    "name": "test_benchmark_read",
    "fullname": "tests/test_benchmark.py::test_benchmark_read",
    "stats": {"min": mean, "max": mean, "mean": mean, "stddev": 0.0, "rounds": 5,
              "median": mean, "ops": ops, "total": mean * 5, "iterations": 1},
}
json.dump({"benchmarks": [bench], "version": "5.3.0"}, open(sys.argv[1], "w"))
print(f"synthetic ops={ops} iter/sec")
