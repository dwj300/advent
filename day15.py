#!/usr/bin/env python3


def part1(nums, count):
    spoken = {}
    prev = 0
    for i,num in enumerate(nums):
        prev = num
        spoken[num] = [i+1, None]
    for i in range(len(nums)+1, count+1):
        speak = 0
        if prev in spoken and spoken[prev][1] is not None:
            speak = spoken[prev][0] - spoken[prev][1]

        if speak in spoken:
            spoken[speak][1] = spoken[speak][0]
            spoken[speak][0] = i
        else:
            spoken[speak] = [i,None]
        prev = speak
    return prev


if __name__ == "__main__":
    sample = [0,3,6]
    problem = [0,8,15,2,12,1,4]

    assert part1(sample, 2020) == 436
    ans1 = part1(problem, 2020)
    print(ans1)
    assert ans1 == 289

    assert part1(sample, 30000000) == 175594
    ans2 = part1(problem, 30000000)
    print(ans2)
    assert ans2 == 1505722
