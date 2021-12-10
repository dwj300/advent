#!/usr/bin/env python3

def part1(lines):
    score = 0
    scores_2 = []
    m = {')': 3, ']': 57, '}': 1197, '>': 25137}
    m_2 = {')': 1, ']': 2, '}': 3, '>': 4}
    opens = {')': '(', ']': '[', '}': '{', '>': '<'}
    closes = {v: k for k, v in opens.items()}

    for line in lines:
        stack = []
        for c in line:
            if c in opens.keys():
                if len(stack) == 0 or stack.pop(0) != opens[c]:
                    score += m[c]
                    break
            else:
                stack.insert(0, c)
        else:
            if len(stack) != 0:
                score_2 = 0
                while stack:
                    score_2 *= 5
                    score_2 += m_2[closes[stack.pop(0)]]
                scores_2.append(score_2)
    scores_2.sort()
    return score, scores_2[len(scores_2) // 2]

if __name__ == "__main__":
    with open('10.txt') as f:
        lines = [x.strip() for x in f.readlines()]
    print(part1(lines))
