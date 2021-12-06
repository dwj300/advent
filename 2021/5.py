#!/usr/bin/env python3
from collections import defaultdict

def parse(lines):
    nums = []
    for line in lines:
        start, end = line.split("->")
        x1, y1 = [int(x) for x in start.strip().split(',')]
        x2, y2 = [int(x) for x in end.strip().split(',')]
        nums.append((x1, x2, y1, y2))
    return nums

def part1(lines):
    pos = defaultdict(int)
    for x1, x2, y1, y2 in lines:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                pos[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                pos[(x, y1)] += 1
    return len([x for x in pos.values() if x >= 2])

def part2(lines):
    pos = defaultdict(int)
    for x1, x2, y1, y2 in lines:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                pos[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                pos[(x, y1)] += 1
        else:
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            while x1 != x2 and y1 != y2:
                pos[(x1, y1)] += 1
                x1 += dx
                y1 += dy
            pos[(x1, y1)] += 1
    return len([x for x in pos.values() if x >= 2])

if __name__ == "__main__":
    with open('5.txt') as f:
        rows = [x.strip() for x in f.readlines()]
    lines = parse(rows)
    print(part1(lines))
    print(part2(lines))
