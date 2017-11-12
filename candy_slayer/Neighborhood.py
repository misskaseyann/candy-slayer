from Home import Home

class Neighborhood():
    """A neighborhood filled with homes on a grid."""

    def __init__(self, width, height):
        """Initialize house grid."""
        self.housing_grid = [[Home() for y in range(width)] for x in range(height)]


    def display(self):
        """Test that grid is initializing properly."""
        print("Testing Neighborhood class.")
        for row in self.housing_grid:
            for item in row:
                item.display()
            print("")