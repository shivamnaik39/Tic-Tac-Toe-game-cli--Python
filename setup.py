
def display_board(board):


    print("\n " *100)


    print("       |       |       ")
    print("   {}   |   {}   |   {}   ".format(board[7] ,board[8], board[9]))
    print("_______|_______|_______")
    print("       |       |       ")
    print("   {}   |   {}   |   {}   ".format(board[4], board[5], board[6]))
    print("_______|_______|_______")
    print("       |       |       ")
    print("   {}   |   {}   |   {}   ".format(board[1], board[2], board[3]))
    print("       |       |       ")


def player_input():
    marker = ''

    while (marker.upper() != 'X') and (marker.upper() != 'O'):
        marker = input("Player1: Choose Either X or O :").upper()

    player1 = marker.upper()

    if player1 == 'X':
        player2 = 'O'

    else:
        player2 = 'X'

    return (player1, player2)


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if board[7] == mark and board[4] == mark and board[1] == mark:
        return True

    elif board[8] == mark and board[5] == mark and board[2] == mark:
        return True

    elif board[9] == mark and board[6] == mark and board[3] == mark:
        return True

    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True

    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True

    elif board[1] == mark and board[2] == mark and board[3] == mark:
        return True

    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True

    elif board[7] == mark and board[5] == mark and board[3] == mark:
        return True

    else:
        return False


import random


def choose_first():
    import random

    f = random.randint(1, 2)

    if f == 1:
        return 'Player1'
    else:
        return 'Player2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose a position (1-9) : "))

    return position


def replay():
    reply = input("Would You Like To Play The Game Again? (y/n) ")

    return reply == 'y'
