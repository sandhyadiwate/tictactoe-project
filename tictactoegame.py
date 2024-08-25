def print_board(board):
    """Prints the Tic Tac Toe board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    """Checks if the current player has won."""
    # Check rows, columns and diagonals
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]], # row 1
        [board[1][0], board[1][1], board[1][2]], # row 2
        [board[2][0], board[2][1], board[2][2]], # row 3
        [board[0][0], board[1][0], board[2][0]], # column 1
        [board[0][1], board[1][1], board[2][1]], # column 2
        [board[0][2], board[1][2], board[2][2]], # column 3
        [board[0][0], board[1][1], board[2][2]], # diagonal 1
        [board[2][0], board[1][1], board[0][2]]  # diagonal 2
    ]
    
    for condition in win_conditions:
        if all(s == player for s in condition):
            return True
    return False

def check_draw(board):
    """Checks if the board is full and there's no winner."""
    return all(cell != ' ' for row in board for cell in row)

def get_valid_input(board):
    """Prompts the player to enter a valid move."""
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                raise ValueError
            row, col = divmod(move - 1, 3)
            if board[row][col] != ' ':
                print("The cell is already taken. Choose another one.")
            else:
                return row, col
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def play_game():
    """Main function to play the Tic Tac Toe game."""
    print("Welcome to Tic Tac Toe!")
    print("The board positions are as follows:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")

    while True:
        board = [[' ']*3 for _ in range(3)]
        current_player = 'X'
        while True:
            print_board(board)
            print(f"Player {current_player}'s turn.")
            row, col = get_valid_input(board)
            board[row][col] = current_player
            
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            if check_draw(board):
                print_board(board)
                print("The game is a draw!")
                break
            
            current_player = 'O' if current_player == 'X' else 'X'
        
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    play_game()
