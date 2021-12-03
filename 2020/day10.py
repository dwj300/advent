#!/usr/bin/env python3
import functools

@functools.lru_cache()
def helper(adapters, current, target):
    if current == target:
        return 1

    possible = [a for a in adapters if (a <= current + 3 and a > current)]
    return sum(map(lambda p: helper(adapters, p, target), possible))

def part1(nums):
    nums = list(map(int, nums))
    deltas = [0,0,0,1]
    current = 0
    for adapter in sorted(nums):
        if adapter > current and adapter <= current + 3:
            deltas[adapter-current] += 1
            current = adapter
    return deltas[1] * deltas[3]

def part2(nums):
    nums = list(map(int, nums))
    nums = tuple(sorted(nums))
    h = helper(nums, 0, max(nums))
    return h


if __name__ == "__main__":
    with open("day10.txt") as f:
        problem = [line.strip() for line in f.readlines()]

    sample1 = """16
10
15
5
1
11
7
19
6
12
4""".split('\n')

    sample2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".split('\n')

    sample = [x.strip() for x in sample1]
    sample3 = [x.strip() for x in sample2]
    assert part1(sample) == 35
    ans1 = part1(problem)
    print(ans1)
    assert ans1 == 1914

    assert part2(sample) == 8
    assert part2(sample3) == 19208
    ans2 = part2(problem)
    print(ans2)
    assert ans2 == 9256148959232
