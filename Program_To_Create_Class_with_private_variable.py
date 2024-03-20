# create a class private variable named pi=3.141
class Circle():
# constructor
    def __init__(self,radius,pi=3.141):
       self.radius = radius
       self.pi = pi
       
# method    
    def myFunc(self):
        print ("The Area of circle :", self.pi* self.radius * self.radius)
# creating object of the class. This invokes constructor

p1 = Circle(10)
p1.myFunc()


