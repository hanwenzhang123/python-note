# super allows us use the code from our super class on demand even after we have overwritten stuff in subclasses.
# when we use super(), we need to include the method name and its required arguments
# super() function in Python makes class inheritance more manageable and extensible.
# Method Resolution Order (MRO) controls the order that classes are searched through to find a particular method.
# super() lets you run a parent class's version of a method

# testing family tree
isinstance('a', str) #True
isinstance(5.2, (int, float)) 
isinstance(5.2, (str,bool, dict)) #False
isinstance(True, int)  #True
issubclass(bool, int) #True
issubclass(str, int) #False

from thieves import Thief
from characters import Character
issubclass(Thief, Character) #True



from 
issubclass(thief, Character)

import random  

class Character:
    def __init__(self, name="", **kwargs):
        self.name = name
        
    for key, value in kwargs.items():
    setattr(self, key, value) 

        
class Thief(Character): #inheritate the character class to thief
  sneaky = True         # thief gets all the things that character does, and can add on its own thing
  
  def __init__(self, name, sneaky = True, **kwargs):
      super(). __init__(name, **kwargs) # override init, call the same method and argument inside the () of parent class
      self.sneaky = sneaky    #if we put super() after self.sneaky, it may override, so we call super() first
  
  def pickpocket(self):  
      return self.sneaky and bool(random.randint(0, 1))
  
  def hide(self, light_level):
      return self.sneaky and light_level < 10

    
# multiple Superclasses (4 files here)
    
# characters.py
class Character:
    def __init__(self, name, **kwargs):
        if not name:
        raise ValueError("name required")
        self.name = name
        
        for key, value in kwargs.items():
            setattr(self, key, value)


# attributes.py
import random

class Sneaky:
    sneaky = True
    
    def __init__(self, sneaky=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sneaky = sneaky
        
    def hide(self, light_level):
        return self.sneaky and light_level < 10
        
class Agile:
    agile = True
    
    def __init__(self, agile=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.agile = agile
        
    def evade(self):
        return self.agile and random.randint(0, 1)

    
# thieves.py
import random
from attributes import Agile, Sneaky
from characters import Character

class Thief(Character, Agile, Sneaky):
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))
    

# play.py
from thieves import Thief

kenneth = Thief(name="Kenneth", sneaky = False)
print(kenneth.seaky) #False
print(kenneth.agile) #True
print(kenneth.hide(8)) #False
    
    
    
    
    #exercise
class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)
        
class SortedInventory(Inventory):
    def add_item(self, item):
        super().add_item(item)      #override the parent calss Inventory
        self.slots.sort()
