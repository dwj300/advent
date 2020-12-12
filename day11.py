#!/usr/bin/env python3


def occupied(seats, r, c, search):
    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            rr = r + i
            cc = c + j
            if search:
                while 0 <= rr < len(seats) and 0 <= cc < len(seats[0]) and seats[rr][cc] == '.':
                    rr += i
                    cc += j
            if 0 <= rr < len(seats) and 0 <= cc < len(seats[0]) and seats[rr][cc] == '#':
                count += 1
    return count


def part1(seats, search, num):
    old = None
    new = [[x for x in seat] for seat in seats]
    while new != old:
        old = [[x for x in seat] for seat in new]
        for r, row in enumerate(old):
            for c, seat in enumerate(row):
                if seat == 'L' and occupied(old, r, c, search) == 0:
                    seat = '#'
                elif seat == '#' and occupied(old, r, c, search) >= num:
                    seat = 'L'
                new[r][c] = seat
    return sum([row.count('#') for row in new])


if __name__ == "__main__":
    with open("day11.txt") as f:
        problem = [[char for char in line] for line in f.readlines()]

    sample = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".split('\n')

    sample = [[char for char in word] for word in sample]
    assert part1(sample, False, 4) == 37
    ans1 = part1(problem, False, 4)
    print(ans1)
    assert ans1 == 2406

    assert part1(sample, True, 5) == 26
    ans2 = part1(problem, True, 5)
    print(ans2)
    assert ans2 == 2149
