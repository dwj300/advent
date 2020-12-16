#!/usr/bin/env python3


def part1(lines):
    rules = {}
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            break
        parts = line.split(':')
        ranges_str = parts[1].split(' or ')
        rules[parts[0]] = []
        for r in ranges_str:
            start,end = [int(x) for x in r.split('-')]
            rules[parts[0]].append((start, end))

    s = 0
    start = False
    for line in lines:
        if "nearby tickets" in line:
            start = True
            continue
        if start:
            for val in [int(x) for x in line.strip().split(',')]:
                found = False
                v = 0
                for ranges in rules.values():
                    for r in ranges:
                        if val >= r[0] and val <= r[1]:
                            found = True
                if not found:
                    s += val
    return s

def part2(lines):
    rules = {}
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            break
        parts = line.split(':')
        ranges_str = parts[1].split(' or ')
        rules[parts[0]] = []
        for r in ranges_str:
            start,end = [int(x) for x in r.split('-')]
            rules[parts[0]].append((start, end))

    tickets = []
    fields = {}
    start = False
    my = ""

    for line in lines:
        if my is None:
            my = line
        if "your ticket" in line:
            my = None
            continue
        if "nearby tickets" in line:
            start = True
            continue
        if start:
            valid = True
            for val in [int(x) for x in line.strip().split(',')]:
                found = False
                v = 0
                for ranges in rules.values():
                    for r in ranges:
                        if val >= r[0] and val <= r[1]:
                            found = True
                if not found:
                    valid = False
            if valid:
                ticket = [int(x) for x in line.strip().split(',')]
                tickets.append(ticket)
                for i,x in enumerate(ticket):
                    if i in fields:
                        fields[i].append(x)
                    else:
                        fields[i] = [x]
                #print(line)

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

    print(mapping)
    print(final_mapping)


    print(tickets)
    print(fields)
    print(my)

    s = 1
    my = [int(x) for x in my.strip().split(',')]
    for i,j in final_mapping.items():
        print(i)
        if "departure" in i:
            s *= my[j]


    print(s)
    return s


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

    sample2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9""".split('\n')
    #sample = [0,3,6]
    #   problem = [0,8,15,2,12,1,4]

    assert part1(sample) == 71
    ans1 = part1(problem)
    print(ans1)
    assert ans1 == 23925

    #assert part2(sample2) == 175594
    ans2 = part2(problem)
    print(ans2)
    assert ans2 == 1505722
