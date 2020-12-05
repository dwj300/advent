#!/usr/bin/env python3

def seat(line):
    r = [0,127]
    for l in line[:7]:
        if l == 'F':
            r[1] = ((r[1] - r[0]) // 2) + r[0]
        else:
            r[0] = round((r[1] - r[0]) / 2) + r[0]
    row = r[0] if line[7] == 'F' else r[1]
    c = [0,7]
    for l in line[7:10]:
        if l == 'L':
            c[1] = ((c[1] - c[0]) // 2) + c[0]
        else:
            c[0] = round((c[1] - c[0]) / 2) + c[0]
    col = c[0] if line[9] == 'L' else c[1]
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
    print(part1(lines))
    print(part2(lines))
