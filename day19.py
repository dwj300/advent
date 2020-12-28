#!/usr/bin/env python3
import re
from utils import runner

def parse(lines):
    lines = [line.strip() for line in lines]
    rules = {}
    strings = []
    i = 0
    while len(lines[i]) != 0:
        name, rule = lines[i].split(':')
        rules[name] = [r.strip().split(' ') for r in rule.split('|')]
        i += 1
    strings = lines[i+1:]
    return rules, strings

def make_re(rules, cur):
    if len(cur) == 1 and len(cur[0]) == 1 and '"' in cur[0][0]:
        return cur[0][0].replace('"', '')

    tmp = ""
    for j in cur:
        for i in j:
            tmp += "({0})".format(make_re(rules, rules[i]))
        tmp += '|'
    return tmp[:-1]

def part1(lines):
    rules, strings = parse(lines)
    regex = re.compile(f"^{make_re(rules, rules['0'])}$")
    return sum([bool(regex.match(line)) for line in strings])

def match(rules, text, start, key):
    if start >= len(text):
        return []

    options = rules[key]
    if len(options) == 1 and len(options[0]) == 1 and '"' in options[0][0]:
        if text[start] == options[0][0].replace('"', ''):
            return [start + 1]
        else:
            return []

    matches = []
    for option in options:
        partials = [start]
        for part in option:
            tmp = []
            for p in partials:
                tmp.extend(match(rules, text, p, part))
            partials = tmp
        matches.extend(partials)
    return matches

def part2(lines):
    rules, strings = parse(lines)
    rules['8'] = [['42'], ['42', '8']]
    rules['11'] = [['42', '31'], ['42', '11', '31']]
    return sum([len(line) in match(rules, line, 0, '0') for line in strings])

if __name__ == "__main__":
    with open("day19.txt") as f:
        problem = [line.strip() for line in f.readlines()]

    sample = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb""".split('\n')

    sample2 = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba""".split('\n')

    runner(part1, sample, 2, problem, 104)
    runner(part2, sample2, 12, problem, 314)
