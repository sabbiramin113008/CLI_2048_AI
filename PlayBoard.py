# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 15 Dec 2018
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

from Board import CheckerBoard

if __name__ == "__main__":
    val_board = [
        [16, 0, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [256, 14, 15, 16]
    ]
    checker_board = CheckerBoard(val_board)
    checker_board.print_board()
