#!/usr/bin/env python3
from functools import reduce
from utils import runner

def helper(lines, dx, dy):
    x,y = (0,0)
    count = 0
    while y < len(lines)-1:
        x = x + dx
        y += dy
        if lines[y][x % len(lines[0])] == '#':
            count += 1
    return count

def part1(lines):
    return helper(lines, 3, 1)

def part2(lines):
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    [helper(lines, x, y) for (x,y) in slopes]
    return reduce(lambda x,y:x*y, [helper(lines, x, y) for (x,y) in slopes])

if __name__ == "__main__":
    sample = ['..##.......',
              '#...#...#..',
              '.#....#..#.',
              '..#.#...#.#',
              '.#...##..#.',
              '..#.##.....',
              '.#.#.#....#',
              '.#........#',
              '#.##...#...',
              '#...##....#',
              ".#..#...#.#"]
    with open("day3.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    runner(part1, sample, 7, lines, 181)
    runner(part2, sample, 336, lines, 1260601650)
