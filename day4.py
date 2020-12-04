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
            pairs = line.split(" ")
            for pair in pairs:
                key = pair.split(':')[0]
                current.add(key)
    return count

def part2(lines):
    keys = set(['byr','iyr','eyr','hgt','hcl','ecl', 'pid'])
    count = 0
    current = {}
    for line in lines:
        if line == "":
            
            if set(current.keys()).issuperset(keys):
                correct = 0
                for key, v in current.items():
                    if key == 'byr':
                        if len(v) == 4 and int(v) >= 1920 and int(v) <= 2002:
                            correct += 1
                    elif key == 'iyr':
                        if len(v) == 4 and int(v) >= 2010 and int(v) <= 2020:
                            correct += 1
                    elif key == 'eyr':
                        if len(v) == 4 and int(v) >= 2020 and int(v) <= 2030:
                            correct += 1
                    elif key == 'hgt':
                        if len(v) >=3 and v[-2:] == 'cm':
                            if v[:-2].isnumeric and int(v[:-2]) >= 150 and int(v[:-2]) <= 193:
                                correct += 1
                        elif len(v) >=3 and v[-2:] == 'in':
                            if v[:-2].isnumeric and int(v[:-2]) >= 59 and int(v[:-2]) <= 76:
                                correct += 1
                    elif key == 'hcl':
                        p = re.compile("^#[0-9a-f]{6}$")
                        if p.match(v):
                            correct += 1
                    elif key == 'ecl':
                        if v in 'amb blu brn gry grn hzl oth'.split(' '):
                            correct += 1
                    elif key == 'pid':
                        p = re.compile("^[0-9]{9}$")
                        if p.match(v):
                            correct += 1
                if correct == 7:
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
