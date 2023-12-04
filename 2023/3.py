#!/usr/bin/env python3
import re
import sys
from collections import defaultdict
from math import prod

dirs = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

def part1(lines):
    sym = set()
    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch != '.' and not ch.isdigit():
                sym.add((r,c))
    s = 0
    for r, line in enumerate(lines):
        prev = ""
        valid = False
        for c, ch in enumerate(line):
            if ch.isdigit():
                prev += ch
                if not valid:
                    for (dr, dc) in dirs:
                        if (r+dr,c+dc) in sym:
                            valid = True
                            break
            if (not ch.isdigit() or c == len(line)-1) and len(prev) > 0:
                if valid:
                    s += int(prev)
                prev = ""
                valid = False
    return s
def part2(lines):
    sym = set()
    gears = {}
    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch != '.' and not ch.isdigit():
                sym.add((r,c))
            if ch == '*':
                gears[(r,c)] = []
    for r, line in enumerate(lines):
        prev = ""
        valid = False
        g = set()
        for c, ch in enumerate(line):
            if ch.isdigit():
                prev += ch
                for (dr, dc) in dirs:
                    if (r+dr,c+dc) in sym:
                        valid = True
                    if (r+dr,c+dc) in gears:
                        g.add((r+dr,c+dc))
            if (not ch.isdigit() or c == len(line)-1) and len(prev) > 0:
                if valid:
                    for x in g:
                        gears[x].append(int(prev))
                prev = ""
                valid = False
                g = set()
    return sum([prod(l) for l in gears.values() if len(l) == 2])

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    print(part1(lines))
    print(part2(lines))
