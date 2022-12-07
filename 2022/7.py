#!/usr/bin/env python3
import re
import sys
from collections import defaultdict

class Node(object):
    def __init__(self, name, parent, size=0):
        self.parent = parent
        self.name = name
        self.size = size
        self.children = {}

def total_dirs(cur):
    if len(cur.children) == 0:
        return cur.size
    cur.size = sum([total_dirs(c) for c in cur.children.values()])
    return cur.size

def create_tree(lines):
    i = 1
    root = Node("/", None)
    cur = root
    while i < len(lines):
        # handle ls
        if lines[i] == "$ ls":
            i += 1
            while i < len(lines) and "$" not in lines[i]:
                size, name = lines[i].split(' ')
                if size == "dir":
                    cur.children[name] = Node(name, cur)
                else:
                    cur.children[name] = Node(name, cur, int(size))
                i += 1
            i -= 1
        else:
            assert "$ cd " in lines[i]
            parts = lines[i].split(' ')
            path = parts[-1]
            if path != "..":
                cur = cur.children[path]
            elif path == ".." and cur.parent != None:
                cur = cur.parent
        i += 1
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
