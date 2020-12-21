#!/usr/bin/env python3
import numpy as np
from math import sqrt
from collections import defaultdict

def check_tile(tiles, placement, i, j, name):
    cur = tiles[name]
    for (x,y) in ((-1,0), (1,0), (0,-1), (0,1)):
        if i+x >= 0 and i+x < len(placement) and \
            j+y >= 0 and j+y < len(placement) and \
            placement[j+y][i+x] != -1:
            neighbor = tiles[placement[j+y][i+x]]
            if x == -1 and y == 0:
                if tuple(cur[:,0]) != tuple(neighbor[:,9]):
                    return False
            elif x == 1 and y == 0:
                if tuple(cur[:,9]) != tuple(neighbor[:,0]):
                    return False
            elif x == 0 and y == -1:
                if tuple(cur[0]) != tuple(neighbor[9]):
                    return False
            elif x == 0 and y == 1:
                if tuple(cur[9]) != tuple(neighbor[0]):
                    return False
            else:
                assert False
    return True

def arrange(placement, tiles, i, j, pairs, corners):
    #print(sum([row.count(-1)]))
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
    i = 0
    tiles = {}
    while i < len(lines):
        if "Tile" in lines[i]:
            tiles[int(lines[i].split(' ')[1][:-1])] = np.array([[char for char in line] for line in lines[i+1:i+11]])
            i += 12
    pairs = defaultdict(list)
    for source_name, source in tiles.items():
        count = 0
        for target_name, target in tiles.items():
            if source_name == target_name:
                continue
            s_top = source[0]
            s_bottom = source[9]
            s_left = source[:,0]
            s_right = source[:,9]

            t_top = target[0]
            t_bottom = target[9]
            t_left = target[:,0]
            t_right = target[:,9]

            s_borders = set([tuple(s_top), tuple(s_bottom), tuple(s_left), tuple(s_right),
                            tuple(reversed(tuple(s_top))), tuple(reversed(tuple(s_bottom))), tuple(reversed(tuple(s_left))), tuple(reversed(tuple(s_right)))])
            t_borders = set([tuple(t_top), tuple(t_bottom), tuple(t_left), tuple(t_right),
                            tuple(reversed(tuple(t_top))), tuple(reversed(tuple(t_bottom))), tuple(reversed(tuple(t_left))), tuple(reversed(tuple(t_right)))])

            if len(s_borders.intersection(t_borders)) > 0:
                pairs[source_name].append(target_name)
                count += 1
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
    #import pdb;pdb.set_trace()
    n = int(sqrt(len(tiles)))
    placement = [[-1 for _ in range(n)] for _ in range(n)]

    corners = []
    for k, v in pairs.items():
        if len(v) == 2:
            corners.append(k)

    if arrange(placement, tiles, 0, 0, pairs, corners):
        print("arrange succeeded")
        #p = placement[0][0] * placement[0][n-1] * placement[n-1][0] * placement[n-1][n-1]
        #return p
    else:
        print("arrange failed")
        #return 0

    #print(placement)
    for i, r in enumerate(placement):
        for j, c in enumerate(r):
            #print(c)
            #print("before")
            #print(tiles[c])
            #import pdb; pdb.set_trace()
            #if j < n-1:
            tiles[c] = np.delete(tiles[c], (9), axis=1)
            #if i < n-1:
            tiles[c] = np.delete(tiles[c], (9), axis=0)
            #if j > 0:
            tiles[c] = np.delete(tiles[c], (0), axis=1)
            #if i > 0:
            tiles[c] = np.delete(tiles[c], (0), axis=0)
            #print("after")
            #print(tiles[c])

    picture = None
    for r, row in enumerate(placement):
        row_arr = None
        for c, name in enumerate(row):
            if row_arr is None:
                row_arr = tiles[name]
            else:
                row_arr = np.concatenate((row_arr, tiles[name]), axis=1)
        if picture is None:
            picture = row_arr
        else:
            picture = np.concatenate((picture, row_arr), axis=0)

    #for row in picture:
        #print("".join(row))

    x = 0
    for row in picture:
        for ch in row:
            if ch == '#':
                x += 1


    #import pdb; pdb.set_trace()
    for rotate in (0,1,2,3):
        for flip in (0,1,2):
            print(f"rotating: {rotate} and flipping: {flip}")
            p2 = np.rot90(picture, rotate)
            if flip != 2:
                p2 = np.flip(p2, flip)
            #for row in picture:
            #    print("".join(row))
            num = num_monsters(p2)
            if num > 0:
                print(x - num*15)
                return(x-num*15)


    assert False
    #print(picture)

def num_monsters(picture):
    monster = ["                  # ",
               "#    ##    ##    ###",
               " #  #  #  #  #  #   "]
    num = 0
    for i in range(picture.shape[0]-2):
        for j in range(picture.shape[0]-19):
            p = picture[i:i+3,j:j+20]
            count = 0
            for (ii, jj), ch in np.ndenumerate(p):
                if monster[ii][jj] == '#' and ch == '#':
                    count += 1
            if count == 15:
                num += 1
    return num

if __name__ == "__main__":
    with open("day20.txt") as f:
        problem = [line.strip() for line in f.readlines()]
    with open("day20_s.txt") as f:
        sample = [line.strip() for line in f.readlines()]

    assert part1(sample) == 20899048083289
    ans1 = part1(problem)
    print(ans1)
    assert ans1 == 63187742854073

    assert part2(sample) == 273
    ans2 = part2(problem)
    print(ans2)
    assert ans2 == 2152
