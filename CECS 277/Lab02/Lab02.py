# Thaw Myo Han, Achal Mohandas
# 02/04/2025
# A basic Rock Paper Scissors game using Functions

import check_input
import random

# Display Weapon Menu
def weapon_menu():
    """
    Display the weapon menu and get the user's choice.
    Args:
        None
    Returns:
        str: The user's weapon choice.
    """

    while True:         # Loop until valid input
        print("Choose your weapon:")        # Display menu
        print("""
            R. Rock
            P. Paper
            S. Scissors
            B. Back
            """)
        
        user_weapon = input("Enter your choice: ").upper()       # Get user input and convert to uppercase

        weapons = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors', 'B': 'Back'}       # Dictionary of weapon choices

        if user_weapon in weapons:     # Check if input is valid
            print(f"You chose {weapons[user_weapon]}.")
            return user_weapon

        else:
            print("Invalid choice. Please try again.")
    

# Computer Weapon Choice
def comp_weapon():
    """
    Generate a random weapon choice for the computer.
    Args:
        None
    Returns:
        str: The computer's weapon choice.
    """

    comp_weapon_list = ["R", "P", "S"]      # List of possible computer choices
    comp_weapon_choice = random.choice(comp_weapon_list)        # Randomly select a choice from the list

    if comp_weapon_choice == "R":       # Display computer choice
        print("Computer chose Rock.")

    elif comp_weapon_choice == "P":
        print("Computer chose Paper.")

    elif comp_weapon_choice == "S":
        print("Computer chose Scissors.")

    return comp_weapon_choice

# Determine Winner
def find_winner(player, comp):
    """
    Determine the winner of the game.
    Args:
        player (str): The player's weapon choice.
        comp (str): The computer's weapon choice.
    Returns:
        int: 0 if tie, 1 if player wins, 2 if computer wins.
    """

    if player == comp:      # Check if tie
        print("It's a tie!")
        return 0

    elif (player == "R" and comp == "S") or (player == "P" and comp == "R") or (player == "S" and comp == "P"):     # Check if player wins
        print("You win!")
        return 1
    
    else:       # Computer wins
        print("Computer wins!")
        return 2

# Display Scores
def display_scores(p_score, c_score):
    """
    Display the scores of the player and computer.
    Args:
        p_score (int): The player's score.
        c_score (int): The computer's score.
    Returns:
        None
    """

    print("Player: ", p_score)
    print("Computer: ", c_score)

# Display Main Menu
def main():

    p_score = 0
    c_score = 0

    while True:     # Loop until user chooses to quit
        print("RPS Game Menu:")     # Display menu
        print("""
            1. Play Game
            2. Show Score
            3. Quit
            """)


        user_input = check_input.get_int("Enter your choice: ")     # Get user input

        if user_input == 1:     # If user chooses to play game
            while True:
                p_weapon = weapon_menu()
                if p_weapon == "B":         # If user chooses to go back
                    break

                c_weapon = comp_weapon()

                winner = find_winner(p_weapon, c_weapon)        # Determine winner

                if winner == 1:       # Update scores based on winner
                    p_score += 1
                elif winner == 2:
                    c_score += 1



        elif user_input == 2:       # If user chooses to show score
            display_scores(p_score, c_score)

        elif user_input == 3:       # If user chooses to quit
            print("Final Score: ")
            display_scores(p_score, c_score)
            exit()

        else:    # If user input is invalid
            print("Invalid choice. Please try again.")


main()