`map()` lets us apply transformations to each item in an iterable.
map() takes a function and an iterable. 
The function should take a single argument. 
This function will be applied, in order, to each item in the iterable and the result of that function will be returned to map(). 
In the end, map() will return a new iterable with the mutated values.

[func(item) for item in iterable] achieves the same result, plus turns the results into a list. 

#map()
Return an iterator that applies function to every item of iterable, yielding the results. 
map(fun, iter)

a = [1, 2, 3]
def double(n):
  return n * 2
print(list(map(double, a))) # 2, 4, 6


#stock.py
from copy import copy
from copy import copy
import json
from operator import attrgetter, itemgetter

class Book:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return str(self)
    
    
def get_books(filename, raw=False):
    try:
        data = json.load(open(filename))
    except FileNotFoundError:
        return []
    else:
        if raw:
            return data['books']
        return [Book(**book) for book in data['books']]
    
BOOKS = get_books('books.json')
RAW_BOOKS = get_books('books.json', raw=True)

def sales_price(book):
    '''apply 20% discount to the book's price'''
    book = copy(book)   #we modify a copy instead of changing json file
    book.price = round(book.price-book*.2, 2)
    return book
    
sales_books = list((map(sales_price, BOOKS))
sales_books2 = [sales_price(book) for book in BOOKS]
print(BOOK[0].price)
print(sales_books2[0].price)    #same result



#exercise
#map
backwards = [
    'tac',
    'esuoheerT',
    'htenneK',
    [5, 4, 3, 2, 1],
]

#Create a function named reverse that takes a single iterable item and returns a reversed version of that item.
def reverse(word):
    return word[::-1]

#Now use map() to create a variable named forwards.
#forwards should use reverse() to reverse the order of every item in backwards.
forwards = map(reverse, backwards)



#map comprehension
dimensions = [
    (5, 5),
    (10, 10),
    (2.2, 2.3),
    (100, 100),
    (8, 70),
]

#Create a function named area() that takes a single argument which will be a two-member tuple.
#area() should return the result of multiplying the first item in the tuple by the second item in the tuple.
def area(nnn):
    return nnn[0]*nnn[1]
#make a variable named areas that calculates the area of each item in dimensions using your area function.
areas = [area(nnn) for nnn in dimensions]
