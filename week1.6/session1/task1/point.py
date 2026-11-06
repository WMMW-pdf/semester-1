# Week 1.6, Session 1: Task 1

import math


class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        """
        Creates a Point, given x & y coordinates.
        """
        if not isinstance(x, int):
            raise TypeError("x coordinate must be an integer")

        if not isinstance(y, int):
            raise TypeError("y coordinate must be an integer")

        self.x = x
        self.y = y

    def distance(self):
        """
        Returns distance of this Point from the origin.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, p):
        """
        Returns distance of this Point from another Point.
        """
        return math.hypot(self.x - p.x, self.y - p.y)
p1=Point(3,4)
print("Distance from origin:",p1.distance())
p2=Point(0,0)
print("Distance between points:",p1.distance_to(p2))
