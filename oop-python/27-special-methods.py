# hide method, _dont_use
# start with __ but not end with double underscore, it will be _Protected, can check with dir()
# @property- we can decorate it with property if we don't want people know it is a method, but just return this as being another value on ther class
# The @property is a built-in decorator for the property() function in Python. 
# It is used to give "special" functionality to certain methods to make them act as getters, setters, or deleters when we define properties in a class.

Specifically, you can define three methods for a property:

A getter - to access the value of the attribute.
A setter - to set the value of the attribute - set the attribute that the property represents
A deleter - to delete the instance attribute.

# protected.py

class Protected:
  __name = 'security'
  
  def __method(self):
    return self.__name
  
  #REPL
prot = Protected()
prot._Protected__method() # 'security'
prot._Protected__name #'Security'


# circle.py
# @property - how it set and how it retrieved, use @property

class Circle:
  def __init__(self, diameter):
      self.diameter = diameter

   @property
   def radius(self):
      return self.diameter / 2 
    
   @radius.setter
   def radius(self, radius):    #we have to set both value the same as the one above
      self.diameter = radius * 2
    
              
    small = Circle(10)
    print(small.diameter) #10
    print(small.radius) #5.0



# exercise
      
@property
def volume(self):
    return self._volume

@volume.setter
def volume(self, num):
    self._volume = num;

   

  
  class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        
    @property       #Add a new property to the Rectangle class named area. calculate and return the area of the Rectangle instance (width * length).
    def area(self):
        return self.width * self.length
    
    @property       #add a perimeter property that returns the perimeter of the rectangle (length * 2 + width * 2).
    def perimeter(self):
        return self.length * 2 +  self.width * 2
