#!/usr/bin/env python3


def set_bit(value, bit):
    return value | (1<<35-bit)


def clear_bit(value, bit):
    return value & ~(1<<35-bit)


def part1(lines):
    memory = {}
    mask = ""
    for line in lines:
        parts = line.split(' = ')
        if parts[0] == "mask":
            mask = parts[1]
        elif "mem" in parts[0]:
            val = int(parts[1])
            for i,x in enumerate(mask):
                if x == '1':
                    val = set_bit(val, i)
                elif x == '0':
                    val = clear_bit(val, i)
            memory[int(parts[0][4:-1])] = val
    return sum(memory.values())


def addresses(addr, f, i):
    if i == len(f)-1:
        return [clear_bit(addr, f[i]), set_bit(addr, f[i])]
    return addresses(set_bit(addr, f[i]), f, i+1) + addresses(clear_bit(addr, f[i]), f, i+1)


def part2(lines):
    memory = {}
    mask = ""
    for line in lines:
        line = line.strip()
        parts = line.split(' = ')
        if parts[0] == "mask":
            mask = parts[1]
        elif "mem" in parts[0]:
            address = int(parts[0][4:-1])
            f = []
            for i,x in enumerate(mask):
                if x == '1':
                    address = set_bit(address, i)
                elif x == 'X':
                    f.append(i)
            for addr in addresses(address, f, 0):
                memory[addr] = int(parts[1])
    return sum(memory.values())


if __name__ == "__main__":
    with open("day14.txt") as f:
        problem = [line.strip() for line in f.readlines()]

    sample = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".split('\n')

    sample2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""".split('\n')

    assert part1(sample) == 165
    ans1 = part1(problem)
    print(ans1)
    assert ans1 == 18630548206046

    assert part2(sample2) == 208
    ans2 = part2(problem)
    print(ans2)
    assert ans2 == 4254673508445
