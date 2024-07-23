# Title: Point Class

class Point:
    """
    Represents a point in a 2D coordinate system.
    """

    def __init__(self, x, y):
        """
        Initializes a Point object with the given x and y coordinates.
        :param x: The x-coordinate of the point.
        :param y: The y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Returns a string representation of the Point object.
        :return: A string representation of the Point object in the format (x, y).
        """
        return "(" + str(self.x) + "," + str(self.y) + ")"
