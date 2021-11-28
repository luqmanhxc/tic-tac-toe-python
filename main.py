from IPython.display import clear_output
import random


def display_board(board):
    """
    Clears any board output and prints the current board
    """
    clear_output()

    print(board[1], "|", board[2], "|", board[3])
    print("--+---+--")
    print(board[4], "|", board[5], "|", board[6])
    print("--+---+--")
    print(board[7], "|", board[8], "|", board[9])


def player_input():
    """
    Sets player 1 and 2's markers
    """
    marker = 'wrong'

    while marker not in ['X', 'O']:

        marker = input("Player 1, choose X or O: ").upper()

        if marker not in ['X', 'O']:
            print("Invalid marker. Choose X or O")

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return player1, player2


def place_marker(board, marker, position):
    # Place marker on board
    board[position] = marker


def win_check(board, mark):
    # Check for win conditions
    b = board

    # horizontal wins
    if (b[1] == b[2] == b[3] == mark) or (b[4] == b[5] == b[6] == mark) or (b[7] == b[8] == b[9] == mark):
        return True

    # vertical wins
    elif (b[1] == b[4] == b[7] == mark) or (b[2] == b[5] == b[8] == mark) or (b[3] == b[6] == b[9] == mark):
        return True

    # cross wins
    elif (b[1] == b[5] == b[9] == mark) or (b[3] == b[5] == b[7] == mark):
        return True

    else:
        return False


def choose_first():
    # Randomize starting player
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    # Check if position is valid
    return board[position] == ' '


def full_board_check(board):
    # Check if board is full
    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True


def player_choice(board):
    """
    Player's choice for position on board
    """
    position = 0
    valid_pos = list(range(1, 10))

    while position not in valid_pos or not space_check(board, position):

        position = int(input("Choose position 1 to 9: "))

        if position not in valid_pos:
            print("Invalid position. Choose 1-9.")
        elif not space_check(board, position):
            print("Position taken. Choose another.")

    return position


def replay():
    """
    Replay choice
    """

    choice = 'placeholder'

    while choice not in ['Y', 'N']:
        choice = input("Play again (Y/N): ").upper()

    if choice == 'Y':
        return True
    else:
        return False


print('Welcome to Tic Tac Toe!')

game_on = True

while True:
    # Set the game up here
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(f"{turn} will go first.")

    start_game = input("Ready to play (Y/N)?: ").upper()

    if start_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:

        # Player 1 Turn
        if turn == 'Player 1':

            display_board(board)
            print(f"{turn}'s {player1_marker} Turn")
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print(f"{turn} wins!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("It is a TIE!")
                    game_on = False
                else:
                    turn = 'Player 2'

        else:

            display_board(board)
            print(f"{turn}'s {player2_marker} Turn")
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print(f"{turn} wins!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("It is a TIE!")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
