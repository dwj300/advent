#!/usr/bin/env python3
import re
import sys
from collections import defaultdict

class Node(object):
    def __init__(self, name, parent, size):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = {}

def total_dirs(cur):
    if len(cur.children) == 0:
        return cur.size
    cur.size = sum([total_dirs(c) for c in cur.children.values()])
    return cur.size

def create_tree(lines):
    root = Node("/", None, 0)
    cur = root
    for line in lines[1:]:
        parts = line.split(' ')
        if parts[1] == "ls":
            continue
        if parts[0] != '$':
            size = int(parts[0]) if parts[0].isdigit() else 0
            cur.children[parts[1]] = Node(parts[1], cur, size)
            continue
        assert parts[1] == "cd"
        path = parts[2]
        if path != "..":
            cur = cur.children[path]
            continue
        if cur.parent != None:
            cur = cur.parent
    total_dirs(root)
    return root

def part1(root):
    t = 0
    q = [root]
    while q:
        cur = q.pop()
        if len(cur.children) > 0 and cur.size <= 100000:
            t += cur.size
        q.extend(cur.children.values())
    assert t == 1423358
    return t

def part2(root):
    free = 70000000 - root.size
    need = 30000000 - free
    m = 70000000
    q = [root]
    while q:
        cur = q.pop()
        if len(cur.children) > 0 and cur.size >= need:
            m = min(cur.size, m)
        q.extend(cur.children.values())
    assert m == 545729
    return m

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    root = create_tree(lines)
    print(part1(root))
    print(part2(root))
