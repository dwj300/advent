#!/usr/bin/env python3
DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))

def in_bounds(graph, y, x):
    if y < 0 or x < 0 or y >= len(graph) or x >= len(graph[0]):
        return False
    return True

def find_lows(graph):
    lows = set()
    for y in range(len(graph)):
        for x in range(len(graph[y])):
            for dy, dx in DIRS:
                ty, tx = y + dy, x + dx
                if in_bounds(graph, ty, tx) and graph[y][x] >= graph[ty][tx]:
                    break
            else:
                lows.add((y, x))
    return lows

def part1(graph):
    n = 0
    for y, x in find_lows(graph):
        n += (1 + graph[y][x])
    return n

def explore(yy, xx, graph):
    q = [(yy, xx)]
    basin = set()
    while q:
        y, x = q.pop(0)
        basin.add((y, x))
        for dy, dx in DIRS:
            ty, tx = y + dy, x + dx
            if not in_bounds(graph, ty, tx):
                continue
            if (ty, tx) in basin:
                continue
            if graph[ty][tx] == 9:
                continue
            q.append((ty, tx))
    return len(basin)

def part2(graph):
    sizes = []
    for y, x in find_lows(graph):
        sizes.append(explore(y, x, graph))
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]

if __name__ == "__main__":
    with open('9.txt') as f:
        graph = [[int(c) for c in x.strip()] for x in f.readlines()]
    print(part1(graph))
    print(part2(graph))
