#!/usr/bin/env python3

def calc_bits(lines):
    bits = [0 for _ in lines[0]]
    for line in lines:
        for i, c in enumerate(line):
            bits[i] += int(c)
    return bits

def part1(lines):
    bits = calc_bits(lines)
    g, e = "", ""
    for b in bits:
        g += ('1' if (b > len(lines) // 2) else '0')
        e += ('0' if (b > len(lines) // 2) else '1')

    return int(g, 2) * int(e, 2)

def reducer(lines, low, high):
    i = 0
    while len(lines) > 1:
        bits = calc_bits(lines)
        bb = high if bits[i] >= len(lines) / 2 else low
        lines = [line for line in lines if line[i] == bb]
        i += 1
    return int(lines[0], 2)

def part2(lines):
    return reducer(lines, '0', '1') * reducer(lines, '1', '0')

if __name__ == "__main__":
    with open('3.txt') as f:
        lines = [x.strip() for x in f.readlines()]
    print(part1(lines))
    print(part2(lines))
