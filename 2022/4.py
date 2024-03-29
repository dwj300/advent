#!/usr/bin/env python3
import re
import sys

def parse(line):
    p1, p2 = line.split(',')
    p1s, p1e = [int(x) for x in p1.split('-')]
    p2s, p2e = [int(x) for x in p2.split('-')]
    return p1s, p1e, p2s, p2e

def part1(lines):
    def contains(parts):
        p1s, p1e, p2s, p2e = parts
        return (p1s <= p2s and p2e <= p1e) or (p2s <= p1s and p1e <= p2e)
    return len(list(filter(contains, lines)))

def part2(lines):
    def overlaps(parts):
        p1s, p1e, p2s, p2e = parts
        return not (p1e < p2s or p2e < p1s)
    return len(list(filter(overlaps, lines)))

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    p = list(map(parse, lines))
    print(part1(p))
    print(part2(p))
