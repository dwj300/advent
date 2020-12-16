#!/usr/bin/env python3
from functools import reduce

def is_valid(ticket, rules):
    for val in ticket:
        found = False
        for ranges in rules.values():
            for r in ranges:
                if val >= r[0] and val <= r[1]:
                    found = True
                    break
        if not found:
            return val
    return None

def part1(lines):
    rules = {}
    i = 0
    while i < len(lines) and len(lines[i]) > 0:
        parts = lines[i].split(':')
        ranges_str = parts[1].split(' or ')
        rules[parts[0]] = []
        for r in ranges_str:
            start,end = [int(x) for x in r.split('-')]
            rules[parts[0]].append((start, end))
        i += 1
    i += 5

    s = 0
    while i < len(lines):
        v = is_valid([int(x) for x in lines[i].strip().split(',')], rules)
        if v != None:
            s += v
        i += 1
    return s

def part2(lines):
    rules = {}
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if len(line) == 0:
            break
        parts = line.split(':')
        ranges_str = parts[1].split(' or ')
        rules[parts[0]] = []
        for r in ranges_str:
            start,end = [int(x) for x in r.split('-')]
            rules[parts[0]].append((start, end))
        i += 1

    fields = {}
    my = ""

    while i < len(lines) and "nearby tickets" not in lines[i]:
        if "your ticket" in lines[i]:
            i += 1
            my = [int(x) for x in lines[i].strip().split(',')]
        i += 1
    i += 1
    while i < len(lines):
        ticket = [int(x) for x in lines[i].strip().split(',')]
        if is_valid(ticket, rules) == None:
            for j,x in enumerate(ticket):
                if j in fields:
                    fields[j].append(x)
                else:
                    fields[j] = [x]
        i += 1

    mapping = {}
    for i, field in fields.items():
        for name, rule in rules.items():
            success = True
            for val in field:
                val_suc = False
                for r in rule:
                    if val >= r[0] and val <= r[1]:
                        val_suc = True
                if not val_suc:
                    success = False
            if success:
                if name in mapping:
                    mapping[name].append(i)
                else:
                    mapping[name] = [i]

    final_mapping = {}
    while len(mapping.keys()) > 0:
        for i, poss in mapping.items():
            for v in final_mapping.values():
                if v in poss:
                    poss.remove(v)

            if len(poss) == 1:
                final_mapping[i] = poss[0]
                del mapping[i]
                break

    s = 1
    return reduce(lambda x,y: x*y, [my[v] for k,v in final_mapping.items() if "departure" in k])


if __name__ == "__main__":
    with open("day16.txt") as f:
        problem = [line.strip() for line in f.readlines()]

    sample = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12""".split('\n')

    assert part1(sample) == 71
    ans1 = part1(problem)
    print(ans1)
    assert ans1 == 23925

    ans2 = part2(problem)
    print(ans2)
    assert ans2 == 964373157673
