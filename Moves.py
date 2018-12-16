# -*- coding: utf-8 -*-
"""
author: S.M. Sabbir Amin
data: 12/16/2018
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
import pprint

board = [
    [2, 0, 0, 2],
    [4, 4, 8, 8],
    [0, 0, 0, 0],
    [0, 0, 2, 4]
]
row_one = [2, 0, 0, 2]
row_two = [4, 4, 8, 8]
row_three = [0, 0, 0, 0]
row_four = [256, 256, 256, 256]


def left_temp_var(pos, pos_minus):
    if pos > 0 and pos_minus == 0:
        # print("Logic 1")
        return pos, 0
    elif pos == 0 and pos_minus > 0:
        # print("Logic 2")
        return pos_minus, 0
    elif pos == pos_minus:
        # print("Logic 3")
        return pos + pos_minus, 0
    elif pos != pos_minus:
        # print("Logic 4")
        return pos_minus, pos


def populate_with_zero(row):
    length = len(row)
    req_length = 4 - length
    for this in range(0, req_length):
        row.append(0)
    return row


def move_left(row):
    for pos in range(3, 0, -1):
        temp, temp_minus = left_temp_var(row[pos], row[pos - 1])
        row[pos - 1] = temp
        row[pos] = temp_minus
    null_row = [cell for cell in row if cell is not 0]
    final_row = populate_with_zero(null_row)
    return (final_row)


def move_right(row):
    reverse_row = row[::-1]
    reverse_right = move_left(reverse_row)
    return reverse_right[::-1]


def board_move_left(boards):
    return [move_left(row) for row in boards]


def board_move_right(boards):
    return [move_right(row) for row in boards]


# print(board_move_left(board))
print (board_move_right(board))

#
# print(move_left(row_three))
# print(move_right(row_four))
