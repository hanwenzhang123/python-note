The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.
This function is defined in “functools” module.

functools.reduce() takes a function and an iterable. The function, though, takes two arguments. 
The first time it runs, the two arguments will be the first two items in the iterable. 
Every time after that, the first argument will be the result of the last time the function was run. 
The second argument will be the next value from the iterable. 
When the iterable is out of items, reduce() will return whatever the function returned last.

Think about adding up all of the numbers in a column. You add the top two, then add the third number to the sum you got from the first two. 
Then you add the fourth number to the sum of the top three, and so on.

Calling a function over again from within itself is known as recursion and it's what makes reduce() able to do its job.

Reduce is using recursive functions to calculate a final total



#stock.py
from copy import copy
from functools import reduce
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

### SORTED ###
# pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))
# print(pub_sort[0]['publish_date'], pub_sort[-1]['publish_date'])
# pages_sort = sorted(BOOKS, key=attrgetter('number_of_pages'))
# print(pages_sort[0].number_of_pages, pages_sort[-1].number_of_pages)

#important_list = [5, 3, 1, 2, 4]
#important_list.sort()  # Bad idea, sorts list in place
# sorted(important_list)  # Sorts a copy of the list

### MAP ###
def sales_price(book):
    """Apply a 20% discount to the book's price"""
    book = copy(book)
    book.price = round(book.price-book.price*.2, 2)
    return book

# sales_books = list(map(sales_price, BOOKS))
# sales_books2 = [sales_price(book) for book in BOOKS]

### FILTER ###
def is_long_book(book):
    """Does a book have 600+ pages?"""
    return book.number_of_pages >= 600

# long_books = list(filter(is_long_book, BOOKS))
# long_books2 = [book for book in BOOKS if book.number_of_pages >= 600]

### CHAINING ###
def has_roland(book):
    return any(["Roland" in subject for subject in book.subjects])

def titlecase(book):
    book = copy(book)
    book.title = book.title.title()
    return book

#print(list(map(titlecase, filter(has_roland, BOOKS))))

def is_good_deal(book):
    return book.price <= 5

# cheap_books = sorted(
#     filter(is_good_deal, map(sales_price, BOOKS)),
#     key=attrgetter('price')
# )
# print(cheap_books[0].price)

### REDUCE ###
def product(x, y):
    return x * y

# print(reduce(product, [1, 2, 3, 4, 5]))   #120

# Reduce() is like a for loop but with an outside value
#total = 1
#for x in [1, 2, 3, 4, 5]:
#    total = x * total
#print(total)    #120

def add_book_prices(book1, book2):
    return book1 + book2

total = reduce(add_book_prices, [b.price for b in BOOKS])
print(total) #$225.3

#recursion
def long_total(a=None, b=None, books=None):
    if a is None and b is None and books is None:
        return None
    if a is None and b is None and books is not None:
        a = books.pop(0)
        b = books.pop(0)
        return long_total(a, b, books)
    if a is not None and books and books is not None and b is None:
        b = books.pop(0)
        return long_total(a, b, books)
    if a is not None and b is not None and books is not None:
        return long_total(a+b, None, books)
    if a is not None and b is not None and not books:
        return long_total(a+b, None, None)
    if a is not None and b is None and not books or books is None:
        return a
print(long_total(None, None, [b.price for b in BOOKS])) #$225.3

#recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5)) #120




#exercise
#reduce
#Import add from the operator module.
from operator import add
#Import reduce() from functools.
from functools import reduce

prices = [
    (6.99, 5),
    (2.94, 15),
    (156.99, 2),
    (99.99, 4),
    (1.82, 102)
]
#writing a function named product_sales that takes a single two-member tuple made up of a price and a number of units sold. 
#product_sales should return the product of the price and the number of units
def product_sales(passed_tuple):
    price, units = passed_tuple
    return price * units

# Create a variable named total. 
#Use map() to find the per-product totals for each item in prices, then use reduce (and add) to find the total value.
total = reduce(add, map(product_sales, prices))




#exercise - recursion
courses = {'count': 2,
           'title': 'Django Basics',
           'prereqs': [{'count': 3,
                     'title': 'Object-Oriented Python',
                     'prereqs': [{'count': 1,
                               'title': 'Python Collections',
                               'prereqs': [{'count':0,
                                         'title': 'Python Basics',
                                         'prereqs': []}]},
                              {'count': 0,
                               'title': 'Python Basics',
                               'prereqs': []},
                              {'count': 0,
                               'title': 'Setting Up a Local Python Environment',
                               'prereqs': []}]},
                     {'count': 0,
                      'title': 'Flask Basics',
                      'prereqs': []}]}

#it recursively finds all of the prerequisite course titles in courses
def prereqs(data, pres=None):
    pres = pres or set()
    # for each prereq in this courses' prereqs...
    for prereq in data['prereqs']:
        # add title of this prereq course, then...
        pres.add(prereq['title'])
        # use recursive call to find further prerequisites of this course, if any
        prereqs(prereq, pres)
    # return current 
    return pres


