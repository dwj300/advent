#!/usr/bin/env python3

def parse_boards(lines):
    nums = [int(x) for x in lines[0].split(',')]
    i = 2
    boards = []
    while i < len(lines):
        board = [[int(r) for r in row.replace('  ', ' ').split(' ')] for row in lines[i:i+5]]
        boards.append(board)
        i += 6
    return nums, boards

def sum_board(board):
    return sum([sum([c for c in row if c != 'X']) for row in board])

def mark_cells(boards, num):
    for b in range(len(boards)):
        for r in range(len(boards[b])):
            for c in range(len(boards[b][r])):
                if boards[b][r][c] == num:
                    boards[b][r][c] = 'X'
    return boards

def check_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] != 'X':
                break
        else:
            return True
    for c in range(len(board[0])):
        for r in range(len(board)):
            if board[r][c] != 'X':
                break
        else:
            return True
    return False

def part1(nums, boards):
    for num in nums:
        boards = mark_cells(boards, num)
        for board in boards:
            if check_board(board):
                return num * sum_board(board)
    return -1

def part2(nums, boards):
    n = 0
    board_idx = list(range(len(boards)))
    while len(board_idx) > 0:
        boards = mark_cells(boards, nums[n])
        for b in board_idx:
            
            if check_board(boards[b]):
                if len(board_idx) > 1:
                    board_idx.remove(b)
                else:
                    break
        else:
            n += 1
            continue
        break
    return sum_board(boards[board_idx[0]]) * nums[n]

if __name__ == "__main__":
    with open('4.txt') as f:
        lines = [x.strip() for x in f.readlines()]
    nums, boards = parse_boards(lines)
    print(part1(nums, boards))
    print(part2(nums, boards))
