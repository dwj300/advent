#!/usr/bin/env python3
from collections import defaultdict

def part1(lines):
    n = 0
    for line in lines:
        for word in line.split(' | ')[1].split(' '):
            if len(word) in set([2, 3, 4, 7]):
                n += 1
    return n

def part2(lines):
    n = 0
    for line in lines:
        train, test = line.split(' | ')

        counts, nums = defaultdict(list), {}
        for word in train.split(' '):
            counts[len(word)].append(set(word))
        nums = {}
        nums[1] = counts[2][0]
        nums[4] = counts[4][0]
        nums[7] = counts[3][0]
        nums[8] = counts[7][0]
        nums[3] = next(filter(lambda w: len(nums[1] - w) == 0, counts[5]))
        nums[9] = nums[3] | nums[4]
        nums[6] = next(filter(lambda w: len(w - nums[1]) == 5, counts[6]))
        nums[0] = next(filter(lambda w: w not in (nums[6], nums[9]), counts[6]))
        nums[5] = next(filter(lambda w: len(w - nums[6]) == 0, counts[5]))
        nums[2] = next(filter(lambda w: w not in (nums[3], nums[5]), counts[5]))

        rev = {}
        for k, v in nums.items():
            rev[frozenset(v)] = k
        b = 0
        for word in test.split(' '):
            b *= 10
            b += rev[frozenset(word)]
        n += b
    return n

if __name__ == "__main__":
    with open('8.txt') as f:
        lines = [x.strip() for x in f.readlines()]
    print(part1(lines))
    print(part2(lines))
