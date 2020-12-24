#!/usr/bin/env python3
from collections import defaultdict
from utils import runner

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def part1(line):
    start = [int(c) for c in line]
    one = play(start, 100, max(start))
    res = ""
    tmp = one.next
    while tmp != one:
        res += str(tmp.val)
        tmp = tmp.next
    return res

def part2(line):
    start = [int(c) for c in line]
    one = play(start, 10000000, 1000000)
    return one.next.val * one.next.next.val

def setup(start, MAX):
    mapping = {}
    head = Node(start[0])
    mapping[start[0]] = head
    cur = head
    m = max(start)
    for c in start[1:] + list(range(m+1, MAX+1)):
        new_node = Node(c)
        mapping[c] = new_node
        cur.next = new_node
        cur = cur.next
    cur.next = head
    return head, mapping

def play(start, rounds, MAX):
    head, mapping = setup(start, MAX)
    cur = head
    for r in range(rounds):
        p = cur.next
        bad = [cur.val, p.val, p.next.val, p.next.next.val]
        cur.next = p.next.next.next
        d = cur.val
        while d in bad:
            d -= 1
            if d < 1:
                d = MAX
        d_tmp = mapping[d].next
        mapping[d].next = p
        p.next.next.next = d_tmp
        cur = cur.next

    return mapping[1]

if __name__ == "__main__":
    sample = "389125467"
    problem = "872495136"
    runner(part1, sample, "67384529", problem, "27865934")
    runner(part2, sample, 149245887792, problem, 170836011000)
