#!/usr/bin/env python3
from functools import reduce


def part1(lines):
    start = int(lines[0].strip())
    buses = [int(x) for x in lines[1].strip().split(',') if x != 'x']
    diff = []
    for bus in buses:
        x = (((start // bus)+1) * bus) - start
        diff.append((x,bus))
    m = min(diff, key=lambda x: x[0])
    return m[0]*m[1]


def inverse(a, n):
    if n == 1:
        return 1
    b0 = n
    t0, t1 = 0, 1

    while a > 1:
        q = a // n
        a, n = n, a % n
        t0, t1 = t1 - q * t0, t0

    if t1 < 0:
        t1 += b0
    return t1


def crt(pairs):
    ans = 0
    N = reduce(lambda x,y: x*y, [p[1] for p in pairs])
    for (a, n) in pairs:
        y = N // n
        z = inverse(y, n)
        ans += a*y*z
    return ans % N


def part2(lines):
    buses = [x for x in lines[1].strip().split(',')]
    pairs = []
    for a, bus in enumerate(buses):
        if bus == 'x':
            continue
        n = int(bus)
        pairs.append((-1*a%n, n))
    ans = crt(pairs)
    return crt(pairs)


if __name__ == "__main__":
    with open("day13.txt") as f:
        problem = [line.strip() for line in f.readlines()]

    sample = """939
7,13,x,x,59,x,31,19""".split('\n')

    assert part1(sample) == 295
    ans1 = part1(problem)
    print(ans1)
    assert ans1 == 2298

    assert(crt([(2,3), (3,5), (2,7)]) == 23)
    assert part2(sample) == 1068781
    ans2 = part2(problem)
    print(ans2)
    assert ans2 == 783685719679632
