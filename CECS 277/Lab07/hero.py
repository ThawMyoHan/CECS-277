import random
from entity import Entity

class Hero(Entity):
    """
    Represents a Hero, inheriting from Entity.
    Attributes:
        name (str): The name of the Hero.
        hp (int): The current health points of the Hero.
    Methods:
        sword_attack(dragon): Attacks the dragon with a sword.
        arrow_attack(dragon): Attacks the dragon with an arrow.
    """
    def sword_attack(self, dragon):
        """
        Attacks the dragon with a sword for 2D6 damage.
        Parameters:
            dragon (Dragon): The dragon being attacked.
        Returns:
            str: The message describing the attack.
        """
        damage = random.randint(1, 6) + random.randint(1, 6) # 2D6
        dragon.take_damage(damage) # call take_damage method from Entity class
        return f"{self.name} slashes {dragon.name} with a sword for {damage} damage!" # return message

    def arrow_attack(self, dragon):
        """
        Attacks the dragon with an arrow for 1D12 damage.
        Parameters:
            dragon (Dragon): The dragon being attacked.
        Returns:
            str: The message describing the attack.
        """
        damage = random.randint(1, 12) # 1D12
        dragon.take_damage(damage)  # call take_damage method from Entity class
        return f"{self.name} hits {dragon.name} with an arrow for {damage} damage!" # return message