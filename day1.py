#!/usr/bin/env python3
from utils import runner

def part1(lines):
    lines = list(map(int, lines))
    parts = {}
    for i in lines:
        parts[2020-i] = i

    for i in lines:
        if i in parts:
            return parts[i] * i
    return -1

def part2(lines):
    lines = list(map(int, lines))
    parts = {}
    for i in lines:
        parts[2020-i] = i
    for i, a in enumerate(lines):
        for j, b in enumerate(lines):
            if i == j:
                continue
            s = a + b
            if s in parts:
                return parts[s] * a * b
    return -1

if __name__ == "__main__":
    sample = [1721,979,366,299,675,1456]
    with open("day1.txt") as f:
        nums = [int(line.strip()) for line in f.readlines()]
    runner(part1, sample, 514579, nums, 842016)
    runner(part2, sample, 241861950, nums, 9199664)
