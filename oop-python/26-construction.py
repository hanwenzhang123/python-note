#  @classmethod - Constructors, as most classmethods would be considered
# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
# Decorators are usually called before the definition of a function you want to decorate.
#   @classmethod - The factory design pattern is mostly associated with which method type in Python?
# __new__ - override to control the construction of an immutable object
# type() - it will give me the class of an instance

# books.py

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    
  def __str__(self):
    return '{} by {}'.format(self.title, self.author)
  

class Bookcase:
  def __init__(self, books = None): #default value
    self.books = books
    
  @classmethod #marks the method as belonging to the class and makes the method assessable from the class
  def create_bookcase(cls, book_list):
    books = []
    for title, author in book_list:
      books.append(Book(title, author))
    return cls(books)
      
    
    
    
# exercise  

# Below is a class called DreamVacation that holds a location and list of activities. 
# Create a @classmethod called rome that will return a new DreamVacation instance with cls() with the following arguments: location = 'Rome' and activities list = ['visit the Colosseum', 'Eat gelato'].

class DreamVacation:
    def __init__(self, location, activities):
        self.location = location
        self.activities = activities

    @classmethod
    def rome(cls):
        return cls('Rome', ['visit the Colosseum', 'Eat gelato'])

      
