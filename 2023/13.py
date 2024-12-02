#!/usr/bin/env python3
import re
import sys

def check_row(window, r, goal=0):
    d = 0
    defect = 0
    while r-d >= 0 and r+1+d < len(window):
        a = window[r-d]
        b = window[r+d+1]

        for i in range(len(a)):
            if a[i] != b[i]:
                defect += 1
        if defect > 1:
            break
        d += 1
    if (r-d == -1 or r+1+d == len(window)) and d > 0 and defect == goal:
        return True
    return False 

def check_col(window, c, goal=0):
    d = 0
    defect = 0
    while c-d >= 0 and c+1+d < len(window[0]):
        a = [row[c-d] for row in window]
        b = [row[c+d+1] for row in window]

        for i in range(len(a)):
            if a[i] != b[i]:
                defect += 1
        if defect > 1:
            break
        d += 1
    if (c-d == -1 or c+1+d == len(window[0])) and d > 0 and defect == goal:
        return True
    return False 

def part1(lines, goal=0):
    windows = []
    window = []
    for line in lines + ['']:
        if len(line) == 0:
            windows.append(window)
            window = []
            continue
        window.append(line)
    s = 0
    for window in windows:
        for r in range(len(window)-1):
            if check_row(window, r, goal):
                s += 100*(r+1)
                break
        else:
            for c in range(len(window[0])-1):
                if check_col(window, c, goal):
                    s += c+1
                    break
    return s

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    print(part1(lines))
    print(part1(lines, 1))
