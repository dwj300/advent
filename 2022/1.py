#!/usr/bin/env python3
import re
import sys

def parse(lines):
    c, counts = 0, []
    for line in lines:
        if len(line) == 0:
            counts.append(c)
            c = 0
            continue
        c += int(line)
    return counts

def part1(counts):
    return max(counts)

def part2(counts):
    return sum(sorted(counts,reverse=True)[:3])

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = [l.strip() for l in open(filename).readlines()]
    counts = parse(lines)
    print(part1(counts))
    print(part2(counts))
