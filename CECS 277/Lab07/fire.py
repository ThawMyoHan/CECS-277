import random
from dragon import Dragon

class FireDragon(Dragon):
    """
    Represents a FireDragon, inheriting from Dragon.
    Attributes: 
        name (str): The name of the FireDragon.
        hp (int): The current health points of the FireDragon.
        fireball_count (int): The number of fireballs the FireDragon has.
    Methods:
        basic_attack(hero): Attacks the hero with a basic attack.
        special_attack(hero): Attacks the hero with a special attack.
    """
    def __init__(self, name, hp):
        """
        Initializes the FireDragon with a name and health points.
        Parameters:
            name (str): The name of the FireDragon.
            hp (int): The health points of the FireDragon.
        """
        super().__init__(name, hp) # call __init__ method from Dragon class
        self._fireball_count = 3 # protected attribute

    def special_attack(self, hero):
        """
        Attacks the hero with a fireball for 6-9 damage.
        Parameters:
            hero (Hero): The hero being attacked.
        Returns:
            str: The message describing the attack.
        """
        if self._fireball_count > 0: # if fireball_count is greater than 0
            damage = random.randint(6, 9) # 6-9 damage
            hero.take_damage(damage) # call take_damage method from Entity class
            self._fireball_count -= 1 # decrement fireball_count by 1
            return f"{self.name} engulfs {hero.name} in flames for {damage} damage!" 
        else:
            return f"{self.name} tries to spit fire at {hero.name} but is all out of fire shots!" 
        
    def __str__(self):
        """
        Returns a string representation of the FireDragon.
        Parameters:
            str: The string representation of the FireDragon.
        Returns:
            str: The string representation of the FireDragon.
        """
        return f'{super().__str__()} \nFireballs remaining: {self._fireball_count}' 