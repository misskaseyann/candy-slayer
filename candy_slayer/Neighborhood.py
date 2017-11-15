from Home import Home

class Neighborhood():
    """A neighborhood filled with homes on a grid."""

    def __init__(self, width, height, game):
        """Initialize house grid."""
        self.housing_grid = [[Home(game) for y in range(width)] for x in range(height)]

    def get_population(self):
        """Find the population of the neighborhood."""
        x = 0
        for row in self.housing_grid:
            for item in row:
                x += item.get_population()
        return x

    def display(self):
        """Test that grid is initializing properly."""
        print("Testing Neighborhood class.")
        for row in self.housing_grid:
            for item in row:
                item.display()
            print("")
        print("Neighborhood size: ", self.get_population())