# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 15 Dec 2018
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

from Board import CheckerBoard

if __name__ == "__main__":
    val_board = [
        [16, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [256, 14, 15, 16]
    ]
    checker_board = CheckerBoard(val_board)
    checker_board.print_board()
'''
print('\n                                   Your score: ' + str(score))
	for y in range(0,4):
		tempstring = ' '
		for x in range(0,4):
			if board[y][x] == 0:
				toprint = '    '
			else:
				toprint = str(board[y][x])
				if board[y][x] < 1000:
					toprint = ' ' + toprint
				if board[y][x] < 100:
					toprint = toprint + ' '
				if board[y][x] < 10:
					toprint = ' ' + toprint
			if x == 3:
				tempstring = tempstring + toprint
			else:
				tempstring = tempstring + toprint + ' | '
		print(tempstring)
		if y < 3:
			print(' --------------------------')
	print()

'''