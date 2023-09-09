# Initialize the Tic Tac Toe board
board = [" " for _ in range(9)]

# Function to print the Tic Tac Toe board
def print_board():
    print("-------------")
    for i in range(0, 9, 3):
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
        print("-------------")

# Function to check if a player has won
def check_win(player):
    # Check rows, columns, and diagonals
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to check if the board is full (tie)
def check_tie():
    return " " not in board

# Main game loop
current_player = "X"
while True:
    print_board()
    print(f"Player {current_player}'s turn. Enter a position (1-9): ", end="")
    try:
        move = int(input()) - 1
        if 0 <= move < 9 and board[move] == " ":
            board[move] = current_player
        else:
            print("Invalid move. Try again.")
            continue
    except ValueError:
        print("Invalid input. Enter a number from 1 to 9.")
        continue

    if check_win(current_player):
        print_board()
        print(f"Player {current_player} wins! Congratulations!")
        break
    elif check_tie():
        print_board()
        print("It's a tie! Good game.")
        break

    # Switch players
    current_player = "O" if current_player == "X" else "X"
