#!/usr/bin/env python3
from collections import defaultdict
def part1(graph):
    def dfs(cur, smallSeen):
        if cur == cur.lower() and cur in smallSeen:
            return 0
        s2 = set(smallSeen)
        if cur == cur.lower():
            s2.add(cur)
        if cur == "end":
            return 1
        return sum([dfs(x, s2) for x in graph[cur]])
    return dfs("start", set())

def part2(graph):
    def dfs(cur, smallSeen, double):
        s2 = set(smallSeen)
        if cur == "start" and cur in smallSeen:
            return False
        if cur == cur.lower() and not double and cur in s2:
            s2.remove(cur)
            double = s2
        elif cur == cur.lower() and cur in smallSeen and double:
            return 0
        if cur == cur.lower():
            s2.add(cur)
        if cur == "end":
            return 1
        return sum([dfs(x, s2, double) for x in graph[cur]])
    return dfs("start", set(), None)

if __name__ == "__main__":
    graph = defaultdict(list)
    for line in open('12.txt'):
        src, tgt = line.strip().split('-')
        graph[src].append(tgt)
        graph[tgt].append(src)
    print(part1(graph))
    print(part2(graph))
