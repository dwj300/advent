#!/usr/bin/env python3
import re
import sys
from collections import Counter

def gen_lists(lines):
    l1, l2 = [], []
    for line in lines:
        a, b = [int(x.strip()) for x in line.split()]
        l1.append(a)
        l2.append(b)
    return l1, l2

def part1(lines):
    l1, l2 = gen_lists(lines)
    l1.sort()
    l2.sort()
    assert len(l1) == len(l2)
    d = 0
    for i in range(len(l1)):
        d += abs(l2[i]-l1[i])
    return d

def part2(lines):
    l1, l2 = gen_lists(lines)
    c = Counter(l2)
    s = 0
    for x in l1:
        s += x * c[x]
    return s

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    print(part1(lines))
    print(part2(lines))
