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
    count = 0
    # X starts the game
    for i in range(3):
        count += board[i].count(EMPTY)
    if count == 9:
        return X

    # If there are more X's than O's it is O's turn otherwise X's move
    count_x = 0
    count_o = 0
    for i in range(3):
        count_x += board[i].count(X)
        count_o += board[i].count(O)

    if count_x > count_o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError(f"Invalid move - {action}")
    else:
        new_board = copy.deepcopy(board)
        i, j = action
        new_board[i][j] = player(board)
        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # There are 8 winning combinations
    # 3 Across row 0
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != EMPTY:
        return board[0][0]

    # 3 Across row 1
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != EMPTY:
        return board[1][0]

    # 3 Across row 2
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != EMPTY:
        return board[2][0]

    # 3 diagonal left to right
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]

    # 3 diagonal right to left
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    # 3 down column 0
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != EMPTY:
        return board[0][0]

    # 3 down column 1
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != EMPTY:
        return board[0][1]

    # 3 down column 2
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != EMPTY:
        return board[0][2]

    # No winner
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # All spots are taken
    count = 0
    for i in range(3):
        count += board[i].count(EMPTY)

    if count == 0:
        return True

    # Somebody has won
    if winner(board) is not None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    val = winner(board)

    if val == X:
        return 1
    elif val == O:
        return -1
    else:
        return 0


def max_value(board):
    values = []
    if terminal(board):
        return utility(board)
    else:
        for action in actions(board):
            values.append(min_value(result(board, action)))

    return max(values)


def min_value(board):
    values = []
    if terminal(board):
        return utility(board)
    else:
        for action in actions(board):
            values.append(max_value(result(board, action)))

    return min(values)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    p = player(board)
    v = math.inf if p == O else -math.inf

    values = []
    moves = []
    if terminal(board):
        return None

    for action in actions(board):
        # If current player is X we want to know what min player is going to do
        if p == X:
            values.append(min_value(result(board, action)))
            moves.append(action)

        # If current player is O we want to know what max player is going to do
        else:
            values.append(max_value(result(board, action)))
            moves.append(action)

    # X is max player, O is min player
    if p == X:
        return moves[values.index(max(values))]
    else:
        return moves[values.index(min(values))]