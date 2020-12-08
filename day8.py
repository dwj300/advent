#!/usr/bin/env python3
import re


def part1(lines):
    a = 0
    seen = set()
    i = 0
    while i not in seen:
        seen.add(i)
        parts = lines[i].split(' ')
        if parts[0] == "acc":
            a += int(parts[1])
        elif parts[0] == "jmp":
            i += int(parts[1])-1
        i += 1
    return a


def part2(lines):
    for j in range(len(lines)):
        for inst in ["nop", "jmp"]:
            a = 0
            seen = set()
            i = 0
            while i not in seen and i != len(lines)-1:
                seen.add(i)
                parts = lines[i].split(' ')
                if i == j and inst == parts[0]:
                    print(lines[i])
                    parts[0] = "jmp" if inst == "nop" else "nop"
                if parts[0] == "acc":
                    a += int(parts[1])
                elif parts[0] == "jmp":
                    i += int(parts[1])-1
                i += 1
            if i == len(lines) - 1:
                print("J:", j)
                print("inst:", inst)
                return a
    return -1


if __name__ == "__main__":
    with open("day8.txt") as f:
        problem = [line.strip() for line in f.readlines()]

    sample1 = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".split('\n')
    assert part1(sample1) == 5
    ans1 = part1(problem)
    print(ans1)
    assert ans1 == 1179

    assert part2(sample1) == 8
    ans2 = part2(problem)
    print(ans2)
    assert ans2 == 1089
