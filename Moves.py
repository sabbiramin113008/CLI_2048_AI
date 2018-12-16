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
    [0, 4, 0, 0],
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


def populate_left_move(row):
    length = len(row)
    req_length = 4 - length
    for this in range(0, req_length):
        row.append(0)
    return row


def populate_right_move(row):
    length = len(row)
    req_length = 4 - length
    for this in range(0, req_length):
        row.insert(0, 0)
    return row


def move_left(row):
    for pos in range(3, 0, -1):
        temp, temp_minus = left_temp_var(row[pos], row[pos - 1])
        row[pos - 1] = temp
        row[pos] = temp_minus
    null_row = [cell for cell in row if cell is not 0]
    final_row = populate_left_move(null_row)
    return (final_row)


def move_right(row):
    for pos in range(3, 0, -1):
        temp, temp_minus = left_temp_var(row[pos], row[pos - 1])
        row[pos - 1] = temp
        row[pos] = temp_minus
    null_row = [cell for cell in row if cell is not 0]
    final_row = populate_right_move(null_row)
    return final_row


def board_move_left(boards):
    return [move_left(row) for row in boards]


def board_move_right(boards):
    return [move_right(row) for row in boards]


def convert_to_columns(boards):
    return [
        [boards[x][0] for x in range(0, 4)],
        [boards[x][1] for x in range(0, 4)],
        [boards[x][2] for x in range(0, 4)],
        [boards[x][3] for x in range(0, 4)]
    ]


def convert_to_boards(boards):
    return [
        [boards[x][0] for x in range(0, 4)],
        [boards[x][1] for x in range(0, 4)],
        [boards[x][2] for x in range(0, 4)],
        [boards[x][3] for x in range(0, 4)]
    ]


def board_move_up(boards):
    col_boards = convert_to_columns(boards)
    up_movement = board_move_left(col_boards)
    row_boards = convert_to_boards(up_movement)
    return row_boards


def board_move_down(boards):
    col_boards = convert_to_columns(boards)
    down_movement = board_move_right(col_boards)
    row_boards = convert_to_boards(down_movement)
    return row_boards


def print_board(boards):
    print("-------2048-----------\n")
    print("----------------------------")
    for row in range(0, 4):
        print("|      |      |      |      |")
        row_printer = ' '
        for column in range(0, 4):
            # if self.boards[row][column] == 0:
            #     cell_print = "      "
            # else:
            cell_print = str(boards[row][column]).center(6)
            if column == 3:
                row_printer = "{}{}|".format(row_printer, cell_print)
            else:
                row_printer = "{}{}{}".format(row_printer, cell_print, "|")
        print(row_printer)
        print("|      |      |      |      |")
        if row < 3:
            print("----------------------------")
    print("----------------------------")


# col_boards = (convert_to_columns(board))
# print(convert_to_boards(col_boards))

# board_up = board_move_up(board)
# print(board_up)
# print_board(board_up)

print_board(board_move_down(board))

# print(board_move_left(board))
# print (board_move_right(board))

#
# print(move_left(row_three))
# print(move_right(row_four))
