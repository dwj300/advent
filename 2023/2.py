#!/usr/bin/env python3
import re
import sys
from collections import defaultdict
def part1(lines):
    score = 0
    for game in lines:
        g, sets = game.split(':')
        n = int(g.split(' ')[1])
        for s in sets.split(';'):
            colors = defaultdict(int)
            for b in s.split(','):
                i, color = [x.strip() for x in b.strip().split(' ')]
                i = int(i)
                colors[color] = i
            if colors["red"] > 12 or colors["green"] > 13 or colors["blue"] > 14:
                break
        else:
            score += n
    return score

def part2(lines):
    score = 0
    for game in lines:
        g, sets = game.split(':')
        n = int(g.split(' ')[1])
        r, g, b = 0,0,0
        for s in sets.split(';'):
            colors = defaultdict(int)
            for ball in s.split(','):
                i, color = [x.strip() for x in ball.strip().split(' ')]
                i = int(i)
                colors[color] = i
            r = max(r, colors["red"])
            g = max(g, colors["green"])
            b = max(b, colors["blue"])
        score += (r*g*b)
    return score


if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    print(part1(lines))
    print(part2(lines))
