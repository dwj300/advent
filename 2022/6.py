#!/usr/bin/env python3
import re
import sys

def marker(line, l):
    for i in range(l, len(line)):
        if len(set(line[i-l:i])) == l:
            return i

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    line = open(filename).read()
    print(marker(line, 4))
    print(marker(line, 14))
