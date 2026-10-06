"""
Triangle module for right-angled triangle calculations.
"""

__author__ = "Klauberta Morina"
__version__ = "1.0"


def hypotenuse(a, b):
    """
    Returns the hypotenuse of a right-angled triangle.
    """
    return (a**2 + b**2) ** 0.5


def area(a, b):
    """
    Returns the area of a right-angled triangle.
    """
    return (a * b) / 2