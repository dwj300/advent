#!/usr/bin/env python3
import re
import sys

def move_sand(x, y, max_y, grid):
    while (x,y) not in grid:
        if y > max_y:
            return False
        for dx, dy in ((0,1),(-1,1),(1,1)):
            xx, yy = x+dx, y+dy
            if (xx, yy) not in grid:
                x, y = xx, yy
                break
        else:
            grid.add((x,y))
            return True
    return False

def parse(lines):
    grid = set()
    max_y = 0
    for line in lines:
        points = [[int(pp) for pp in l.strip().split(',')] for l in line.split("->")]
        for i in range(len(points)-1):
            start, end = points[i], points[i+1]
            for x in range(min(start[0],end[0]), max(start[0],end[0])+1):
                for y in range(min(start[1],end[1]), max(start[1],end[1])+1):
                    grid.add((x,y))
                    max_y = max(max_y, y)
    return grid, max_y

def part1(lines):
    grid, max_y = parse(lines)
    ans = 0
    while move_sand(500, 0, max_y, grid):
        ans += 1
    return ans

def part2(lines):
    grid, max_y = parse(lines)
    floor = max_y + 2
    for x in range(500-floor-2, 500+floor+3):
        grid.add((x,floor))
    ans = 0
    while (500,0) not in grid:
        move_sand(500, 0, floor, grid)
        ans += 1
    return ans     

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    print(part1(lines))
    print(part2(lines))
