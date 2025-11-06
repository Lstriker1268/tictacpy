# Code that ChatGPT came up with. MIGHT DELETE LATER.
from ai import best_move, winner, is_full

board = [' ' for _ in range(9)]

def print_board(b):
    print(f"{b[0]} | {b[1]} | {b[2]}")
    print("--+---+--")
    print(f"{b[3]} | {b[4]} | {b[5]}")
    print("--+---+--")
    print(f"{b[6]} | {b[7]} | {b[8]}")
    print()

while True:
    print_board(board)

    # Check if game over
    if winner(board) or is_full(board):
        break

    # Human move
    move = int(input("Your move (0-8): "))
    if board[move] != ' ':
        print("Invalid move. Try again.")
        continue
    board[move] = 'O'

    # Check again
    if winner(board) or is_full(board):
        break

    # AI move
    ai_move = best_move(board)
    board[ai_move] = 'X'
    print(f"AI chose {ai_move}")

# Game over
print_board(board)
w = winner(board)
if w:
    print(f"{w} wins!")
else:
    print("It's a draw!")
