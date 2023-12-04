#!/usr/bin/env python3
import re
import sys

def part1(lines):
    s = 0
    for l in lines:
        n = []
        for c in l:
            if c.isdigit():
                n.append(int(c))
        s += 10*n[0] + n[-1]
    return s

# len 3,4,5
mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def part2(lines):
    s = 0
    for l in lines:
        n = []
        word = ""
        for c in l:
            if c.isdigit():
                n.append(int(c))
                word = ""
                continue
            word += c
            options = []
            for i in range(5, 2, -1):
                if len(word) >= 5:
                    options.append(word[-1*i:])
            for o in options:
                if o in mapping:
                    n.append(mapping[o])
        s += 10*n[0] + n[-1]
    return s

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    print(part1(lines))
    print(part2(lines))
