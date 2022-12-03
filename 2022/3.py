#!/usr/bin/env python3
import re
import sys

def score_item(item):
    if ord(item) >= ord('a') and ord(item) <= ord('z'):
        return ord(item) - ord('a') + 1
    return ord(item) - ord('A') + 27

def part1(lines): 
    def compute(line):
        n = len(line)
        p1, p2 = line[:(n//2)], line[(n//2):]
        items = set(p1).intersection(set(p2))
        return score_item(list(items)[0])
    return sum(map(compute, lines))

def part2(lines):
    i, s = 0, 0
    while i < len(lines):
        items = set(lines[i])
        for j in range(2):
            items.intersection_update(lines[i+1+j])
        s += score_item(list(items)[0])
        i += 3
    return s

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    print(part1(lines))
    print(part2(lines))
