board = [...]

# print board as a 3x3 table
def print_board():...

# This function returns True if board[row][col] is currently unmarked
# and thus can be chosen by a player. It returns False otherwise
def check_mark(row, column, player):...

# This function returns True if the indicated player has won the game
# It returns False otherwise
# For player 1, winning occurs board has a complete row, column or
# diagonal of X
# For player 2, winning occurs when the board has a complete row, column or
# diagonal of 0
def check_win(player):...


def place_mark(param, param1, param2):
    pass


def main():
    print('Testing print_board')
    print_board()

    print('before place_mark, check mark for 1, 1 is ', check_mark(1, 1))
    place_mark(1, 1, 1)
    print('after place_mark, check_mark for 1, 1 is ',check_mark(1, 1))
    place_mark(0, 2, 2)
    print_board()

main()
