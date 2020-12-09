#!/usr/bin/env python3

def check(nums, target):
    diff = {}
    for i, n in enumerate(nums):
        diff[target-n] = i

    for j, n in enumerate(nums):
        if n in diff and diff[n] != j:
            return True
    return False


def part1(nums, pre):
    for i in range(pre, len(nums)):
        if not check(nums[i-pre:i], nums[i]):
            return nums[i]
    return -1


def part2(nums, target):
    i, j, s = 0, 0, nums[0]
    while s != target and j < len(nums):
        if s < target:
            j += 1
            s += nums[j]
        else:
            s -= nums[i]
            i += 1
    return min(nums[i:j+1]) + max(nums[i:j+1])


if __name__ == "__main__":
    with open("day9.txt") as f:
        problem = [int(line.strip()) for line in f.readlines()]

    sample1 = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split('\n')
    sample = [int(x.strip()) for x in sample1]
    assert part1(sample, 5) == 127
    ans1 = part1(problem, 25)
    print(ans1)
    assert ans1 == 27911108

    assert part2(sample, 127) == 62
    ans2 = part2(problem, 27911108)
    print(ans2)
    assert ans2 == 4023754
