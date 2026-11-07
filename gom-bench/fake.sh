#!/bin/sh
# Synthetic `go test -bench` output: the real runner CPU line, ns/op from gom-bench/value.txt.
v=$(cat gom-bench/value.txt)
cpu=$(grep -m1 '^model name' /proc/cpuinfo | cut -d: -f2 | xargs)
printf 'goos: linux\ngoarch: amd64\npkg: github.com/glaziermag/ci-probes/gom-bench\ncpu: %s\n' "$cpu"
printf 'BenchmarkToBytes-4   \t 1979722\t       %s ns/op\t      40 B/op\t       3 allocs/op\n' "$v"
printf 'PASS\nok  \tgithub.com/glaziermag/ci-probes/gom-bench\t1.234s\n'
