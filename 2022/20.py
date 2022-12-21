#!/usr/bin/env python3
import re
import sys
from collections import defaultdict

def part1(lines):
    nums = [int(l) for l in lines]
    s = list(range(len(nums)))
    i = 0
    moved = [False for _ in range(len(nums))]
    print(nums)
    while i < len(nums):
        if moved[i]:
            i += 1
            continue
        
        d = nums[i]
        #if d < 0:
        #    d -= 1
        
        new = (d + i-1) % (len(nums))
        print(f"moving {nums[i]} from {i} to {new}")
        # if new < i:
        #     i += 1
        #print("{i}")
        #print(nums)
        x = nums.pop(i)
        
        nums.insert(new, x)
        #moved[i] = moved[new]
        moved.insert(new, moved.pop(i))
        moved[new] = True
        print(nums)
        print(moved)
    print(nums)
    

def part2(lines):
    pass

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    print(part1(lines))
    print(part2(lines))
