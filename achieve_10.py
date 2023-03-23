class Shape:
    category = "Quadrilateral"
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def perm(self):
        a = (self.width*2) + (self.height*2)
        print("Total length:\n",a," cm")
        return a
    def calculateArea(self):
        b = (self.width*self.height)
        print("Total area:\n",b," cm²")
        return b
    def displayInfo(self):
        print("Dimensions: width = {} cm height = {} cm".format(self.width, self.height))   
        Dimension.calculateArea()
        Dimension.perm()
  
print("Welcome to the geometry calculator!\n")        
Dimension = Shape(float(input("Enter the width in centimeters:")), float(input("Enter the length in centimeters:")))

Dimension.displayInfo()
