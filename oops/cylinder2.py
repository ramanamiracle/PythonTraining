#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""cylinder.py: The cylinder module, which defines the Cylinder class"""
from math import pi
from circle import Circle  # Using the Circle class in the circle module


class Cylinder(Circle):
    """The Cylinder class is a subclass of Circle"""

    def __init__(self, radius=1.0, height=1.0):
        """Initializer"""
        super().__init__(radius)  # Invoke superclass' initializer
        self.height = height

    def __str__(self):
        """Self Description for print() and str()"""
        return 'Cylinder({}, height={})'.format(super().__repr__(), self.height)
        # Use superclass' __repr__()

    def __repr__(self):
        """Formal Description for repr()"""
        return self.__str__()  # re-direct to __str__() (not recommended)

    # Override
    def get_area(self):
        """Return the surface area the cylinder"""
        return 2.0 * pi * self.radius * self.height

    def get_volume(self):
        """Return the volume of the cylinder"""
        return super().get_area() * self.height  # Use superclass' get_area()


# For testing
if __name__ == '__main__':
    cy1 = Cylinder(1.1, 2.2)
    print(cy1)  # Invoke __str__(): Cylinder(Circle(radius=1.1), height=2.2)
    print(cy1.get_area())  # Invoke overridden version
    print(cy1.get_volume())  # Invoke its method
    print(cy1.radius)
    print(cy1.height)
    print(str(cy1))  # Invoke __str__()
    print(repr(cy1))  # Invoke __repr__()

    cy2 = Cylinder()  # Default radius and height
    print(cy2)  # Invoke __str__(): Cylinder(Circle(radius=1.0), height=1.0)
    print(cy2.get_area())
    print(cy2.get_volume())

    print(dir(cy1))
    # ['get_area', 'get_volume', 'height', 'radius', ...]
    print(Cylinder.get_area)
    # <function Cylinder.get_area at 0x7f505f464488>
    print(Circle.get_area)
    # <function Circle.get_area at 0x7f490436b378>