

import random

from setup import *



print('Welcome to Tic Tac Toe! \n\n')




while True:

    # set up everything
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    player1_marker, player2_marker = player_input()

    turn = choose_first()

    print(turn, " will start the game.")

    play_game = input("Ready to Play The Game?(y/n):")

    if play_game == 'y':
        game_on = True

    else:
        game_on = False

    # GamePlay

    while game_on:

        if turn == 'player1':

            display_board(board)

            position = player_choice(board)

            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print("\nPLAYER1 HAS WON THE GAME!!")
                game_on = False

            else:
                if full_board_check(board):
                    display_board(board)
                    print("\nTIE GAME!!")
                    game_on = False

                else:
                    turn = 'player2'


        else:

            display_board(board)

            position = player_choice(board)

            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print("\nPLAYER2 HAS WON THE GAME!!")
                game_on = False

            else:
                if full_board_check(board):
                    display_board(board)
                    print("\nTIE GAME!!")
                    game_on = False

                else:
                    turn = 'player1'

    if not replay():
        break
