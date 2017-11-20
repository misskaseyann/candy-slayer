from random import *

from candy_slayer.monster.Ghoul import Ghoul
from candy_slayer.monster.Person import Person
from candy_slayer.monster.Vampire import Vampire
from candy_slayer.monster.Werewolf import Werewolf
from candy_slayer.monster.Zombie import Zombie
from candy_slayer.observed.Observer import Observer
from candy_slayer.observed.Observable import Observable


class Home(Observer):
    """A home filled with monsters."""
    def __init__(self, manager):
        """
        Initialize monsters inside the house.

        :param manager: game manager class
        """
        self.observable = Observable()
        self.observable.register(manager)
        self.monsters = [self.numb_to_monster(randint(1, 5)) for i in range(randint(1, 10))]

    @property
    def get_population(self):
        """Give the population of the house."""
        self.population = 0
        for monster in self.monsters:
            if monster.name != "Person":
                self.population += 1
        return self.population

    def update(self):
        """Called when a monster dies so that it can turn into a person."""
        for i, item in enumerate(self.monsters):
            if item.hp < 1:
                self.monsters.pop(i)
                self.monsters.insert(i, Person(self))
                self.observable.update_observers()

    def numb_to_monster(self, x):
        """
        Link a value to a monster object.

        :param x: random integer
        """
        monster_val = {
            1: Person(self),
            2: Zombie(self),
            3: Vampire(self),
            4: Ghoul(self),
            5: Werewolf(self),
        }
        return monster_val.get(x, Person(self))
