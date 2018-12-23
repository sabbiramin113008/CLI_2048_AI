# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 15 Dec 2018
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
from Moves import *
from Train import *
import time
from Board import CheckerBoard

if __name__ == "__main__":
    boards = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    message_choice = "Press\n 1 to Teaching the AI,\n 2 to Test your AI,\n 3. To Just Play\n  "
    choice = input(message_choice)
    if int(choice) == 1:
        u_name = input("Enter Your Name: ")
        file_name = "{}".format(u_name)

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
                            record_moves(file_name, temp, key_press)
                            print_board(temp)
                        else:
                            print_board(u_board)
                            print("\nInvalid Move..\n")
                    elif key_press == 'd':
                        d_board = board_move_down(temp)
                        d_flag, temp = populate_board(d_board)
                        if d_flag:
                            record_moves(file_name, temp, key_press)
                            print_board(temp)
                        else:
                            print_board(d_board)
                            print("\nInvalid Move..\n")
                    elif key_press == 'l':
                        l_board = board_move_left(temp)
                        l_flag, temp = populate_board(l_board)
                        if l_flag:
                            record_moves(file_name, temp, key_press)
                            print_board(temp)
                        else:
                            print_board(l_board)
                            print("\nInvalid Move..\n")
                    elif key_press == 'r':
                        r_board = board_move_right(temp)
                        r_flag, temp = populate_board(r_board)
                        if r_flag:
                            record_moves(file_name, temp, key_press)
                            print_board(temp)
                        else:
                            print_board(r_board)
                            print("\nInvalid Move..\n")
                    else:
                        pass
    elif int(choice) == 2:
        profile_name = input("Enter Your Profile Name: ")
        msg, scale = train_model(profile_name)
        print("Loading Your Model's Accuracy....")
        print(msg)
        goto_sleep()

        status, init_board = populate_board(boards)
        print_board(init_board)
        if status:
            flag, first_board = populate_board(boards)
            time.sleep(10)
            if flag:
                temp = first_board
                print_board(first_board)
                for i in range(0, 20):
                    key_press = predict_move(boards=temp, scale=scale, profile_name=profile_name)
                    goto_sleep()
                    print (key_press)

                    if key_press == 'u':
                        u_board = board_move_up(temp)
                        u_flag, temp = populate_board(u_board)
                        if u_flag:
                            # record_moves(file_name, temp, key_press)
                            print_board(temp)
                        else:
                            print_board(u_board)
                            print("\nInvalid Move..\n")
                    elif key_press == 'd':
                        d_board = board_move_down(temp)
                        d_flag, temp = populate_board(d_board)
                        if d_flag:
                            # record_moves(file_name, temp, key_press)
                            print_board(temp)
                        else:
                            print_board(d_board)
                            print("\nInvalid Move..\n")
                    elif key_press == 'l':
                        l_board = board_move_left(temp)
                        l_flag, temp = populate_board(l_board)
                        if l_flag:
                            # record_moves(file_name, temp, key_press)
                            print_board(temp)
                        else:
                            print_board(l_board)
                            print("\nInvalid Move..\n")
                    elif key_press == 'r':
                        r_board = board_move_right(temp)
                        r_flag, temp = populate_board(r_board)
                        if r_flag:
                            # record_moves(file_name, temp, key_press)
                            print_board(temp)
                        else:
                            print_board(r_board)
                            print("\nInvalid Move..\n")
                    else:
                        pass
