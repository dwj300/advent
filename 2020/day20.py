#!/usr/bin/env python3
import numpy as np
from math import sqrt
from collections import defaultdict
from utils import runner

def check_tile(tiles, placement, i, j, name):
    cur = tiles[name]
    for (x,y) in ((-1,0), (1,0), (0,-1), (0,1)):
        if i+x >= 0 and i+x < len(placement) and \
            j+y >= 0 and j+y < len(placement) and \
            placement[j+y][i+x] != -1:
            neighbor = tiles[placement[j+y][i+x]]
            if x == -1 and y == 0 and tuple(cur[:,0]) != tuple(neighbor[:,9]):
                return False
            elif x == 1 and y == 0 and tuple(cur[:,9]) != tuple(neighbor[:,0]):
                return False
            elif x == 0 and y == -1 and tuple(cur[0]) != tuple(neighbor[9]):
                return False
            elif x == 0 and y == 1 and tuple(cur[9]) != tuple(neighbor[0]):
                return False
    return True

def arrange(placement, tiles, i, j, pairs, corners):
    if placement[j][i] != -1:
        i += 1
        if i == len(placement) and j == len(placement)-1:
            # Last tile - base case
            return True
        elif (i,j) in ((len(placement)-1,0), (0, len(placement)-1), (len(placement)-1,len(placement)-1)):
            p = corners
        elif i == len(placement):
            # past the end of the row
            i = 0
            p = pairs[placement[j][i]]
            j += 1
        else:
            p = pairs[placement[j][i-1]]
    else:
        p = corners

    for name in p:
        if any([name in row for row in placement]):
            continue
        for rotate in (0,1,2,3):
            for flip in (0,1,2):
                tiles[name] = np.rot90(tiles[name], rotate)
                if flip != 2:
                    tiles[name] = np.flip(tiles[name], flip)
                if check_tile(tiles, placement, i, j, name):
                    placement[j][i] = name
                    if arrange(placement, tiles, i, j, pairs, corners):
                        return True
                    placement[j][i] = -1

    return False

def parse(lines):
    tiles = {}
    pairs = defaultdict(list)
    i = 0
    while i < len(lines):
        if "Tile" in lines[i]:
            tiles[int(lines[i].split(' ')[1][:-1])] = np.array([[char for char in line] for line in lines[i+1:i+11]])
            i += 12

    for source_name, source in tiles.items():
        for target_name, target in tiles.items():
            if source_name == target_name:
                continue
            look, sets = [source, target], [set(), set()]
            for i in range(2):
                for idx in (0,9):
                    a = tuple(look[i][idx,:])
                    b = tuple(look[i][:,idx])
                    sets[i].add(a)
                    sets[i].add(b)
                    sets[i].add(tuple(reversed(a)))
                    sets[i].add(tuple(reversed(b)))

            if len(sets[0].intersection(sets[1])) > 0:
                pairs[source_name].append(target_name)
    return tiles, pairs

def part1(lines):
    _, pairs = parse(lines)
    p = 1
    for k, v in pairs.items():
        if len(v) == 2:
            p *= k
    return p

def part2(lines):
    tiles, pairs = parse(lines)
    n = int(sqrt(len(tiles)))
    placement = [[-1 for _ in range(n)] for _ in range(n)]
    corners = [k for k, v in pairs.items() if len(v) == 2]
    if not arrange(placement, tiles, 0, 0, pairs, corners):
        assert False

    # Remove borders
    for r in placement:
        for c in r:
            for idx in (9, 0):
                for axis in (1,0):
                    tiles[c] = np.delete(tiles[c], (idx), axis=axis)

    picture = np.concatenate([np.concatenate([tiles[n] for n in row], axis=1) for row in placement], axis=0)
    for rotate in (0,1,2,3):
        for flip in (0,1,2):
            p2 = np.rot90(picture, rotate)
            if flip != 2:
                p2 = np.flip(p2, flip)
            num = num_monsters(p2)
            if num > 0:
                return (picture == '#').sum() - num*15
    return 0

def num_monsters(p):
    monster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
    num = 0
    for i in range(p.shape[0]-2):
        for j in range(p.shape[0]-19):
            if sum([monster[ii][jj] == '#' and ch == '#' for (ii, jj), ch in np.ndenumerate(p[i:i+3,j:j+20])]) == 15:
                num += 1
    return num

if __name__ == "__main__":
    with open("day20.txt") as f:
        problem = [line.strip() for line in f.readlines()]
    with open("day20_s.txt") as f:
        sample = [line.strip() for line in f.readlines()]

    runner(part1, sample, 20899048083289, problem, 63187742854073)
    runner(part2, sample, 273, problem, 2152)
