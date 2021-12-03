#!/usr/bin/env python3

def num_increasing(nums, window=1):
    prev = sum(nums[0:window])
    n = 0
    for i in range(1, len(nums)):
        cur = sum(nums[i:i + window])
        if cur > prev:
            n += 1
        prev = cur
    return n

if __name__ == "__main__":
    with open('1.txt') as f:
        nums = [int(x.strip()) for x in f.readlines()]
    print(num_increasing(nums))
    print(num_increasing(nums, 3))
