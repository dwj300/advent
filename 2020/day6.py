#!/usr/bin/env python3

def part1(lines):
    groups = []
    group = set()
    for line in lines:
        line = line.strip()
        if line == "":
            groups.append(len(group))
            group = set()
        else:
            for l in line:
                group.add(l)

    return sum(groups)

def part2(lines):
    groups = []
    group = {}
    count = 0
    for line in lines:
        line = line.strip()
        if line == "":
            n = 0
            for k,v in group.items():
                if v == count:
                    n += 1
            groups.append(n)
            group = {}
            count = 0
        else:
            for l in line:
                if l in group:
                    group[l] += 1
                else:
                    group[l] = 1
            count += 1
    return sum(groups)

if __name__ == "__main__":
    with open("day6.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    sample = """abc

a
b
c

ab
ac

a
a
a
a

b

"""
    assert part1(sample.split('\n')) == 11
    print(part1(lines))

    assert part2(sample.split('\n')) == 6
    print(part2(lines))
