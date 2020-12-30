#!/usr/bin/env python3
from collections import defaultdict

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def make_tree(parts, mode):
    root = None
    i = 0
    while i < len(parts):
        part = parts[i]
        tmp = Node(part)
        if part == '(':
            j = i
            count = 0
            while count != 1 or parts[i] != ')':
                mapping = defaultdict(int, {'(': 1, ')': -1})
                count += mapping[parts[i]]
                i += 1
            tmp = make_tree(parts[j+1:i], mode)
        elif part == '*' and mode:
            tmp.left = root
            tmp.right = make_tree(parts[i+1:], mode)
            root = tmp
            i = len(parts)
            continue

        if root is None:
            root = tmp
        elif root.left is not None and root.right is None:
            root.right = tmp
        else:
            tmp.left = root
            root = tmp
        i += 1
    return root

def compute(tree):
    if tree.left is None and tree.right is None:
        return int(tree.val)
    elif tree.val == '*':
        return compute(tree.left) * compute(tree.right)
    elif tree.val == '+':
        return compute(tree.left) + compute(tree.right)

def part1(lines, mode=False):
    return sum(map(lambda line: compute(make_tree(line.replace('(', '( ').replace(')', ' )').split(' '), mode)), lines))

def part2(lines):
    return part1(lines, True)

if __name__ == "__main__":
    with open("day18.txt") as f:
        problem = [line.strip() for line in f.readlines()]

    assert part1(["1 + 2 * 3 + 4 * 5 + 6"]) == 71
    assert part1(["2 * 3 + (4 * 5)"]) == 26
    ans1 = part1(problem)
    print(ans1)
    assert ans1 == 31142189909908

    assert part2(["1 + 2 * 3 + 4 * 5 + 6"]) == 231
    assert part2(["2 * 3 + (4 * 5)"]) == 46
    ans2 = part2(problem)
    print(ans2)
    assert ans2 == 323912478287549
