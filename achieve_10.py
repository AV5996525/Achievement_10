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
        print("Total area:\n",b," cm^2")
        return b
    def displayInfo(self):
        print("Dimensions: width = {} height = {}".format(self.width, self.height))   
        Dimension.calculateArea()
        Dimension.perm()
print("Enter width followed by height")        
Dimension = Shape(float(input()), float(input()))

Dimension.displayInfo()
