class Entity:
    """
    Represents an Entity with a name and health points.
    Attributes:
        name (str): The name of the Entity.
        max_hp (int): The maximum health points of the Entity.
        hp (int): The current health points of the Entity.
    Methods:
        take_damage(dmg): Reduces the health points of the Entity by the specified damage.
    """
    def __init__(self, name, max_hp):
        """
        Initializes the Entity with a name and maximum health points.
        Parameters:
            name (str): The name of the Entity.
            max_hp (int): The maximum health points of the
                Entity.
        """
        self._name = name   # protected attribute
        self._max_hp = max_hp  # protected attribute
        self._hp = max_hp # protected attribute
    @property
    def name(self):
        """
        Returns the name of the Entity.
        Parameters:
            str: The name of the Entity.
        Returns:
            str: The name of the Entity.
        """
        return self._name
    
    @property
    def hp(self):
        """
        Returns the current health points of the Entity.
        Parameters:
            int: The current health points of the Entity.
        Returns:
            int: The current health points of the Entity.
        """
        return self._hp # protected attribute
    
    def take_damage(self, dmg):
        """
        Reduces the health points of the Entity by the specified damage.
        Parameters:
            dmg (int): The amount of damage to take.
        """
        self._hp -= dmg
        if self._hp < 0: # if hp is negative, set hp to 0
            self._hp = 0

    def __str__(self):
        """
        Returns a string representation of the Entity.
        Parameters:
            str: The string representation of the Entity.
        Returns:
            str: The string representation of the Entity.
        """
        return f'{self._name}: {self._hp}/{self._max_hp}' # protected attributes

