#!/usr/bin/env python3
import re
import sys
from collections import defaultdict
import heapq

def part1(G, n):
    R, C = len(G), len(G[0])
    dp = [[None for _ in range(n*C)] for _ in range(n*R)]

    q = [(0, 0, 0)]
    while q:
        cost, r, c = heapq.heappop(q)
        if r < 0 or r >= n*R or c < 0 or c >= n*C:
            continue
        val = G[r%R][c%C] + (r//R) + (c//C)
        while val > 9:
            val -= 9
        cost += val
        if not dp[r][c] or cost < dp[r][c]:
            dp[r][c] = cost
        else:
            continue
        if r == n*R-1 and c == n*C-1:
            break
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            heapq.heappush(q, (dp[r][c], r+dr, c+dc))
    return dp[n*R-1][n*C-1] - G[0][0]

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    graph = [[int(c) for c in row.strip()] for row in open(filename)]
    print(part1(graph, 1))
    print(part1(graph, 5))
