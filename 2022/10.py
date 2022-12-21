#!/usr/bin/env python3
import re
import sys

def part1(lines):
    x, i, s = 1, 1, 0
    for line in lines:
        di, dx = 1, 0
        if line != "noop":
            di += 1
            dx = int(line.split(' ')[1])
        for _ in range(di):
            if (i-20) % 40 == 0:
                s += i * x
            i += 1
        x += dx
    return s

def part2(lines):
    x, i, row = 1, 1, ""
    for line in lines:
        di, dx = 1, 0
        if line != "noop":
            di += 1
            dx = int(line.split(' ')[1])
        for _ in range(di):
            if x<=i<=x+2:
                row += '#'
            else:
                row += ' '
            if i>0 and i % 40 == 0:
                print(row)
                i, row = 0, ""
            i += 1
        x += dx

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    print(part1(lines))
    part2(lines)
