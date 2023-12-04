#!/usr/bin/env python3
import re
import sys
from collections import defaultdict

def part1(lines):
    s = 0
    for line in lines:
        _, data = line.split(':')
        win, ours = [x.strip() for x in data.split('|')]
        w = set([int(n.strip()) for n in win.split(' ') if len(n.strip()) > 0])
        o = set([int(n.strip()) for n in ours.split(' ') if len(n.strip()) > 0])
        score = len(w.intersection(o))
        if score > 0:
            s += 2**(len(w.intersection(o))-1)
    return s

def part2(lines):
    cc = defaultdict(int)
    for line in lines:
        card, data = line.split(':')
        c = int(card.strip().split(' ')[-1])
        cc[c] += 1
        win, ours = [x.strip() for x in data.split('|')]
        w = set([int(n.strip()) for n in win.split(' ') if len(n.strip()) > 0])
        o = set([int(n.strip()) for n in ours.split(' ') if len(n.strip()) > 0])
        score = len(w.intersection(o))
        if score > 0:
            for i in range(score):
                cc[c+i+1] += cc[c]
    return sum(cc.values())
   

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    print(part1(lines))
    print(part2(lines))
