class Neighborhood():
    """A neighborhood filled with homes on a grid."""

    def __init__(self, width, height):
        """Initialize house grid."""
        self.housing_grid = [[0] * height for i in range(width)]

    def display(self):
        """Test that grid is initializing properly."""
        for row in self.housing_grid:
            print(' '.join([str(elem) for elem in row]))
