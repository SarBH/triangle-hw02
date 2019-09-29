# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangle(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testScaleneTriangle(self): 
        self.assertEqual(classify_triangle(10,20,11),'Scalene')
        self.assertEqual(classify_triangle(3, 4, 6), 'Scalene')

    def testEquilateralTriangle(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classify_triangle(34, 34, 34), 'Equilateral')

    def testNotATriangle(self): 
        self.assertEqual(classify_triangle(0,0,0), 'NotATriangle', 'side lengths of zero')
        self.assertEqual(classify_triangle(25,10,11),'NotATriangle', '25,10,11 is not a triangle because 10+11 < 25') 
        self.assertEqual(classify_triangle(34, 34, -35), 'NotATriangle', '34.5, 34.5, -35 is not a triangle because it has a negative side length')

    def testIsocelesTrianlge(self): 
        self.assertEqual(classify_triangle(10,10,11),'Isoceles')
        self.assertEqual(classify_triangle(34, 34, 35), 'Isoceles', 'is isoceles even though its side length is non-integer')

    def testInvalidInput(self): 
        self.assertEqual(classify_triangle(10.5,10,11),'InvalidInput', 'cant accept non integer side values')
        self.assertEqual(classify_triangle('thirty', 34, '35'), 'InvalidInput', 'cant accept string values')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(verbosity=2)

