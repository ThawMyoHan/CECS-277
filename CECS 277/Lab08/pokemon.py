from abc import ABC, abstractmethod
import random

class Pokemon(ABC):
    """
    Represents a Pokemon with a name, type, and health points
    Attributes:
        _battle_table (list): a 2D list of the effectiveness of each type against each other
        _name (str): the name of the Pokemon
        _type (int): the type of the Pokemon (0 = Fire, 1 = Water, 2 = Grass
    Methods:
        __init__(self, name, type): initializes the Pokemon with a name, type, and health points
        get_name(self): returns the name of the Pokemon
        get_type(self): returns the type of the Pokemon
        get_hp(self): returns the health points of the Pokemon
    """
    def __init__(self, name, p_type):
        """
        This is the constructor for the Pokemon class.
        Parameters:
        - name: str
        - p_type: int
        """
        self._name = name
        self._poke_type = p_type
        self._battle_table = [
            [1, .5, 2],     # Fire vs. (Fire, Water, Grass)
            [2, 1, .5],     # Water vs. (Fire, Water, Grass)
            [.5, 2, 1]    # Grass vs. (Fire, Water, Grass)
        ]
        self._hp = 25
    
    @property
    def hp(self):
        """
        This is the getter for the hp property.
        """
        return self._hp
    
    def get_normal_menu(self):
        """
        This function will return the normal moves that the Pokemon can use.
        """
        return """    1. Slam
    2. Tackle
        """
    
    def _normal_move(self, opponent, move):
        """
        This function will perform a normal move on the opponent.
        Parameters:
        - opponent: Pokemon object
        - move: int
        """
        if move == 1:
            return self._slam(opponent)
        elif move == 2:
            return self._tackle(opponent)
        else:
            return "Invalid move!"
        
    def _slam(self, opponent):
        """
        This function will perform the Slam move on the opponent.
        Parameters:
        - opponent: Pokemon object
        """
        damage = random.randint(2, 6)
        opponent._take_damage(damage)
        return f"{self._name} SLAMS {opponent._name} for {damage} damage!"
    
    def _tackle(self, opponent):
        """
        This function will perform the Tackle move on the opponent.
        Parameters:
        - opponent: Pokemon object
        """
        damage = random.randint(3, 5)
        opponent._take_damage(damage)
        return f"{self._name} TACKLES {opponent._name} for {damage} damage!"
    
    @abstractmethod
    def get_special_menu(self) -> str:
        """
        This function will return the special moves that the Pokemon can use.
        """
        pass

    def _special_move(self, opponent, move) -> str:
        """
        This function will perform a special move on the opponent.
        Parameters:
        - opponent: Pokemon object
        - move: int
        """
        pass
    
    def attack(self, opponent, type, move):
        """
        This function will attack the opponent with the move of the specified type.
        Parameters:
        - opponent: Pokemon object
        - type: str
        - move: int
        """
        if type == "normal":
            return self._normal_move(opponent, move)
        elif type == "special":
            return self._special_move(opponent, move)
        else:
            return "Invalid attack type!"
        
    def __str__(self):
        """
        This function will return the string representation of the Pokemon object.
        """
        return f"{self._name} HP: {self._hp}/25"
    
    def _take_damage(self, dmg):
        """
        This function will decrease the HP of the Pokemon by the specified amount.
        Parameters:
        - dmg: int
        """
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0