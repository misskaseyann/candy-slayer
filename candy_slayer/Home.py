from random import *

from monster.Ghoul import Ghoul
from monster.Person import Person
from monster.Vampire import Vampire
from monster.Werewolf import Werewolf
from monster.Zombie import Zombie
from observed.Observer import Observer

class Home(Observer):
    """A home filled with monsters"""

    def __init__(self):
        """Initialize monsters inside the house."""
        self.monsters = [self.numb_to_monster(randint(1, 5)) for i in range(10)]

    def get_population(self):
        """Give the population of the house."""
        return len(self.monsters)

    def get_monsters(self):
        """Give the list of monsters in the house."""
        return self.monsters

    def update(self):
        """Called when a monster dies so that it can turn into a person."""
        for i, item in enumerate(self.monsters):
            if item.hp < 1:
                self.monsters.pop(i)
                self.monsters.insert(i, Person(self))


    def numb_to_monster(self, x):
        """Link a value to a monster object."""
        monster_val = {
            1: Person(self),
            2: Zombie(self),
            3: Vampire(self),
            4: Ghoul(self),
            5: Werewolf(self),
        }
        return monster_val.get(x, Person(self))

    def display(self):
        """Test that everything works."""
        print(len(self.monsters), end = " ")