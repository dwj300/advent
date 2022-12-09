#!/usr/bin/env python3
import re
import sys

def parse(lines):
    i = 0
    while len(lines[i]) > 0: i += 1
    grid = [list(l) for l in lines[:i-1]]
    pattern, stacks = lines[i-1], []
    for j, x in enumerate(pattern):
        if str.isdigit(x):
            stacks.append([])
            for row in grid:
                if row[j] != ' ':
                    stacks[int(x)-1].insert(0, row[j])
    i += 1
    r = re.compile(r'move ([0-9]+) from ([0-9]) to ([0-9])')
    def extract(line):
        m = r.match(line)
        return [int(x) for x in m.groups()]
    moves = map(extract, lines[i:])
    return stacks, moves

def move(lines, reverse):
    stacks, moves = parse(lines)
    for l, src, tgt in moves:
        src, tgt = src-1, tgt-1
        x = stacks[src][len(stacks[src])-l:]
        stacks[src] = stacks[src][:len(stacks[src])-l]
        if reverse:
            x.reverse()
        stacks[tgt].extend(x)
    return "".join([s[-1] for s in stacks])

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    print(move(lines, True))
    print(move(lines, False))
