# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 15 Dec 2018
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
from Moves import *
from Board import CheckerBoard

if __name__ == "__main__":
    boards = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    status, init_board = populate_board(boards)
    print_board(init_board)
    if status:
        flag, first_board = populate_board(init_board)
        if flag:
            temp = first_board
            print_board(first_board)
            while (1):
                key_press = input()
                if key_press == 'u':
                    u_board = board_move_up(temp)
                    temp = populate_board(u_board)[1]
                    print_board(temp)
                elif key_press == 'd':
                    d_board = board_move_down(temp)
                    temp = populate_board(d_board)[1]
                    print_board(temp)
                elif key_press == 'l':
                    l_board = board_move_left(temp)
                    temp = populate_board(l_board)[1]
                    print_board(temp)
                elif key_press == 'r':
                    isValid, r_board = board_move_right(temp)
                    temp = populate_board(r_board)[1]
                    print_board(temp)
                else:
                    pass
