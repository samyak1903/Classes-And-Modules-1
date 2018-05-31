#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
class Circle:
    ''' class for compi=utong the area and circumference of circle'''
    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        ''' method for computing the area of circle'''
        return 3.14*self.radius*self.radius
    def getCircumference(self):
        ''' method for computing the circumference of circle'''
        return 2*3.14*self.radius
radius=float(input("Enter the radius of circle: "))
c=Circle(radius)
print("Area of circle= ",c.getArea())
print("Circumference of circle= ",c.getCircumference())

