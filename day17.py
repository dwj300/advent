#!/usr/bin/env python3
from collections import defaultdict

def part1(lines, w_range):
    lines = [line.strip() for line in lines]
    active = set()
    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            if c == '#':
                active.add((x,y,0,0))

    for _ in range(6):
        new_active = set()
        neighbors = defaultdict(int)
        for a in active:
            count = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    for z in range(-1,2):
                        for w in w_range:
                            if x == y == z == w == 0:
                                continue
                            if (a[0]+x,a[1]+y,a[2]+z, a[3]+w) in active:
                                count += 1
                            neighbors[(a[0]+x,a[1]+y,a[2]+z, a[3]+w)] += 1
            if count in (2,3):
                new_active.add(a)
        for neighbor, v in neighbors.items():
            if neighbor not in active and v == 3:
                new_active.add(neighbor)
        active = new_active

    return len(active)

if __name__ == "__main__":
    with open("day17.txt") as f:
        problem = [line.strip() for line in f.readlines()]

    sample = """.#.
..#
###""".split('\n')
    assert part1(sample, range(1)) == 112
    ans1 = part1(problem, range(1))
    print(ans1)
    assert ans1 == 289

    p2s = part1(sample, range(-1,2))
    assert p2s == 848
    ans2 = part1(problem, range(-1,2))
    print(ans2)
    assert ans2 == 2084
