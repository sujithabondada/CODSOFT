# ============================================================
# CodSoft AI Internship — Task 2
# Tic-Tac-Toe AI using Minimax Algorithm
# ============================================================

import math

# ──────────────────────────────────────────────
# Board Setup
# ──────────────────────────────────────────────
def create_board():
    return [' ' for _ in range(9)]

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def print_position_guide():
    print("\n  Position Guide:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("\n")

# ──────────────────────────────────────────────
# Game Logic
# ──────────────────────────────────────────────
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]               # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_board_full(board):
    return ' ' not in board

def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

# ──────────────────────────────────────────────
# Minimax Algorithm (AI Brain)
# ──────────────────────────────────────────────
def minimax(board, is_maximizing):
    # Terminal states
    if check_winner(board, 'X'):  # AI wins
        return 1
    if check_winner(board, 'O'):  # Human wins
        return -1
    if is_board_full(board):      # Draw
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = 'X'
            score = minimax(board, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = 'O'
            score = minimax(board, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = 'X'
        score = minimax(board, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# ──────────────────────────────────────────────
# Main Game Loop
# ──────────────────────────────────────────────
def play_game():
    print("=" * 50)
    print("   CodSoft AI Internship — Task 2")
    print("   Tic-Tac-Toe AI (Minimax Algorithm)")
    print("=" * 50)
    print("\n  You = O    AI = X")
    print_position_guide()

    board = create_board()

    # Ask who goes first
    while True:
        choice = input("Do you want to go first? (yes/no): ").lower().strip()
        if choice in ['yes', 'y']:
            human_first = True
            break
        elif choice in ['no', 'n']:
            human_first = False
            break
        else:
            print("Please type yes or no.")

    human_turn = human_first

    while True:
        print_board(board)

        if human_turn:
            # Human move
            while True:
                try:
                    move = int(input("Your turn! Enter position (1-9): ")) - 1
                    if move < 0 or move > 8:
                        print("Please enter a number between 1 and 9.")
                    elif board[move] != ' ':
                        print("That spot is already taken! Try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Enter a number 1-9.")

            board[move] = 'O'

            if check_winner(board, 'O'):
                print_board(board)
                print("🎉 Congratulations! You won! Amazing!")
                break

        else:
            # AI move
            print("🤖 AI is thinking...")
            move = get_best_move(board)
            board[move] = 'X'
            print(f"🤖 AI played at position {move + 1}")

            if check_winner(board, 'X'):
                print_board(board)
                print("🤖 AI wins! Better luck next time!")
                break

        # Check draw
        if is_board_full(board):
            print_board(board)
            print("🤝 It's a draw! Great game!")
            break

        # Switch turns
        human_turn = not human_turn

    # Play again
    again = input("\nPlay again? (yes/no): ").lower().strip()
    if again in ['yes', 'y']:
        play_game()
    else:
        print("\nThanks for playing! Goodbye! 👋")

# ──────────────────────────────────────────────
if __name__ == "__main__":
    play_game()
