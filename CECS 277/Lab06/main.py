# Thaw Han, Achal Mohandas
# 03/05/2025
# Description: This program creates a Yahtzee game. The player can roll the dice and the program will display the result. The program will display a message if the player gets a three of a kind, a series, or a pair. The program will also display a message if the player does not get any of the above combinations. The player can continue playing the game or quit. The program will display the final score when the player quits the game.

from player import Player
import check_input

def take_turn(player):
    """
    Take a turn in the game.
    Args:
        player: Player object representing the player.
    """
    player.roll_dice()  # roll the dice
    print(player)

    if player.has_three_of_a_kind(): # check if the player has three of a kind
        print("You got 3 of a kind!")
    
    elif player.has_series():  # check if the player has a series
        series = player.has_series()
        print(f"You got a series of 3!")
    
    elif player.has_pair():   # check if the player has a pair
        print("You got a pair!")
    
    else:
        print("Aww. Too Bad!") # display message if the player does not get any of the above combinations

    print(f"Score: {player.points}") # display the updated score

def main():
    player = Player()  # create a player object

    print(" - Yahtzee - ")

    while True: # loop to take turns
        take_turn(player)  # take a turn
        if not check_input.get_yes_no("Do you want to continue? (y/n): "): # check if the player wants to continue
            print("")
            break
    
    print("Game Over!")
    print(f"Final score: {player.points}")

if __name__ == "__main__":
    main()