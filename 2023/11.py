#!/usr/bin/env python3
import re
import sys

def search(g, a, b):
    return abs(b[1]-a[1]) + abs(b[0]-a[0])

def search2(g, a, b, ex_r, ex_c):
    cc = 0
    for c in range(min(b[1],a[1]), max(b[1],a[1])):
        cc += ex_c.get(c, 0)
    rr = 0
    for c in range(min(b[0],a[0]), max(b[0],a[0])):
        rr += ex_r.get(c, 0)

    return abs(b[1]-a[1]) + abs(b[0]-a[0]) + rr + cc

def part1(lines):
    g = [list(l.strip()) for l in lines]
    gal = []

    r = 0
    while r < len(g):
        if g[r] == ['.']*len(g[r]):
            g.insert(r, g[r])
            r += 1
        r += 1
    c = 0
    while c < len(g[0]):
        tmp = []
        for i in range(len(g)):
            tmp.append(g[i][c])
        
        if tmp == ['.']*len(tmp):
            for i in range(len(g)):
                g[i].insert(c, '.')
            c += 1
        c += 1

    for r, row in enumerate(g):
        for c, cell in enumerate(row):
            if cell == '#':
                gal.append((r,c))
    s = 0
    for i in range(len(gal)):
        for j in range(len(gal)):
            if i == j:
                continue
            s += search(g, gal[i], gal[j])
    return s // 2
            
def part2(lines):
    g = [list(l.strip()) for l in lines]
    gal = []
    ex_r = {}
    ex_c = {}
    r = 0
    while r < len(g):
        if g[r] == ['.']*len(g[r]):
            ex_r[r] = 1000000-1
        r += 1
    c = 0
    while c < len(g[0]):
        tmp = []
        for i in range(len(g)):
            tmp.append(g[i][c])
        
        if tmp == ['.']*len(tmp):
            ex_c[c] = 1000000-1
        c += 1

    for r, row in enumerate(g):
        for c, cell in enumerate(row):
            if cell == '#':
                gal.append((r,c))
    s = 0
    for i in range(len(gal)-1):
        for j in range(i+1,len(gal)):
            s += search2(g, gal[i], gal[j], ex_r, ex_c)
    return s


if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    print(part1(lines))
    print(part2(lines))
