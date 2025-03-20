import random
from entity import Entity

class Dragon(Entity):
    """
    Represents a Dragon, inheriting from Entity.
    Attributes:
        name (str): The name of the Dragon.
        hp (int): The current health points of the Dragon.
    Methods:
        basic_attack(hero): Attacks the hero with a basic attack.
        special_attack(hero): Attacks the hero with a special attack.
    """
    def basic_attack(self, hero):
        """
        Attacks the hero with a basic attack.
        Parameters:
            hero (Hero): The hero being attacked.
        Returns:
            str: The message describing the attack.
        """
        damage = random.randint(2, 5) # 2-5 damage
        hero.take_damage(damage) # call take_damage method from Entity class
        return f"{self.name} smashes {hero.name} with its tail for {damage} damage!" # return message

    def special_attack(self, hero):
        """
        Attacks the hero with a special attack.
        Parameters:
            hero (Hero): The hero being attacked.
        Returns:
            str: The message describing the attack.
        """
        damage = random.randint(3, 7) # 3-7 damage
        hero.take_damage(damage) # call take_damage method from Entity class
        return f"{self.name} slashes {hero.name} with its claw for {damage} damage!" # return message
