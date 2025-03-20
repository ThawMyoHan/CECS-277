# Thaw Han, Achal Mohandas
# 03/11/2025
# Descrption: This program is a text-based game where the player must defeat 3 dragons. The player can choose to attack with an arrow or a sword. The player can also choose to attack a dragon with a basic attack or a special attack. The player wins if they defeat all 3 dragons. The player loses if their health points reach 0.

import random
import check_input
from hero import Hero
from dragon import Dragon
from fire import FireDragon
from flying import FlyingDragon

def main():
    """
    The main function of the game.
    """
    name = input("What is your name, challenger?\n") # get the name of the player
    print(f"Welcome to the Dragon Training, {name}!\nYou must defeat 3 dragons.") 
    
    hero = Hero(name, 50) # create a Hero object with 50 health points

    dragons = [     # create a list of Dragon objects
        Dragon("Deadly Naddler", 10),
        FireDragon("Gronckle", 15),
        FlyingDragon("Timberjack", 20)
    ]

    while hero.hp > 0 and dragons:  # while the hero's health points are greater than 0 and there are dragons left
        print(f"\n{hero}")  # print the hero's health points

        for i, dragon in enumerate(dragons): # iterate through the list of dragons
            print(f"{i + 1}. {dragon}")

        choice = check_input.get_int_range((("\nChoose a dragon to attack: ")), 1, len(dragons)) - 1 # get the index of the dragon the player wants to attack

        dragon = dragons[choice] # get the dragon object from the list of dragons

        print("\nAttack with:") # print the attack options
        print("""
        "1. Arrow (1 D12) "
        "2. Sword (2 D6) "
        """)
        
        attack_choice = check_input.get_int_range("Enter the number of the attack: ", 1, 2) # get the attack choice from the player

        if attack_choice == 1: # if the player chooses to attack with an arrow
            print(hero.arrow_attack(dragon))

        else:
            print(hero.sword_attack(dragon))

        if dragon.hp == 0: # if the dragon's health points reach 0
            print(f"{dragon.name} has been defeated!") 
            dragons.remove(dragon)  # remove the dragon from the list of dragons

        if dragons: # if there are dragons left
            attacking_dragon = random.choice(dragons) # choose a random dragon to attack the hero
            attack_type = random.choice(["basic", "special"]) # choose a random attack type
            if attack_type == "basic": # if the attack type is basic
                print(attacking_dragon.basic_attack(hero))

            else: # if the attack type is special
                print(attacking_dragon.special_attack(hero))

    if hero.hp > 0: # if the hero's health points are greater than 0
        print("Congratulations! You have defeated all 3 dragons, you have passed the trials!")

    else:   # if the hero's health points are less than or equal to 0
        print("You have been defeated by the dragons!")

if __name__ == "__main__":
    """
    Calls the main function.
    """
    main()