# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 15 Dec 2018
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

from Templates import template_board


class CheckerBoard:
    def __init__(self, boards):
        self.boards = boards
        self.template_board = template_board


    def print_board(self, final_score=None):
        for row in range(0, 4):
            row_printer = ' '
            for column in range(0, 4):
                if self.boards[row][column] == 0:
                    cell_print = "    "
                else:
                    cell_print = str(self.boards[row][column]).center(4)
                if column == 3:
                    row_printer = "{}{}".format(row_printer, cell_print)
                else:
                    row_printer = "{}{}{}".format(row_printer, cell_print, "|")
            print(row_printer)
            if row < 3:
                print("--------------------")
