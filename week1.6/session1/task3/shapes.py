# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")

        self.colour = colour


# Implement your Circle class here
class   Circle(Shape): 
    def __init__(self, radius,position,colour="red"):
        super().__init__(position,colour)
        self.set_radius(radius)
    def set_radius(self, radius):
        """ set the radius of the circles"""
        if not isinstance(radius,(float,int) ):
            raise TypeError("radius must be float or int")
        if radius <=0:
            raise ValueError("radius must greater than zero")
        self.radius=radius
    def  __str__(self):
        return f"{self.colour} radius,radius {self.radius},at {self.position}"
    def  area(self):
        return math.pi*self.radius**2
    def  perimeter(self):
        return (math.pi*2)*self.radius
# Make sure that it inherits properly from Shape!
