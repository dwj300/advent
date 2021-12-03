#!/usr/bin/env python3

def split(line, r, target, u, j):
    for l in line:
        if l == target:
            r[1] = ((r[1] - r[0]) // 2) + r[0]
        else:
            r[0] = round((r[1] - r[0]) / 2) + r[0]
    return  r[0] if line[7] == target else r[1]

def seat(line):
    row = split(line, [0, 127], 'F', 0, 7)
    col = split(line, [0, 7], 'L', 7, 9)
    return row * 8 + col

def part1(lines):
    return max([seat(line) for line in lines])

def part2(lines):
    seats = set([seat(line) for line in lines])
    nums = set(range(min(seats), max(seats)+1))
    return list(nums.difference(seats))[0]

if __name__ == "__main__":
    with open("day5.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    assert seat("FBFBBFFRLR") == 357
    ans1 = part1(lines)
    print(ans1)
    assert ans1 == 6714
    ans2 = part2(lines)
    print(ans2)
    assert ans2 == 3435
