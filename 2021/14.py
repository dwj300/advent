#!/usr/bin/env python3
import re
import sys
from collections import Counter

def parse(lines):
    p = lines[0].strip()
    i = 2
    rules = {}
    while i < len(lines):
        a, b = lines[i].strip().split(' -> ')
        rules[a] = b
        i += 1
    return p, rules

def sim(p, rules, steps):
    counts = Counter()
    for i in range(len(p) - 1):
        counts[p[i:i + 2]] += 1
    for _ in range(steps):
        counts2 = Counter()
        for k, v in counts.items():
            counts2[k[0] + rules[k]] += v
            counts2[rules[k] + k[1]] += v
        counts = counts2

    c = Counter()
    for k, v in counts.items():
        c[k[0]] += v
    c[p[-1]] += 1
    return (c.most_common()[0][1] - c.most_common()[-1][1])

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    p, rules = parse(open(filename).readlines())
    print(sim(p, rules, 10))
    print(sim(p, rules, 40))
