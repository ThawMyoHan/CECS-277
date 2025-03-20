from pokemon import Pokemon
import random
import math

class Water(Pokemon):
    """
    This class will represent a Water type Pokemon.
    Attributes:
        _battle_table (list): a 2D list of the effectiveness of each type against each other
        _name (str): the name of the Pokemon
        _type (int): the type of the Pokemon (0 = Fire, 1 = Water, 2 = Grass
    Methods:
        __init__(self, name, type): initializes the Pokemon with a name, type, and health points
        get_name(self): returns the name of the Pokemon
        get_type(self): returns the type of the Pokemon
        get_hp(self): returns the health points of the Pokemon
        _normal_move(self, opponent, move): performs a normal move on the opponent
        _special_move(self, opponent, move): performs a special move on the opponent
        attack(self, opponent, type, move): attacks the opponent with the move of the specified type
        __str__(self): returns the string representation of the Pokemon object
    """
    def __init__(self, name = None):
        """
        This is the constructor for the Water class.
        Parameters:
        - name: str
        """
        names = ["Staryu", "Magikarp", "Horsea"]
        if name is None:
            name = random.choice(names)
        super().__init__(name, 1)   # Water type is 1

    def get_special_menu(self):
        """
        This function will return the special moves that the Water Pokemon can use.
        """
        return """    1. Water Gun
    2. Bubble Beam
        """
    
    def _special_move(self, opponent, move):
        """
        This function will perform a special move on the opponent.
        Parameters:
        - opponent: Pokemon object
        - move: int
        """
        if move == 1:
            return self._water_gun(opponent)
        elif move == 2:
            return self._bubble_beam(opponent)
        else:
            return "Invalid move!"
        
    def _water_gun(self, opponent):
        """
        This function will perform the Water Gun move on the opponent.
        Parameters:
        - opponent: Pokemon object
        """
        damage = random.randint(1, 7)
        multiplier = self._battle_table[self._poke_type][opponent._poke_type]
        total_damage = math.ceil(damage * multiplier)
        opponent._take_damage(total_damage)
        effectiveness = "SUPER EFFECTIVE" if multiplier > 1 else "not very effective"
        return f"{self._name} used Water Gun on {opponent._name} for {total_damage} damage! It was {effectiveness}!"
    
    def _bubble_beam(self, opponent):
        """
        This function will perform the Bubble Beam move on the opponent.    
        Parameters:
        - opponent: Pokemon object
        """
        damage = random.randint(3, 5)
        multiplier = self._battle_table[self._poke_type][opponent._poke_type]
        total_damage = math.ceil(damage * multiplier)
        opponent._take_damage(total_damage)
        effectiveness = "SUPER EFFECTIVE" if multiplier > 1 else "not very effective"
        return f"{self._name} used Bubble Beam on {opponent._name} for {total_damage} damage! It was {effectiveness}!"