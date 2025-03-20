# Thaw Han, Achal Mohandas
# 03/05/2025
# Description: This program creates a rectangle object and allows the user to move the rectangle in the grid. The user can move the rectangle up, down, left, or right. The program will display the grid after each move. The user can quit the program by entering '5'. The program will display an error message if the user tries to move the rectangle out of bounds. The program will also display an error message if the user enters an invalid choice.

from rectangle import Rectangle
import check_input

def display_grid(grid):
    """
    Display the grid.
    Args:
        grid: 2D list representing the grid.
    """
    for row in grid:
        print(' '.join(row))    # join elements of the list with a space
    print()

def reset_grid(grid):
    """
    Reset the grid to its initial state.
    Args:
        grid: 2D list representing the grid.
    """
    for i in range(len(grid)):  # iterate through each row
        for j in range(len(grid[i])):  # iterate through each column
            grid[i][j] = '.'

def place_rect(grid, rect):
    """
    Place the rectangle on the grid.
    Args:
        grid: 2D list representing the grid.
        rect: Rectangle object to place on the grid.
    """
    x, y = rect.get_coords()    # get the coordinates of the rectangle
    width, height = rect.get_dimensions()   # get the dimensions of the rectangle
    for i in range(y, y + height):  # iterate through the rows
        for j in range(x, x + width):   # iterate through the columns
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]):    # check if the coordinates are within the grid
                grid[i][j] = '*'  

def main():
    width = check_input.get_int_range("Enter the rectangle wdith (1-5): ", 1, 5) # get the width of the rectangle
    height = check_input.get_int_range("Enter the rectange height (1-5): ", 1, 5)   # get the height of the rectangle

    rect = Rectangle(width, height)
    grid = [['.' for _ in range(20)] for _ in range(20)]    # create a 20x20 grid

    place_rect(grid, rect) # place the rectangle on the grid
    display_grid(grid) # display the grid

    while True:
        print("Enter Direction:")   # display the menu
        print("""
        1. Move up
        2. Move down
        3. Move left
        4. Move right
        5. Quit
        """)

        choice = input("Enter choice: ")  # get the user's choice

        if choice == '1':  # move the rectangle up
            if rect.y > 0:
                rect.move_up()
            else:
                print("Error: Cannot move up, out of bounds.")
        
        elif choice == '2': # move the rectangle down
            if rect.y + rect.height < 20:
                rect.move_down()
            else:
                print("Error: Cannot move down, out of bounds.")
        
        elif choice == '3': # move the rectangle left
            if rect.x > 0:
                rect.move_left()
            else:
                print("Error: Cannot move left, out of bounds.")

        elif choice == '4': # move the rectangle right
            if rect.x + rect.width < 20:
                rect.move_right()
            else:
                print("Error: Cannot move right, out of bounds.")
        
        elif choice == '5': # quit the program
            break

        else:
            print("Invalid choice. Please try again.") # display an error message for invalid choice

        reset_grid(grid)   # reset the grid
        place_rect(grid, rect) # place the rectangle on the grid
        display_grid(grid) # display the grid



if __name__ == "__main__":
    main()