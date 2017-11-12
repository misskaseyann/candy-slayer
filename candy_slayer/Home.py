from random import *

class Home():
    """A home filled with monsters"""

    def __init__(self):
        """Initialize monsters inside the house."""
        self.monsters = [0 for i in range(randint(0, 10))]

    def display(self):
        """Test that everything works."""
        print(len(self.monsters), end = " ")