# Create a new class named TicTacToe that inherits from Board and give it an __init__ method. 
# Inside the __init__ of the TicTacToe class use super() to initialize a board with width and height each set to 3. 
# When an instance of TicTacToe is created, it will result in a board that has the dimensions 3 x 3.

#Let's make all Board instances iterable so we can loop through their cells attribute. 
#Inside the Board class, define an iter method that yields the cells. 

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []    # <---- This is what we are trying to iterate over in Challenge 2 
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append((x, y))

    def __iter__(self):    #<----- Second challenge asked us to define __iter__
        for cell in self.cells:
            yield cell


class TicTacToe(Board):      # <---- First challenge asked to make this class
    def __init__(self):
        super().__init__(width=3, height=3)
        
        
        
        
# We'd like to compare songs by their length, which is measured in whole seconds. 
#Create an __int__ method that should return the length of the song. 
#Then, create the following comparison methods: __eq__, __lt__, __gt__, __le__ and __ge__.   

class Song:
    def __init__(self, artist, title, length):
        self.artist = artist
        self.title = title
        self.length = length
        
    def __int__(self):
        return self.length
    
    def __eq__(self, other):
        return int(self) == other
    
    def __lt__(self, other):
        return int(self) < other
    
    def __gt__(self, other):
        return int(self) > other
    
    def __le__(self, other):
        return int(self) < other or int(self) == other
    
    def __ge__(self, other):
        return int(self) > other or int(self) == other
      
      
      
        
# Create a new class in dice.py named D20 that extends Die.
# It should automatically have 20 sides and will not need any arguments to create.


import random


class Die:
    def __init__(self, sides=2):
        if sides < 2:
            raise ValueError("Can't have fewer than two sides")
        self.sides = sides
        self.value = random.randint(1, sides)
        
    def __int__(self):
        return self.value
      
    def __add__(self, other):
        return int(self) + other
    
    def __radd__(self, other):
        return self + other
    
class D20(Die):
    def __init__(self, sides = 20):
        super().__init__(sides)

 
# In the hands.py file import the D20 class from dice.py. 
# Create a classmethod named roll. Since it is a classmethod, it will take cls as an argument. 
# It will also take the number of dice as an argument. 
# Inside the roll classmethod create a new instance of the Hand class and assign it to a variable.
# Append a D20 to your Hand equal to the number of dice given as an argument to the roll classmethod. 
# Then return the Hand of D20s. For example, if Hand.roll(2) is called, it would return a list with two D20s inside.


from dice import D20

class Hand(list):

    def __init__(self, size=0, die_class=D20):
        super().__init__()
        for _ in range(size):
            self.append(die_class())

    @classmethod
    def roll(cls, size=2):
        return cls(size=size)

    @property
    def total(self):
        return sum(self)
