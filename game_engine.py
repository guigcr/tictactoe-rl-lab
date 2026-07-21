"""
game_engine.py

Core Tic-Tac-Toe game engine.

Board representation:
    - 3x3 numpy integer array
    - 1  -> 'X'
    - -1 -> 'O'
    - 0  -> empty cell
"""

import numpy as np


# ---------------------------------------------------------------------------
# Board setup
# ---------------------------------------------------------------------------

def create_empty_board():
    """Return an empty 3x3 Tic-Tac-Toe board as an int numpy array of zeros."""
    matriz = np.zeros((3, 3), dtype=int)


def encode_player(player):
    """Return the integer encoding for 'X', 'O', or 'empty'."""
    if player == 'X':
        return 1
    elif player == 'O':
        return -1
    elif player == 'empty':
        return 0


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------

def print_board(board):
    """Print the 3x3 board using X, O, and . characters."""
    for i in range(3):
        linha = []
        for j in range(3):
            if board[i][j] == 1:
                linha.append("X")
            elif board[i][j] == -1:
                linha.append("O")
            else:
                linha.append(".")
        print(" ".join(linha))


# ---------------------------------------------------------------------------
# Cell / move utilities
# ---------------------------------------------------------------------------

def is_cell_empty(board, row, col):
    """Return True if board[row, col] is empty (0), else False."""
    if board[row][col] == 0:
        return True
    else:
        return False


def place_move(board, row, col, player):
    """Place player's mark at (row, col) and return the new board."""
    if not is_cell_empty(board, row, col):
        raise ValueError("Cell is already occupied")

    board_new = board.copy()
    board_new[row, col] = player

    return board_new


def get_legal_moves(board):
    """Return a list of (row, col) tuples for all empty cells on the board."""
    lista = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                lista.append((i, j))
    return lista


# ---------------------------------------------------------------------------
# Win / draw checks
# ---------------------------------------------------------------------------

def check_row_win(board, player):
    """Return True if `player` has three-in-a-row across any row of `board`."""
    for row in board:
        if np.all(row == player):
            return True
    return False


def check_column_win(board, player):
    """Return True if `player` has three-in-a-row in any column of `board`."""
    for col in range(3):
        if np.all(board[:, col] == player):
            return True
    return False


def check_main_diagonal_win(board, player):
    """Return True if `player` occupies all three main-diagonal cells."""
    soma = 0

    for i in range(3):
        if board[i][i] == player:
            soma += 1

    return soma == 3


def check_anti_diagonal_win(board, player):
    """Return True if `player` occupies all three anti-diagonal cells of the 3x3 board."""
    soma = 0
    for i in range(3):
        if board[i][2 - i] == player:
            soma += 1

    return soma == 3


def is_winner(board, player):
    """Return True if `player` has won via row, column, or either diagonal."""
    return (
        check_column_win(board, player)
        or check_row_win(board, player)
        or check_main_diagonal_win(board, player)
        or check_anti_diagonal_win(board, player)
    )


def is_draw(board):
    """Return True iff the board is full and neither player has won."""
    return (
        np.all(board != 0)
        and not is_winner(board, 1)
        and not is_winner(board, -1)
    )


def get_game_status(board):
    """Return 'X_win', 'O_win', 'draw', or 'ongoing' for the given 3x3 board."""
    if is_winner(board, 1):
        return "X_win"
    elif is_winner(board, -1):
        return "O_win"
    elif is_draw(board):
        return "draw"
    else:
        return "ongoing"


# ---------------------------------------------------------------------------
# Turn management
# ---------------------------------------------------------------------------

def get_current_player(board):
    """Infer whose turn it is by comparing the count of X's and O's on the board."""
    sum_1 = 0
    sum_2 = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                sum_1 += 1
            elif board[i][j] == -1:
                sum_2 += 1

    if sum_1 == sum_2:
        return 1
    else:
        return -1


def switch_player(player):
    """Return the opponent of `player` (1 <-> -1)."""
    if player == 1:
        return -1
    else:
        return 1


# ---------------------------------------------------------------------------
# Game loops
# ---------------------------------------------------------------------------

def play_hardcoded_game(moves):
    """Play a predetermined sequence of (row, col) moves and return the final board and status."""
    board = np.zeros((3, 3), dtype=int)

    player = 1

    for row, col in moves:
        board = place_move(board, row, col, player)

        status = get_game_status(board)

        if status != "ongoing":
            return board, status

        player = switch_player(player)

    return board, "ongoing"


def play_interactive_game():
    """Play a game interactively via terminal input, printing the board after each move."""
    board = np.zeros((3, 3), dtype=int)
    player = 1

    while True:
        for row in board:
            linha = []
            for cell in row:
                if cell == 1:
                    linha.append("X")
                elif cell == -1:
                    linha.append("O")
                else:
                    linha.append(".")
            print(" ".join(linha))

        row, col = map(int, input().split())

        try:
            board = place_move(board, row, col, player)
        except ValueError:
            continue

        status = get_game_status(board)

        if status != "ongoing":
            for row in board:
                linha = []
                for cell in row:
                    if cell == 1:
                        linha.append("X")
                    elif cell == -1:
                        linha.append("O")
                    else:
                        linha.append(".")
                print(" ".join(linha))

            return status

        player = switch_player(player)


if __name__ == "__main__":
    play_interactive_game()
