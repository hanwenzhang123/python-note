__str__ - Control how your instances turn into strings, identify the object you want to turn into a string
__int__ - Control int() conversion
__init__ - Customize the initialization of your instances


# characters.py
class Character:
    def __init__(self, name, **kwargs):
        self.name = name
        
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    def __str__(self):
         return "{}: {}".format(self.__class__.__name__, self.name)
            
        

# numstring.py
  class NumString:
   # conversion
    def __init__(self, value):
      self.value = str(value)
      
    def __str__(self):
      return self.value
    
    def __int__(self):
      return int(self.value)
    
    def __float(self):
      return float(self.value)
   
    # math
    def __add__(self, other):
      if '.' in self.value:
        return float(self) + other
      return int(self) + other    # Don't forget that int! NumString(4) + 5  # 9 only apply left side
#     return self.value + str(other)   five + 4  # 54

    def __radd__(self, other):      # this apply to the right side of the value
        return self + other
    
    def __iadd__ (self, other):     #this changes the value like age+=1
        self.value = self + other
        return self.value
        
    
#in the console
from numstring import NumString
  five = NumString(5)
  str(five) # '5'
  print(five) # 5
  int(five) # 5
  float(five) # 5.0
  five + 4  # 54
  NumString(4) + 5  # 9 only apply left side
  age = NumString(25)
  age + 5   #30
  5 + age   #30
  age += 1  # age = 26  
  
#exercise
  class DreamCar:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def __str__(self):
        return "My dream car is a {} {}.".format(self.make, self.model)
    
    
    
    
    
    class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
         return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)
    
    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other
      
    def __radd__(self, other):
        return self + other
    
    def __iadd__(self, other):
        self.value = self + other
        return self.value
    
    def __mul__(self, other):
        if '.' in self.value:
            return float(self) * other
        return int(self) * other

    def __rmul__(self, other):
        return self * other 
    
    def __imul__(self, other):
        self.value = self * other
        return self.value
