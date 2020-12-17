#!/usr/bin/env python3
from collections import defaultdict
from functools import reduce
from copy import deepcopy
import re

pattern = re.compile(r"([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)")

def is_valid(ticket, rules):
    for val in ticket:
        if not any(map(lambda r: (val >= r[0][0] and val <= r[0][1]) or (val >= r[1][0] and val <= r[1][1]), rules.values())):
            return val
    return None

def extract_rules(lines):
    rules = {}
    for line in lines:
        if len(line) == 0:
            return rules
        name,a,b,c,d = pattern.match(line).group(1,2,3,4,5)
        rules[name] = [(int(a),int(b)), (int(c),int(d))]
    return rules

def extract_tickets(lines):
    my = []
    tickets = []
    i = 0
    while i < len(lines) and "nearby tickets" not in lines[i]:
        if "your ticket" in lines[i]:
            i += 1
            my = [int(x) for x in lines[i].strip().split(',')]
        i += 1
    i += 1
    for line in lines[i:]:
        tickets.append([int(x) for x in line.strip().split(',')])
    return my, tickets

def part1(lines):
    rules = extract_rules(lines)
    _, tickets = extract_tickets(lines)
    s = 0
    for ticket in tickets:
        v = is_valid(ticket, rules)
        if v != None:
            s += v
    return s

def part2(lines):
    mapping = defaultdict(list)
    rules = extract_rules(lines)
    my, tickets = extract_tickets(lines)
    valid_tickets = filter(lambda t: (is_valid(t, rules) == None), tickets)
    fields = {idx: list(map(lambda t: t[idx], deepcopy(valid_tickets))) for idx in range(len(my))}

    for i, field in fields.items():
        for name, r in rules.items():
            if not any(map(lambda val: (val < r[0][0] or val > r[0][1]) and (val < r[1][0] or val > r[1][1]), field)):
                mapping[name].append(i)

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
