#!/usr/bin/env python3

def part1(lines):
    d, h = 0, 0
    for line in lines:
        inst, amt = line.split(' ')
        amt = int(amt)
        if inst == "forward":
            h += amt
        elif inst == "down":
            d += amt
        elif inst == "up":
            d -= amt
    return d * h

def part2(lines):
    a, d, h = 0, 0, 0
    for line in lines:
        inst, amt = line.split(' ')
        amt = int(amt)
        if inst == "forward":
            h += amt
            d += a * amt
        elif inst == "down":
            a += amt
        elif inst == "up":
            a -= amt
    return d * h

if __name__ == "__main__":
    with open('2.txt') as f:
        lines = [x.strip() for x in f.readlines()]
    print(part1(lines))
    print(part2(lines))
