def print_board(board):
    """Prints the Tic-Tac-Toe board in a 3x3 format."""
    print("\nCurrent board:")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()  # Extra newline for readability

def check_winner(board, player):
    """Checks if the given player has won."""
    # Defining possible win conditions
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    # Checking each win condition to see if it matches the player's symbol
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True  # Return early if a win condition is met
    return False

def check_tie(board):
    """Checks if the game is a tie."""
    return " " not in board  # Returns True if there are no empty spots

def get_player_input(player, board):
    """Prompts the player to choose a position and validates it."""
    while True:
        try:
            position = input(f"Player {player}, choose a position (1-9): ").strip()
            if not position.isdigit():
                print("Please enter a valid number.")
                continue
            
            position = int(position) - 1
            if position < 0 or position > 8:
                print("Invalid position. Choose a number between 1 and 9.")
            elif board[position] != " ":
                print("Position already taken. Choose another spot.")
            else:
                return position  # Position is valid and empty
        except ValueError:
            print("Please enter a valid number.")  # Catch any unexpected input errors

def play_game():
    """Main game loop that controls the flow of the Tic-Tac-Toe game."""
    board = [" "] * 9
    current_player = "X"
    
    while True:
        print_board(board)
        position = get_player_input(current_player, board)
        board[position] = current_player  # Update board with the player's move
        
        # Check for a win or tie after each move
        if check_winner(board, current_player):
            print_board(board)
            print(f"Congratulations, Player {current_player} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch player after each valid move
        current_player = "O" if current_player == "X" else "X"

    # Replay option
    replay = input("Play again? (y/n): ").strip().lower()
    if replay == "y":
        play_game()
    else:
        print("Thanks for playing! Come back soon!")

# Start the game
play_game()
