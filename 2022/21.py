#!/usr/bin/env python3
import re
import sys

def part1(lines):
    m = {}
    while len(m) < len(lines):
        for line in lines:
            name, op = line.split(':')
            op = op.strip()
            if op.isdigit():
                m[name] = int(op)
            else:
                left, sign, right = op.split(' ')
                if left not in m or right not in m:
                    continue
                if sign == '+':
                    m[name] = m[left] + m[right]
                elif sign == '-':
                    m[name] = m[left] - m[right]
                elif sign == '*':
                    m[name] = m[left] * m[right]
                elif sign == '/':
                    m[name] = m[left] // m[right]
    return m['root']

class Node():
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.sign = None
        self.val = None
        self.parent = None
        self.guess = False
    def __repr__(self):
        l, r = self.left, self.right
        if l is None or r is None:
            return f"{self.name}: {self.val}"
        return f"{self.name}: {l.name} {self.sign} {r.name}"
 
def total(node):
    #print(node)
    if node.val is not None:
        return node.val
    if node.val is None and node.sign is None:
        return None
    
    l = total(node.left)
    r = total(node.right)
    if not l or not r or not node.sign:
        return None
    sign = node.sign
    if sign == '+':
        t = l + r
    elif sign == '-':
        t = l - r
    elif sign == '*':
        t = l * r
    elif sign == '/':
        t = l // r
    node.val = t
    #print(f"Totaling {node.name} = {t}")
    return t

def target(n, v):
    if n.name == "humn":
        return v
    l = total(n.left)
    # v == l sign r
    if l is not None:
        # v = l + r
        # v-l = r
        if n.sign == '+':
            return target(n.right, v-l)
        # v = l - r
        # l-v = r
        elif n.sign == '-':
            return target(n.right, l-v)
        # v = l * r
        # v // l = r
        elif n.sign == '*':
            return target(n.right, v//l)
        # v = l // r
        # l // v = r
        elif n.sign == '/':
            return target(n.right, l//v)
    r = total(n.right)
    assert r is not None

    # v = l + r
    # v - r = l
    if n.sign == '+':
        return target(n.left, v-r)
    # v = l - r
    # v + r = l
    elif n.sign == '-':
        return target(n.left, v+r)
    # v = l * r
    # v // r = l
    elif n.sign == '*':
        return target(n.left, v//r)
    # v = l // r
    # v * r = l
    elif n.sign == '/':
        return target(n.left, v*r)
    
def part2(lines):
    m = {}
    for line in lines:
        name, op = line.split(':')
        op = op.strip()
        if name not in m:
            n = Node(name)
            m[name] = n
        n = m[name]
    
        if name == 'humn':
            continue
        if op.isdigit():
            x = int(op)
            n.val = x
        else:
            left, sign, right = op.split(' ')
            if left not in m:
                m[left] = Node(left)
            if right not in m:
                m[right] = Node(right)
            n.left, n.right, n.sign = m[left], m[right], sign
            n.left.parent = n
            n.right.parent = n
    n = m['humn']
    while n:
        n.guess = True
        n = n.parent
    
    r = m["root"]
    if not r.left.guess:
        return target(r.right, total(r.left))
    return target(r.left, total(r.right))

if __name__ == "__main__":
    day = re.match("(?:./)?([0-9]+).py", sys.argv[0]).groups()[0]
    filename = sys.argv[1] if len(sys.argv) > 1 else f"{day}.txt"
    lines = open(filename).read().strip().split('\n')
    print(part1(lines))
    print(part2(lines))
