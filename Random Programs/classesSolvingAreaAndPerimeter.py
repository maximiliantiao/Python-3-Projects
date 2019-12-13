from math import *

class TriangleArea():        

    def __init__(self, base_length, height):
        self.base_length = base_length
        self.height = height

    def findTriangleArea(self):
        return "\nThe area of your triangle is " + str(0.5 * self.base_length * self.height) + ".\n"

class RectangleArea():

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def findRectangleArea(self):
        return "\nThe area of your rectangle is " + str(self.length * self.width) + ".\n"

