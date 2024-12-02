#!/usr/bin/env python3
import re
import sys

def hist(l):
    h = [l]
    while True:
        d = []
        for i in range(1, len(l)):
            d.append(l[i] - l[i-1])
        h.append(d)
        if d == [0]*len(d):
            break
        l = d
    return h

def calc(l):
    h = hist(l)
    return sum([l[-1] for l in h])

def calc2(l):
    h = hist(l)
    h[-1].insert(0, 0)
    for i in range(len(h)-2,-1,-1):
        h[i].insert(0, h[i][0]-h[i+1][0])
    return h[0][0]

def part1(lines):
    return sum([calc([int(x) for x in line.strip().split(' ')]) for line in lines])

def part2(lines):
    return sum([calc2([int(x) for x in line.strip().split(' ')]) for line in lines])

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    print(part1(lines))
    print(part2(lines))
