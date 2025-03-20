from pokemon import Pokemon
import random
import math


class Grass(Pokemon):
    """
    This class will represent a Grass type Pokemon.
    Attributes:
        _battle_table (list): a 2D list of the effectiveness of each type against each other
    Methods:
        __init__(self, name, type): initializes the Pokemon with a name, type, and health points
        get_special_menu(self): returns the special moves that the Grass Pokemon can use
        _special_move(self, opponent, move): performs a special move on the opponent
        attack(self, opponent, type, move): attacks the opponent with the move of the specified type
        __str__(self): returns the string representation of the Pokemon object
    """

    def __init__(self, name=None):
        """
        This is the constructor for the Grass class.
        Parameters:
        - name: str
        """
        names = ["Oddish", "Bellsprout", "Exeggcute"]
        if name is None:
            name = random.choice(names)
        super().__init__(name, 2)  # Grass type is 2

    def get_special_menu(self):
        """
        This function will return the special moves that the Grass Pokemon can use.
        """
        return """    1. Razor Leaf
    2. Solar Beam
        """

    def _special_move(self, opponent, move):
        """
        This function will perform a special move on the opponent.
        Parameters:
        - opponent: Pokemon object
        - move: int
        """
        if move == 1:
            return self._razor_leaf(opponent)
        elif move == 2:
            return self._solar_beam(opponent)
        else:
            return "Invalid move!"

    def _razor_leaf(self, opponent):
        """
        This function will perform the Razor Leaf move on the opponent.
        Parameters:
        - opponent: Pokemon object
        """
        damage = random.randint(3, 5)
        multiplier = self._battle_table[self._poke_type][opponent._poke_type]
        total_damage = math.ceil(damage * multiplier)
        opponent._take_damage(total_damage)
        effectiveness = "SUPER EFFECTIVE" if multiplier > 1 else "not very effective"
        return f"{self._name} used Razor Leaf on {opponent._name} for {total_damage} damage! It was {effectiveness}!"

    def _solar_beam(self, opponent):
        """
        This function will perform the Solar Beam move on the opponent.
        Parameters:
        - opponent: Pokemon object
        """
        damage = random.randint(2, 6)
        multiplier = self._battle_table[self._poke_type][opponent._poke_type]
        total_damage = math.ceil(damage * multiplier)
        opponent._take_damage(total_damage)
        effectiveness = "SUPER EFFECTIVE" if multiplier > 1 else "not very effective"
        return f"{self._name} used Solar Beam on {opponent._name} for {total_damage} damage! It was {effectiveness}!"
