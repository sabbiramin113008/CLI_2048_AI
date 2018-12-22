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
                    u_flag, temp = populate_board(u_board)
                    if u_flag:
                        print_board(temp)
                    else:
                        print_board(u_board)
                elif key_press == 'd':
                    d_board = board_move_down(temp)
                    d_flag, temp = populate_board(d_board)
                    if d_flag:
                        print_board(temp)
                    else:
                        print_board(d_board)
                elif key_press == 'l':
                    l_board = board_move_left(temp)
                    l_flag, temp = populate_board(l_board)
                    if l_flag:
                        print_board(temp)
                    else:
                        print_board(l_board)
                elif key_press == 'r':
                    r_board = board_move_right(temp)
                    r_flag, temp = populate_board(r_board)
                    if r_flag:
                        print_board(temp)
                    else:
                        print_board(r_board)
                else:
                    pass
