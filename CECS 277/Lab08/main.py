# Thaw Han, Achal Mohandas
# 03/18/25
# Description: This program is a Pokemon battle simulator. The user will choose a Pokemon to battle with and will fight against 3 random Pokemon. The user will choose an attack type and a move to attack the opponent. The opponent will randomly choose an attack type and a move to attack the user. The battle will continue until the user's Pokemon faints or the user defeats all the opponent's Pokemon.

from fire import Fire
from water import Water
from grass import Grass
import random
import check_input

def choose_pokemon():
    """
    This function will prompt the user to choose a Pokemon to battle with.
    The user will choose between Charmander, Squirtle, and Bulbasaur.
    The function will return the Pokemon object that the user chose.
    """
    print("Select the pokemon that you will battle with.")      # Prompt the user to choose a Pokemon
    print("""
    1. I choose you, Charmander!
    2. Squirtle! GO!
    3. We can do it together, Bulbasaur!
    """)    # Display the options for the user to choose from
    choice = check_input.get_int_range("Please choose a pokemon: ", 1, 3)   # Get the user's choice

    if choice == 1:    # If the user chose Charmander
        return Fire("Charmander")
    elif choice == 2: # If the user chose Squirtle
        return Water("Squirtle")
    else:  # If the user chose Bulbasaur
        return Grass("Bulbasaur")
    
def choose_attack_type():
    """
    This function will prompt the user to choose an attack type.
    The user will choose between Normal and Special.
    The function will return the attack type that the user chose.
    """
    print("Choose an Attack Type:")     # Prompt the user to choose an attack type
    print("""
    1. Normal
    2. Special
    """)

    choice = check_input.get_int_range("Enter attack type: ", 1, 2)     # Get the user's choice

    if choice == 1:     # If the user chose Normal
        return "normal"
    else:   # If the user chose Special
        return "special"

def choose_move(pokemon, attack_type):
    """
    This function will prompt the user to choose a move to attack the opponent.
    The user will choose between 2 moves.
    The function will return the move that the user chose.
    Parameters:
    - pokemon: Pokemon object
    - attack_type: str
    """
    if attack_type == "normal":     # If the attack type is Normal
        print(pokemon.get_normal_menu())
    else:  # If the attack type is Special
        print(pokemon.get_special_menu())
    
    move = check_input.get_int_range("Enter your move: ", 1, 2)    # Get the user's choice
    return move

def main():
    """
    This function will simulate a Pokemon battle between the user and 3 random Pokemon.
    The user will choose a Pokemon to battle with and will fight against 3 random Pokemon.
    The user will choose an attack type and a move to attack the opponent.
    The opponent will randomly choose an attack type and a move to attack the user.
    The battle will continue until the user's Pokemon faints or the user defeats all the opponent's Pokemon.
    """
    print("PROF OAK: Hello Trainer! Today you're off to fight your first battle of 1 vs. 3 pokemon.")

    opponent_pokemons = [random.choice([Fire(), Water(), Grass()]) for _ in range(3)]   # Create 3 random Pokemon for the opponent
    
    for i, pokemon in enumerate(opponent_pokemons):   # Display the opponent's Pokemon
        print(f"{i + 1}. {pokemon}")

    user_pokemon = choose_pokemon()
    
    print("  -- TRAINER BATTLE --")
    while user_pokemon.hp > 0 and len(opponent_pokemons) > 0:   # Continue the battle until the user's Pokemon faints or the user defeats all the opponent's Pokemon
        opponent_pokemon = opponent_pokemons[0]
        print(f"TRAINER: I choose you: \n{opponent_pokemon}")

        print(f"\n{user_pokemon}")

        # User's turn
        attack_type = choose_attack_type()  # Get the user's attack type
        move = choose_move(user_pokemon, attack_type)  # Get the user's move
        result = user_pokemon.attack(opponent_pokemon, attack_type, move) # Perform the attack
        print(result)
        
        if opponent_pokemon.hp <= 0:   # If the opponent's Pokemon faints
            print(f"{opponent_pokemon._name} fainted!")
            print("TRAINER: NOOOOO! You defeated my pokemon!")
            opponent_pokemons.pop(0)
        else:
            # Opponent's turn
            attack_type = random.choice(["normal", "special"]) # Randomly choose the opponent's attack type
            move = random.choice([1, 2])   # Randomly choose the opponent's move
            result = opponent_pokemon.attack(user_pokemon, attack_type, move)  # Perform the attack
            print(result)
            print("")

    if user_pokemon.hp > 0:  # If the user's Pokemon has more than 0 HP
        print("Congratulations! You defeated all the opponent's Pokemon!")
    else:   # If the user's Pokemon has 0 HP
        print("TRAINER: HA! I defeated you, come back when you get a better Pokemon...")


if __name__ == "__main__":
    main()