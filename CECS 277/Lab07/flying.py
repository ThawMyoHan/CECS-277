import random
from dragon import Dragon

class FlyingDragon(Dragon):
    """
    Represents a FlyingDragon, inheriting from Dragon.
    Attributes:
        name (str): The name of the FlyingDragon.
        hp (int): The current health points of the FlyingDragon.
        swoops (int): The number of swoops the FlyingDragon has.
    Methods:
        basic_attack(hero): Attacks the hero with a basic attack.
        special_attack(hero): Attacks the hero with a special attack.
    """
    def __init__(self, name, hp):
        """
        Initializes the FlyingDragon with a name and health points.
        Parameters:
            name (str): The name of the FlyingDragon.
            hp (int): The health points of the FlyingDragon.
        """
        super().__init__(name, hp) # call __init__ method from Dragon class
        self.swoops = 3 

    def special_attack(self, hero):
        """
        Attacks the hero with a swoop for 5-8 damage.
        Parameters:
            hero (Hero): The hero being attacked.
        Returns:
            str: The message describing the attack.
        """
        if self.swoops > 0: # if swoops is greater than 0
            damage = random.randint(5, 8) # 5-8 damage
            hero.take_damage(damage) # call take_damage method from Entity class
            self.swoops -= 1 # decrement swoops by 1
            return f"{self.name} swoops down on {hero.name} for {damage} damage."
        else:
            return f"{self.name} is out of energy!"
        
    def __str__(self):
        """
        Returns a string representation of the FlyingDragon.
        Parameters:
            str: The string representation of the FlyingDragon.
        Returns:
            str: The string representation of the FlyingDragon.
        """
        return f'{super().__str__()} \nSwoop Attacks Remaining: {self.swoops}'
