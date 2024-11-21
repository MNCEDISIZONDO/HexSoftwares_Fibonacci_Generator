import random

#function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

#function to check if a player has won
def checkWin(board, player):
    
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

#function to check if the board is full
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

#function to get the player move
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("This spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

# Function to get the computer's move
def computer_move(board):
    print("Computer's turn...")
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    row, col = random.choice(empty_cells)
    board[row][col] = "O"

# Main function to control the game flow
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    
    while True:
        # Player's move
        player_move(board)
        print_board(board)
        if checkWin(board, "X"):
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        
        # Computer's move
        computer_move(board)
        print_board(board)
        if checkWin(board, "O"):
            print("Computer wins! Better luck next time.")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
