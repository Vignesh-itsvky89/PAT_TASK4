# create a class private variable named pi=3.141
class Circle():
# constructor
    def __init__(self,radius,pi=3.141):
       self.radius = radius
       self.pi = pi
       
# method 1
    def area(self):
        print ("The Area of circle :", self.pi* self.radius * self.radius)
# method 2
    def perimeter(self):
        print ("The perimerter of circle :", 2 * self.pi* self.radius)
# creating object of the class. This invokes constructor

p1 = Circle(10)
p1.area()
p1.perimeter()