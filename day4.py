#!/usr/bin/env python3
from utils import runner
import re

def part1(lines):
    keys = set(['byr','iyr','eyr','hgt','hcl','ecl', 'pid'])
    count = 0
    current = set()
    for line in lines:
        if line == "":
            if current.issuperset(keys):
                count +=  1
            current = set()
        else:
            for pair in line.split(" "):
                current.add(pair.split(':')[0])
    return count

def part2(lines):
    hcl_p = re.compile("^#[0-9a-f]{6}$")
    pid_p = re.compile("^[0-9]{9}$")
    rules = {'byr': lambda v: len(v) == 4 and int(v) >= 1920 and int(v) <= 2002,
            'iyr': lambda v: len(v) == 4 and int(v) >= 2010 and int(v) <= 2020,
            'eyr': lambda v: len(v) == 4 and int(v) >= 2020 and int(v) <= 2030,
            'hgt': lambda v: len(v) >=3 and ((v[-2:] == 'cm' and v[:-2].isnumeric and int(v[:-2]) >= 150 and int(v[:-2]) <= 193) or \
                                             (v[-2:] == 'in' and v[:-2].isnumeric and int(v[:-2]) >= 59 and int(v[:-2]) <= 76)),
            'hcl': lambda v: hcl_p.match(v),
            'ecl': lambda v: v in 'amb blu brn gry grn hzl oth'.split(' '),
            'pid': lambda v: pid_p.match(v)}

    count = 0
    current = {}
    for line in lines:
        if line == "":
            correct = 0
            if len(list(filter(lambda pair: pair[0] in rules and rules[pair[0]](pair[1]), [(k, v) for k, v in current.items()]))) == 7:
                count +=  1
            current = {}
        else:
            pairs = line.split(" ")
            for pair in pairs:
                parts = pair.split(':')
                current[parts[0]] = parts[1]
    return count

if __name__ == "__main__":
    with open("4s.txt") as f:
        sample1 = [line.strip() for line in f.readlines()]

    with open("42i.txt") as f:
        sample2 = [line.strip() for line in f.readlines()]

    with open("42v.txt") as f:
        sample3 = [line.strip() for line in f.readlines()]

    with open("day4.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    runner(part1, sample1, 2, lines, 235)
    runner(part2, sample2, 0, lines, 194)
    runner(part2, sample3, 4, lines, 194)
