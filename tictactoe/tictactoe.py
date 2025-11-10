"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for piece in row:
            if piece == X:
                x_count += 1
            if piece == O:
                o_count += 1

    if x_count == o_count:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []

    for row, row_data in enumerate(board):
        for col, piece in enumerate(row_data):
            if piece == EMPTY:
                moves.append((row, col))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action in actions(board):
        # make a copy of the board
        new_board = copy.deepcopy(board)
        # make the move
        r, c = action
        new_board[r][c] = player(board)
        # return the board
        return new_board
    else:
        raise Exception


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
