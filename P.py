# -*- coding: utf-8 -*-
"""
author: S.M. Sabbir Amin
data: 12/16/2018
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

import random
from Moves import *

# while (input() != 'q'):
#     print(random.randint(0, 9))

boards = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
temp = boards
for i in range(0, 20):
    status, score = (populate_board(temp))
    print ("Status: {}".format(status))
    if status:
        temp = score
        print("POST Board: {}".format(score))
    else:
        print("Error")
