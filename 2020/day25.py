#!/usr/bin/env python3
from utils import runner

def compute(pub, subject):
    cur = 1
    loop = 0
    while cur != pub:
        cur = (cur * subject) % 20201227
        loop += 1
    return loop

def part1(keys):
    card_pub, door_pub = list(map(int, keys))
    card_loop = compute(card_pub, 7)
    door_loop = compute(door_pub, 7)
    cur = 1
    for _ in range(card_loop):
        cur = (cur * door_pub) % 20201227
    return cur

def part2(keys):
    return "all done!"

if __name__ == "__main__":
    with open("day25.txt") as f:
        card, door = [line.strip() for line in f.readlines()]
    runner(part1, ("5764801", "17807724"), 14897079, (card, door), 19414467)