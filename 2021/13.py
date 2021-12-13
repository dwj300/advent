#!/usr/bin/env python3
import re
import sys

def parse(lines):
    points, folds = set(), []
    for line in lines:
        if ',' in line:
            x, y = [int(c) for c in line.strip().split(',')]
            points.add((x, y))
        elif 'fold' in line:
            folds.append(line.strip().split(' ')[2])
    return points, folds

def part1(points, folds):
    d, v = folds[0].split('=')
    v = int(v)
    p2 = set()
    for p in points:
        x, y = p
        if d == 'x':
            p2.add((min(x, 2 * v - x), y))
        else:
            p2.add((x, min(y, 2 * v - y)))
    return len(p2)

def part2(points, folds):
    for fold in folds:
        d, v = fold.split('=')
        v = int(v)
        p2 = set()
        for x, y in points:
            if d == 'x':
                p2.add((min(x, 2 * v - x), y))
            else:
                p2.add((x, min(y, 2 * v - y)))
        points = p2
    Y = max([p[1] for p in points])
    X = max([p[0] for p in points])
    G = [[' ' for x in range(X + 1)] for y in range(Y + 1)]
    for x, y in points:
        G[y][x] = '#'
    return '\n'.join([''.join(row) for row in G])

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    points, folds = parse(open(filename).readlines())
    print(part1(points, folds))
    print(part2(points, folds))
