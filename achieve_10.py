#Name:          achieve_10.py
#Author:        AJ Varatharajan
#Date Created:  March 23, 2023
#Date Last Modified: March 23, 2023
#Purpose: User is able to input width and height and calculate perimeter and area.
#This program will output calculations. The users input will create the shape object that is being used to determine the calculations.
#
class Shape: # base class
    category = "Quadrilateral" # class attribute
    def __init__(self, width, height):# Instance attribute
        self.width = width
        self.height = height
    def calculatePerimeter(self): #instance method
        a = (self.width*2) + (self.height*2)
        print("Total length:\n",a," cm")
        return a
    def calculateArea(self): #instance method
        b = (self.width*self.height)
        print("Total area:\n",b," cm²")
        return b
    def displayInfo(self): #instance method
        print("Dimensions: width = {} cm height = {} cm".format(self.width, self.height))   
        Dimension.calculateArea()
        Dimension.calculatePerimeter()
  
print("Welcome to the geometry calculator!\n")        
Dimension = Shape(float(input("Enter the width in centimeters:")), float(input("Enter the length in centimeters:"))) # Object instantiation, through user input.

Dimension.displayInfo() # Accessing class methods
