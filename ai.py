# What ChatGPT came up with. MIGHT EDIT LATER.
import math

def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    return None

def is_full(board):
    return ' ' not in board

def minimax(board, is_maximizing):
    win = winner(board)
    if win == 'X':
        return 1
    elif win == 'O':
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = 'X'
            score = minimax(board, False)
            board[move] = ' '
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = 'O'
            score = minimax(board, True)
            board[move] = ' '
            best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in available_moves(board):
        board[i] = 'X'
        score = minimax(board, False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    return move
