#!/usr/bin/env python3
import re

def parse(lines):
    p = re.compile("([0-9]+) ([a-z ]+)")
    rules = {}
    for line in lines:
        if line == "":
            continue

        parts = line.split(" bags contain ")
        src = parts[0]
        targets = []
        if "contain no other bags" not in line:
            for part in parts[1].split(','):
                combo = part.strip().split(" bag")[0]
                g = p.match(combo).groups()
                num = int(g[0])
                name = g[1]
                targets.append((num, name))
        rules[src] = targets
    return rules

def part1(lines):
    def search(start, rules, seen):
        if start == "shiny gold":
            return True
        if start in seen or not start in rules or (start in rules and len(rules[start]) == 0):
            return False

        seen.add(start)
        for s in rules[start]:
            s = s[1]
            if search(s, rules, seen):
                return True
        return False

    rules = parse(lines)
    return len(list(filter(lambda x: x, map(lambda key: key != "shiny gold" and search(key, rules, set()), rules.keys()))))


def part2(lines):
    rules = parse(lines)

    def recurse(k):
        if len(rules[k]) == 0:
            return 0
        return sum(map(lambda x: x[0] + x[0] * recurse(x[1]), rules[k]))

    return recurse('shiny gold')

if __name__ == "__main__":
    with open("day7.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    sample1 = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
""".split('\n')
    assert part1(sample1) == 4
    ans1 = part1(lines)
    print(ans1)
    assert ans1 == 332

    sample2 = """faded blue bags contain no other bags.
dotted black bags contain no other bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
shiny gold bags contain 1 dark olive bags, 2 vibrant plum bags.""".split('\n')

    sample3 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.""".split('\n')

    assert part2(sample2) == 32
    assert part2(sample3) == 126
    ans2 = part2(lines)
    print(ans2)
    assert ans2 == 10875
