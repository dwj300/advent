#!/usr/bin/env python3
import re
import sys

def part1(lines):
    times = [int(x) for x in lines[0].split(':')[1].strip().split()]
    dists = [int(x) for x in lines[1].split(':')[1].strip().split()]
    assert len(times) == len(dists)
    p = 1
    for i in range(len(times)):
        t = times[i]
        d = dists[i]
        n = 0
        for h in range(t):
            remain = t-h
            total = remain * h
            if total > d:
                n += 1
        p *= n
    return p

def part2(lines):
    time = int("".join(lines[0].split(':')[1].strip().split()))
    dist = int("".join(lines[1].split(':')[1].strip().split()))
    # run binary search to find the min time to win
    s, e = 0, time
    while s < e-1:
        h = (s + e) // 2
        score = (time-h) * h
        if score < dist:
            s = h
        elif score > dist:
            e = h
    low = e
    # run binary search to find the max time to win
    s, e = 0, time
    while s < e-1:
        h = (s + e) // 2
        score = (time-h) * h
        if score > dist:
            s = h
        elif score < dist:
            e = h
    high = s
    return high - low + 1 


if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    print(part1(lines))
    print(part2(lines))
