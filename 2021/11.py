#!/usr/bin/env python3

def energy(G):
    part1, f, step = 0, 0, 1
    R, C = len(G), len(G[0])
    while True:
        for r in range(R):
            for c in range(C):
                G[r][c] += 1
        fs = set()
        p = 1
        while p > 0:
            p = 0
            for r in range(R):
                for c in range(C):
                    if G[r][c] > 9:
                        fs.add((r, c))
                        G[r][c] = 0
                        for dr in range(-1, 2):
                            for dc in range(-1, 2):
                                tr, tc = r + dr, c + dc
                                if (dr == dc == 0):
                                    continue
                                if not (0 <= tr < R and 0 <= tc < C):
                                    continue
                                G[tr][tc] += 1
                                if G[tr][tc] > 9:
                                    p += 1
        for r, c in fs:
            graph[r][c] = 0
        f += len(fs)
        if step == 100:
            part1 = f

        if len(fs) == R * C:
            return part1, step
        step += 1

if __name__ == "__main__":
    graph = []
    for line in open('11.txt'):
        graph.append([int(y) for y in line.strip()])
    print(energy(graph))
