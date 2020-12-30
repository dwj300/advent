#!/usr/bin/env python3
from collections import defaultdict
from functools import reduce
from utils import runner

def parse(lines):
    possible = defaultdict(list)
    ing = defaultdict(int)

    for line in lines:
        parts = line.strip().replace('(', '').replace(')', '').split("contains")
        fds = [p.strip() for p in parts[0].strip().split(' ')]
        alergens = [a.strip() for a in parts[1].split(',')]
        for f in fds:
            ing[f] += 1
        for a in alergens:
            possible[a].append(fds)
    return possible, ing

def part1(lines):
    possible, ing = parse(lines)
    bad = reduce(lambda x,y: x.union(y), [set.intersection(*[set(a) for a in v]) for v in possible.values()])
    return sum([ing[i] for i in ing.keys() if i not in bad])

def part2(lines):
    possible, ing = parse(lines)
    mapping = {}
    bad = { k: set.intersection(*[set(a) for a in v]) for (k,v) in possible.items() }

    while bad:
        solved = next(k for (k,v) in bad.items() if len(v) == 1)
        mapping[solved] = bad[solved].pop()
        for v in bad.values():
            v.discard(mapping[solved])
        del bad[solved]
    return ",".join([mapping[k] for k in sorted(mapping.keys())])

if __name__ == "__main__":
    with open("day21.txt") as f:
        problem = [line.strip() for line in f.readlines()]

    sample = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""".split('\n')

    runner(part1, sample, 5, problem, 2072)
    runner(part2, sample, "mxmxvkd,sqjhc,fvjkl", problem, "fdsfpg,jmvxx,lkv,cbzcgvc,kfgln,pqqks,pqrvc,lclnj")
