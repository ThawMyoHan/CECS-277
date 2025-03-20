from pokemon import Pokemon
import random
import math

class Fire(Pokemon):
    """
    This class will represent a Fire type Pokemon.
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
        This is the constructor for the Fire class.
        Parameters:
        - name: str
        """
        names = ["Ponyta", "Growlithe", "Vulpix"]
        if name is None:
            name = random.choice(names)
        super().__init__(name, 0)   # Fire type is 0

    def get_special_menu(self):
        """
        This function will return the special moves that the Fire Pokemon can use.
        """
        return """    1. Ember
    2. Fire Blast
        """
    
    def _special_move(self, opponent, move):
        """
        This function will perform a special move on the opponent.
        Parameters:
        - opponent: Pokemon object
        - move: int
        """
        if move == 1:
            return self._ember(opponent)
        elif move == 2:
            return self._fire_blast(opponent)
        else:
            return "Invalid move!"
        
    def _ember(self, opponent):
        """
        This function will perform the Ember move on the opponent.
        Parameters:
        - opponent: Pokemon object
        """
        damage = random.randint(2, 6)
        multiplier = self._battle_table[self._poke_type][opponent._poke_type]
        total_damage = math.ceil(damage * multiplier)
        opponent._take_damage(total_damage)
        effectiveness = "SUPER EFFECTIVE" if multiplier > 1 else "not very effective"
        return f"{self._name} used Ember on {opponent._name} for {total_damage} damage! It was {effectiveness}!"
    
    def _fire_blast(self, opponent):
        """
        This function will perform the Fire Blast move on the opponent.
        Parameters:
        - opponent: Pokemon object
        """
        damage = random.randint(1, 7)
        multiplier = self._battle_table[self._poke_type][opponent._poke_type]
        total_damage = math.ceil(damage * multiplier)
        opponent._take_damage(total_damage)
        effectiveness = "SUPER EFFECTIVE" if multiplier > 1 else "not very effective"
        return f"{self._name} used Fire Blast on {opponent._name} for {total_damage} damage! It was {effectiveness}!"