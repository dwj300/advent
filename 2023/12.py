#!/usr/bin/env python3
import re
import sys
from functools import cache

@cache
def f(line, pattern, i, p, cur):
    if i == len(line):
        if p == len(pattern) and cur == 0:
            return 1
        if p == len(pattern)-1 and cur == pattern[p]:
            return 1
        return 0

    ret = 0
    for c in ['#','.']:
        if line[i] != '?' and line[i] != c:
            continue
        if c == '#':
            ret += f(line, pattern, i+1, p, cur+1)
        elif c == '.' and cur == 0:
            ret += f(line, pattern, i+1, p, cur)
        elif c == '.' and cur > 0 and p < len(pattern) and pattern[p] == cur:
            ret += f(line, pattern, i+1, p+1, 0)
    return ret

def calc(lines, n=1):
    s = 0
    for line in lines:
        line, pattern = line.strip().split(' ')
        pattern = [int(x) for x in pattern.split(',')]*n
        line = '?'.join([line]*n)
        score = f(line, tuple(pattern), 0, 0, 0)
        s += score
    return s

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    print(calc(lines))
    print(calc(lines,n=5))

