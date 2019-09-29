# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(side_a, side_b, side_c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(side_a, int) and isinstance(side_b, int) and isinstance(side_c, int)):
        return 'InvalidInput'
    # require that the input values be >= 0 and <= 200
    elif (side_a > 200 or side_b > 200 or side_c > 200):
        return 'InvalidInput'

    elif (side_a <= 0 or side_b <= 0 or side_c <= 0):
        return 'NotATriangle'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    elif two_sides_bigger_than_one(side_a, side_b, side_c):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    elif (side_a == side_b and side_b == side_a and side_a == side_c):
        return 'Equilateral'
    elif check_for_right(side_a, side_b, side_c):
        return 'Right'
    elif side_a not in (side_b, side_c) and side_b != side_c:
        return 'Scalene'
    else:
        return 'Isoceles'


def check_for_right(side_a, side_b, side_c):
    """ Takes in three triangle side lengths and checks if they
    form the sides of a right triangle using Pitagoras"""
    a_squared, b_squared, c_squared = side_a ** 2, side_b ** 2, side_c ** 2
    if a_squared + b_squared == c_squared:
        return True
    elif a_squared + c_squared == b_squared:
        return True
    elif b_squared + c_squared == a_squared:
        return True
    else:
        return False

def two_sides_bigger_than_one(side_a, side_b, side_c):
    """ Takes in three triangle side lenths and checks that they can form
    a real triangle, using the rule that the sum of two triangle side
    lengths cannot exceed the length of the third one."""
    if side_a >= (side_b + side_c):
        return True
    elif side_b >= (side_a + side_c):
        return True
    elif side_c >= (side_a + side_b):
        return True
    else:
        return False