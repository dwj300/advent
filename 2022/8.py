#!/usr/bin/env python3
import re
import sys
from collections import defaultdict

def part1(grid):
    m, n = len(grid)-1, len(grid[0])-1
    visible = [[False for _ in range(n+1)] for _ in range(m+1)]

    # left to right and right to left
    X = ((0, n, 1), (n, 0, -1))
    for r in range(m+1):
        for s, e, d in X:
            prev = -1
            for c in range(s, e, d):
                if grid[r][c] > prev:    
                    visible[r][c] = True
                prev = max(prev, grid[r][c])
    
    # top to bottom and bottom to top
    Y = ((0, m, 1), (m, 0, -1))
    for c in range(n+1):
        prev = -1
        for s, e, d in Y:
            prev = -1
            for r in range(s, e, d):
                if grid[r][c] > prev:
                    visible[r][c] = True
                prev = max(prev, grid[r][c])

    v = sum([len(list(filter(lambda x: x, r))) for r in visible])
    assert v == 1794
    return v

def part2(grid):
    m, n = len(grid), len(grid[0])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    ans = 0

    for r in range(m):
        for c in range(n):
            cur = 1
            for (dr, dc) in dirs:
                dist = 1
                rr, cc = r+dr, c+dc
                while True:
                    if not (0 <= rr < m and 0 <= cc < n):
                        dist -= 1
                        break
                    if grid[rr][cc] >= grid[r][c]:
                        break
                    dist += 1
                    rr, cc = rr+dr, cc+dc
                cur *= dist
            ans = max(ans, cur)
    assert ans == 199272
    return ans

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    grid = [[int(x) for x in l.strip()] for l in lines]
    print(part1(grid))
    print(part2(grid))
