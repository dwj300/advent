#!/usr/bin/env python3
from collections import defaultdict
from utils import runner

directions = {
        'e': (1,-1, 0),
        'se': (0,-1,1),
        'sw': (-1,0,1),
        'w': (-1,1,0),
        'nw': (0,1,-1),
        'ne': (1,0,-1)
    }

def part1(lines):
    grid = run(lines)
    return len(grid)

def run(lines):
    lines = [l.strip() for l in lines]
    grid = set()

    for line in lines:
        cur = (0,0,0)
        i = 0
        dirs = ""
        while i < len(line):
            if line[i] in ('e', 'w'):
                d = line[i]
                i += 1
            elif line[i:i+2] in ('se', 'sw', 'nw', 'ne'):
                d = line[i:i+2]
                i += 2
            else:
                assert False
            dirs += d

            cur = (cur[0] + directions[d][0], cur[1] + directions[d][1], cur[2] + directions[d][2])
        if cur in grid:
            grid.remove(cur)
        else:
            grid.add(cur)
    return grid

def part2(lines):
    grid = run(lines)
    for d in range(100):
        grid2 = set()
        neighbors = defaultdict(int)
        for cur in grid:
            count = 0
            for _, dd in directions.items():
                tmp = (cur[0] + dd[0], cur[1] + dd[1], cur[2] + dd[2])
                if tmp in grid:
                    count += 1

                neighbors[tmp] += 1

            if not (count == 0 or count > 2):
                grid2.add(cur)

        for n,v in neighbors.items():
            if v == 2 and n not in grid:
                grid2.add(n)
        grid = grid2

    return len(grid)

if __name__ == "__main__":
    with open("day24.txt") as f:
        problem = [line.strip() for line in f.readlines()]

    sample = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""".split('\n')

    runner(part1, sample, 10, problem, 263)
    runner(part2, sample, 2208, problem, 3649)
