from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        """
        Returns area of designated shape
        """

class Square(Shape):
    def __init__(self, side):

        if not isinstance(side, (int, float)):
            raise TypeError("Side length must be integer or float.")
        if side < 0:
            raise ValueError("Side length must be greater than 0.")
        
        self.side = side

    def area(self):
        return self.side ** 2


class Circle(Shape):
    def __init__(self, radius):
        
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be integer or float.")
        if radius < 0:
            raise ValueError("Radius must be greater than 0.")
        
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2