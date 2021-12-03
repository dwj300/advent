#!/usr/bin/env python3
import re
from utils import runner

def part1(lines):
    num = 0
    p = re.compile("(?P<min>[0-9]+)-(?P<max>[0-9]+) (?P<letter>[a-z]): (?P<pw>[a-z]+)")
    for line in lines:
        m = p.match(line)
        count = m.group('pw').count(m.group('letter'))
        if count >= int(m.group('min')) and count <= int(m.group('max')):
            num += 1
    return num

def part2(lines):
    num = 0
    p = re.compile("(?P<min>[0-9]+)-(?P<max>[0-9]+) (?P<letter>[a-z]): (?P<pw>[a-z]+)")
    for line in lines:
        m = p.match(line)
        letter = m.group('letter')
        pw = m.group('pw')
        MIN = int(m.group('min')) - 1
        MAX = int(m.group('max')) - 1
        if (pw[MIN] == letter and pw[MAX] != letter) or (pw[MIN] != letter and pw[MAX] == letter):
            num += 1
    return num

if __name__ == "__main__":
    sample = ["1-3 a: abcde", "1-3 b: cdefgn", "2-9 c: ccccccccc"]
    with open("day2.txt") as f:
        lines = f.readlines()
    runner(part1, sample, 2, lines, 550)
    runner(part2, sample, 1, lines, 634)
