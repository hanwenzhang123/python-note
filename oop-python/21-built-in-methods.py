# dunder methdos are built-in methods that are automatically created


# __str__   dunder string: this method controls how your objects are represented as a string
# __iter__  dunder iterate: how to handle iterating through an instance like you would with while or for loops
# __eq__  dunder equal: equal comparison, compare two objects you created


class Car: 
  wheels = 4    
  doors = 2
  engine = True

def __init__(self, model, year, make='ford'): 
  self.make = make      
  self.model = model
  self.year = year
  self.gas = 100
  self.is_moving = False 
    
def __str__ (self):
  return f'{self.make} {self.model} {self.year}'
  
def __eq__(self, other):    # boolean value to see either they equal
  return self.make == other.make and self.model == other.model

class Dealership:
    def __init__(self):
      self.cars = []
    def __iter__(self): 
      yield from self.cars  #yield from grabs each item in the iterable here the car list and return it
    def add_car(self, car):
      self.cars.append(car)
 
#string example
print(str(car_one))   # same result as call python car.py in the console directly
#iteration example
car_one = Car("Model T", 1908)
car_two = Car("fiesta", 2000)
my_dealership = Dealership()
my_dealership.add_car(car_one)
my_dealership.add_car(car_two)
for car in my_dealership:
  print(Car)
#equal comparison
if car_one == car_two:
  print('equal')
else:
  print('not equal')

  
# for attribute in car_one:
#   print(attribute)  # car object is not iterable this code does not work here


# exercise
class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def __str__(self):
        return "{}, {}".format(self.author, self.title)

    def __eq__(self, other):
        return self.author + self.title == other
      
      from book import Book


class BookCase:
    def __init__(self):
       self.books = []

    def add_books(self, book):
        self.books.append(book)

    def __iter__(self):
        yield from self.books
