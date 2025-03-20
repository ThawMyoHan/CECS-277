# Thaw Han, Achal Mohandas
# 02/11/2025
# A Battleship Game that allows user to input coordinates onto a 5x5 grid to sink the enemy ship.
import random
import check_input

# Display the board with row and column labels
def display_board(board):
    """
    Display the board with row and column labels.
    Args:
        board: 2D list representing the game board.
    Returns:
        None
    """
    print("  1 2 3 4 5")
    row_labels = ["A", "B", "C", "D", "E"]
    for i, row in enumerate(board):     # i = 0, row = ["~", "~", "~", "~", "~"]
        print(row_labels[i], " ".join(row))

# Reset the game by creating a new board and solution
def reset_game():
    """
    Reset the game by creating a new board and solution.
    Args:
        None
    Returns:
        grid: 2D list representing the game board.
        sol: list of tuples representing the solution
    """
    grid = [
        ["~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~"]
    ]
    
    row = random.randint(0,3)      # Randomly generate the solution
    col = random.randint(0,3)
    sol = [(row, col), (row, col + 1), (row + 1, col), (row + 1, col + 1)]      
    return grid,sol

# Get the row letter from the user and validate it
def get_row():
    """
    Get the row letter from the user and validate it.
    Args:
        None
    Returns:
        The index of the row letter in the list ["A", "B", "C", "D", "E"]
    """
    letter = ["A", "B", "C", "D", "E"]
    row = input("Enter a Row Letter (A-E): ").upper()       
    while row not in letter:        # Check if the input is a valid row letter  
        print("Invalid input - should be a letter between A-E.")
        row = input("Enter a Row Letter (A-E): ").upper()
    return letter.index(row)

# Fire a shot at the specified row and column
def fire_shot(grid,solution, row, col):
    """
    Fire a shot at the specified row and column.
    Args:
        grid: 2D list representing the game board.
        solution: list of tuples representing the solution
        row: integer representing the row index.
        col: integer representing the column index.
    Returns:
        True if the shot is a hit, False otherwise.
    """
    if (row, col) in solution:
        grid[row][col] = '*'    # Hit
        return True
    else:
        grid[row][col] = 'X'   # Miss
        return False
    
# Main function to run the game
def main():

    while True:     # Loop to play multiple games
        board, solution = reset_game()
        hits = 0

        while hits < 4:     # Loop to play a single game
            display_board(board)
            print("""Menu:
            1. Fire Shot
            2. Show Solution
            3. Quit
            """)

            choice = check_input.get_int("Enter your choice: ")

            if choice == 1:     # Fire Shot
                    row = get_row()
                    col = check_input.get_int_range("Enter a Column Number (1-5): ", 1, 5) - 1
                    if board[row][col] in ['*', 'X']:       # Check if the location has already been fired at
                        print("You already fired at this location. Try again.")

                    else:
                        if fire_shot(board, solution, row, col):        # Check if the shot is a hit
                            print("Hit!")
                            hits += 1

                        else:
                            print("Miss!")

            elif choice == 2:   # Show Solution
                print("Showing Solution")
                for r, c in solution:
                    board[r][c] = '*'
                display_board(board)
                break

            elif choice == 3:       # Quit
                print("Goodbye! Thank you for playing.")
                exit()

            else:
                print("Invalid choice. Please try again.")
            
        if hits == 4:   # Check if the game is won
                print("Congratulations! You sunk the enemy ship!")

        else:
            print("Game Over. The enemy ship was at:")      # Show solution if the game is lost
            for r, c in solution:
                board[r][c] = '*'
            display_board(board)


main()