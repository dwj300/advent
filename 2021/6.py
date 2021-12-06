#!/usr/bin/env python3
from collections import defaultdict

def part1(fish):
    for d in range(80):
        new = []
        for i in range(len(fish)):
            fish[i] -= 1
            if fish[i] == -1:
                new.append(8)
                fish[i] = 6
        fish.extend(new)
    return len(fish)

def part2(fish):
    new = defaultdict(int)
    for f in fish:
        new[f] += 1
    fish = new
    for d in range(256):
        new = defaultdict(int)
        for f, c in fish.items():
            if f == 0:
                new[6] += c
                new[8] += c
            else:
                new[f - 1] += c
            fish = new
    return sum(fish.values())

if __name__ == "__main__":
    with open('6.txt') as f:
        fish = [int(y) for y in f.read().split(',')]
    print(part1(fish))
    print(part2(fish))
