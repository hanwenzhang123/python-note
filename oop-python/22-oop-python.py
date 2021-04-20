# The class keyword lets us define a class. We use it just like we do the def keyword for making functions. Class definitions are blocks like function definitions.
class NewClass:


# Inside of the class, variables are called attributes.
class NewClass:
    name_attribute = "Kenneth"
    
    
# And functions that are defined inside of a class are called methods.
class NewClass:
    name_attribute = "Kenneth"

    def name_method(self):
        return self.name_attribute
        
        
# Whenever we call a class, it creates an instance. Each instance has full access to the all of the attributes and methods of the class.
new_instance = NewClass()
new_instance.name_method()


# Classes are the blueprints for objects.
# A variable that belongs to a class is known as an attribute.	
# An instance is the result of using, or calling, a class. An instance is a new copy of a class.
# methods are functions that belongs to class
# method takes at least one parameter which represents that called self
# The self argument that all standard methods receive is a reference to the instance
# dunder - when you create a new instance of a class, python usually runs on its own
# del - delete an instance

import random   #Random is package. You import it once, then you can use it in your code anytime you want.

class Character:
    def __init__(self, name, **kwargs):
        self.name = name
        
        for key, value in kwargs.items():
        setattr(self, key, value) 

        
class Thief(Character): #inheritate the character class to thief
  sneaky = True         # thief gets all the things that character does, and can add on its own thing
  
#   def __init__(self, name, sneaky = True, **kwargs): #key value pair
#     self.name = name
#     self.sneaky = sneaky
    
#     for key, value in kwargs.items():
#       setattr(self, key, value)   # setattr to take any other keyword arguments that come in
  
  def pickpocket(self):  
      return self.sneaky and bool(random.randint(0, 1)) #random.randint() used to give a variable a random value. 
  
  def hide(self, light_level):
    return self.sneaky and light_level < 10
  
  

  
# exercise
class Student:
    name = 'Hanwen'
    
me = Student()
print(me.name)

class Student:
    name = "Hanwen"
    
    def __init__(self, name, **kwargs):
    self.name = name

    for key, value in kwargs.items():
    setattr(self, key, value)
            
    def praise(self):
        return "{} You're doing a great job".format(self.name)
      
      class Student:
    name = "Hanwen"
    
    def praise(self):
        return "You inspire me, {}".format(self.name)
    
    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)
    
    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        return self.reassurance()
     
      
      
      
class RaceCar:
    def __init__ (self, color, fuel_remaining, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        self.laps = 0
        
        for key, value in kwargs.items():
            setattr(self, key, value)
        
    def run_lap(self, length):
        self.fuel_remaining -= length * 0.125
        self.laps = self.laps + 1
 
