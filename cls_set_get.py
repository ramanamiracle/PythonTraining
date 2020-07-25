#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""circle.py: The circle module, which defines the Circle class"""
from math import pi

class Circle:
    """A Circle instance models a circle with a radius"""

    def __init__(self, radius = 1.0):
        """Initializer with default radius of 1.0"""
        self.radius = radius   # Call decorated setter

    @property
    def radius(self):
        """Radius of this circle"""  # doc-string here
        # Define getter here
        return self._radius  # Read the hidden instance variable _radius
    # Equivalent to:
    # def get_radius(self):
    #    return self._radius
    # radius = property(get_radius)   # Define a property with getter

    @radius.setter
    def radius(self, radius):
        """Setter for instance variable radius with input validation"""
        if radius < 0:
           raise ValueError('Radius shall be non-negative')
        self._radius = radius  # Set a hidden instance variable _radius

    @radius.deleter
    def radius(self):
        """Deleter for instance variable radius"""
        del self._radius  # Delete the hidden instance variable _radius

    def get_area(self):
        """Return the area of this Circle instance"""
        return self.radius * self.radius * pi  # Call decorated getter

    def __repr__(self):
        """Self description for this Circle instance, used by print(), str() and repr()"""
        return 'Circle(radius={})'.format(self.radius)  # Call decorated getter


if __name__ == '__main__':
    c1 = Circle(1.2)
    print(c1)               # Output: Circle(radius=1.200000)
    print(vars(c1))         # Output: {'_radius': 1.2}
    print(dir(c1))          # Output: ['_radius', 'radius', ...]]
    c1.radius = 3.4         # Setter
    print(c1.radius)        # Getter. Output: 3.4
    print(c1._radius)       # hidden instance variable. Output: 3.4
    #print(c1.get_radius()) # AttributeError: 'Circle' object has no attribute 'get_radius'

    c2 = Circle()         # Default radius
    print(c2)             # Output: Circle(radius=1.000000)

    c3 = Circle(-5.6)     # ValueError: Radius shall be non-negative