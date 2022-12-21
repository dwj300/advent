#!/usr/bin/env python3
import re
import sys

def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def solve(moves, l):
    dirs = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    k = [[0,0] for _ in range(l)]
    t_seen = set([(0,0)])
    for move in moves:
        dir, n = move.split(' ')
        for _ in range(int(n)):
            k[0] = [k[0][0] + dirs[dir][0], k[0][1] + dirs[dir][1]]
            for i in range(1, l):
                d = dist(k[i-1], k[i])
                if d < 2:
                    continue
                if d > 2:
                    for x in range(2):
                        if k[i][x] > k[i-1][x]:
                            k[i][x] -= 1
                        else:
                            k[i][x] += 1
                elif k[i-1][0] == k[i][0]:
                    if k[i][1] > k[i-1][1]:
                        k[i][1] -= 1
                    else:
                        k[i][1] += 1
                elif k[i-1][1] == k[i][1]:
                    if k[i][0] > k[i-1][0]:
                        k[i][0] -= 1
                    else:
                        k[i][0] += 1
            t_seen.add(tuple(k[-1]))
    return len(t_seen)

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    moves = open(filename).read().strip().split('\n')
    print(solve(moves, 2))
    print(solve(moves, 10))
