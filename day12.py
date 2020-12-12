#!/usr/bin/env python3


def part1(lines):
    x,y = 0,0
    d = 0
    for row in lines:
        row = row.strip()
        i = row[0]
        n = int(row[1:])
        if i == 'F':
            if d in (0,2):
                j = 1 if d == 0 else -1
                x += j*n
            if d in (1,3):
                j = 1 if d == 1 else -1
                y += j*n
        elif i in ('R', 'L'):
            j = 1 if i == 'R' else -1
            d = (d + j*(n // 90)) % 4
        elif i in ('N', 'S'):
            j = 1 if i == 'S'  else -1
            y += j*n
        elif i in ('W', 'E'):
            j = 1 if i == 'E'  else -1
            x += j*n

    return abs(x) + abs(y)

def part2(lines):
    wx,wy = 10,-1
    x,y = 0,0
    for row in lines:
        row = row.strip()
        i = row[0]
        n = int(row[1:])
        if i == 'F':
            x += n*wx
            y += n*wy
        elif i in ('L', 'R'):
            j = -1 if i == 'L' else 1
            for _ in range(n // 90):
                wx,wy = j*-1*wy, j*wx
        elif i in ('N', 'S'):
            d = -1 if i == 'N' else 1
            wy += d*n
        elif i in ('W', 'E'):
            d = -1 if i == 'W' else 1
            wx += d*n
    return abs(x) + abs(y)


if __name__ == "__main__":
    with open("day12.txt") as f:
        problem = [line.strip() for line in f.readlines()]

    sample = """F10
N3
F7
R90
F11""".split('\n')

    assert part1(sample) == 25
    ans1 = part1(problem)
    print(ans1)
    assert ans1 == 1186

    assert part2(sample) == 286
    ans2 = part2(problem)
    print(ans2)
    assert ans2 == 47806
