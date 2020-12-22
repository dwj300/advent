#!/usr/bin/env python3
from utils import runner

def part1(lines):
    decks = parse(lines)
    while all([len(decks[i]) > 0 for i in (0,1)]):
        cards = [decks[d].pop(0) for d in (0,1)]
        winner = 0
        if cards[0] < cards[1]:
            winner = 1
            cards = reversed(cards)
        decks[winner].extend(cards)
    return sum([c*(len(decks[winner])-i) for (i,c) in enumerate(decks[winner])])

def part2(lines):
    winner, decks = helper(parse(lines))
    return sum([c*(len(decks[winner])-i) for (i,c) in enumerate(decks[winner])])

def parse(lines):
    i = 1
    decks = [[],[]]
    j = 0
    while i < len(lines):
        line = lines[i].strip()
        if "Player" in line:
            j += 1
        elif len(line) > 0:
            decks[j].append(int(lines[i].strip()))
        i += 1
    return decks

def helper(decks):
    seen = set()
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        view = tuple(tuple(decks[i]) for i in (0,1))
        if view in seen:
            return 0, decks
        seen.add(view)
        cards = [decks[d].pop(0) for d in (0,1)]
        if all([len(decks[i]) >= cards[i] for i in (0,1)]):
            winner, _ = helper([decks[i][:cards[i]] for i in (0,1)])
        elif cards[0] < cards[1]:
            winner = 1
        else:
            winner = 0
        if winner == 1:
            cards = reversed(cards)
        decks[winner].extend(cards)
    return winner, decks

if __name__ == "__main__":
    with open("day22.txt") as f:
        problem = [line.strip() for line in f.readlines()]

    sample = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10""".split('\n')

    runner(part1, sample, 306, problem, 32856)
    runner(part2, sample, 291, problem, 33805)
