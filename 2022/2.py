#!/usr/bin/env python3
import re
import sys

wins = {'A': 'B', 'B': 'C', 'C': 'A'}

def score_move(b): return ord(b) - ord('A') + 1

def convert(b): return chr(ord(b)-ord('X')+ord('A'))

def part1(lines):
    def score(line):
        a, b = line.split(' ')
        b = convert(b)
        if a == b:
            return 3 + score_move(b)
        elif wins[a] == b:
            return 6 + score_move(b)
        return score_move(b)

    return sum(map(score, lines))

def part2(lines):
    wins = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    loss = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    mapping = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    
    def score(line):
        a, b = line.split(' ')
        if b == 'Y':
            return 3 + score_move(convert(mapping[a]))
        elif b == 'Z':
            return 6 + score_move(convert(wins[a]))
        return 0 + score_move(convert(loss[a]))

    return sum(map(score, lines))

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    print(part1(lines))
    print(part2(lines))
