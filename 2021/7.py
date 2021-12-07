#!/usr/bin/env python3
from statistics import median

def part1(nums):
    return sum((abs(n - int(median(nums))) for n in nums))

def part2(nums):
    def gauss(n):
        return n * (n + 1) // 2
    f = float('inf')
    for goal in range(min(nums), max(nums) + 1):
        f = min(f, sum((gauss(abs(n - goal)) for n in nums)))
    return f

if __name__ == "__main__":
    with open('7.txt') as f:
        nums = [int(x) for x in f.read().strip().split(',')]
    print(part1(nums))
    print(part2(nums))
