#!/usr/bin/env python3
import re
import sys
from collections import defaultdict

class Node(object):
    def __str__(self):
        r = ""
        if len(self.children) == 0:
            p = self.parent.name if self.parent else ""
            r += f"Dir: {self.name}; parent: {p} size: {self.size}\n"
        else:
            r += f"File: {self.name}: {self.size}\n"
        for _, v in self.children.items():
            r += "  " + str(v)
        return r
    def __init__(self, name, parent, size=0):
        self.parent = parent
        self.name = name
        self.size = size
        self.children = {}

def create_tree(lines):
    i = 1
    root = Node("/", None)
    cur = root
    while i < len(lines):
        # handle ls
        if lines[i] == "$ ls":
            print(f"Running ls on {cur.name}")
            i += 1
            while i < len(lines) and "$" not in lines[i]:
                print(lines[i])
                size, name = lines[i].split(' ')
                if size == "dir":
                    print(f"Adding dir {name}")
                    cur.children[name] = Node(name, cur)
                else:
                    print(f"Adding file {name}")
                    cur.children[name] = Node(name, cur, int(size))
                i += 1
            i -= 1
        else:
            print(lines[i])
            assert "$ cd " in lines[i]
            parts = lines[i].split(' ')
            path = parts[-1]
            print(f"path: {path}")
            if path != "..":
                print(f"cur name: {cur.name}")
                cur = cur.children[path]
                print(f"cur name: {cur.name}")
            elif path == ".." and cur.parent != None:
                cur = cur.parent
            
        i += 1
    print(root)
    total_dirs(root)
    print(root)
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

def total_dirs(cur):
    #print(f"calling total on {cur.name}")
    if len(cur.children) == 0:
        return cur.size
    cur.size = sum([total_dirs(c) for c in cur.children.values()])
    return cur.size


def part2(root):    
    need = 30000000 - (70000000 - root.size)

    m = None
    q = [root]
    while q:
        cur = q.pop()
        if len(cur.children) > 0 and cur.size >= need:
            if not m or cur.size < m:
                print(f"FOUND BETTER MIN: {cur.name}, {cur.size}")
                m = cur.size
        q.extend(cur.children.values())
    
    print(f"root total: {root.size}")
    print(f"need total: {need}")
    assert m == 545729
    return m

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    root = create_tree(lines)
    print(part1(root))
    print(part2(root))
