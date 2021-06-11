class Employee():
  def __init__(self, name):
    self.name = name
 
argus = Employee("Argus Filch")
print(argus)
# prints "<__main__.Employee object at 0x104e88390>"    #when we print out an object we get a default representation that seems fairly useless.



#dunder method called __repr__()
This is a method we can use to tell Python what we want the string representation of the class to be. 
__repr__() can only have one parameter, self, and must return a string.


class Employee():
  def __init__(self, name):
    self.name = name
 
  def __repr__(self):
    return self.name
 
argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"


#example
class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)

# Circle with radius 6.0
# Circle with radius 18.0
# Circle with radius 5730.0
