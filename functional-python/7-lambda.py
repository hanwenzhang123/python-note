lambda, like def, is the keyword that marks a new function. 
Lambda functions don't have to have a name, though. It is anonymous function.
Lambdas can't contain new lines (outside of containers) or assignments.
It is useful when we do not want to write a function but just throw a thing in there


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

# print(reduce(product, [1, 2, 3, 4, 5]))

def add_book_prices(book1, book2):
    return book1 + book2

# total = reduce(add_book_prices, [b.price for b in BOOKS])

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
#print(long_total(None, None, [b.price for b in BOOKS]))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
# print(factorial(5))

### LAMBDA ###          #automatically return the last value that is calculated
total = reduce(lambda x, y: x + y, [b.price for b in BOOKS]) 
print(total) # $225.3
long_books = filter(lambda book: book.number_of_pages >= 600, BOOKS)
print(len(list(long_books))) #12
good_deals = filter(lambda book: book.price <= 6, BOOKS)  #6


#exercise 1
#Use a lambda and filter() to create a variable named high_cal with only the items in meals where the "calories" value is greater than 1000.
meals = [
    {'name': 'cheeseburger',
     'calories': 750},
    {'name': 'cobb salad',
     'calories': 250},
    {'name': 'large pizza',
     'calories': 1500},
    {'name': 'burrito',
     'calories': 1050},
    {'name': 'stir fry',
     'calories': 625}
]
high_cal = filter(lambda cal: cal['calories'] > 1000, meals)



#exercise 2
#Use reduce() and a lambda to find the longest string in strings. Save this value in the variable longest.
#reduce() takes two arguments and you can write an if statement like: give_me_this if this_thing > that_thing else give_me_that.

from functools import reduce

strings = [
    "Do not take life too seriously. You will never get out of it alive.",
    "My fake plants died because I did not pretend to water them.",
    "A day without sunshine is like, you know, night.",
    "Get your facts first, then you can distort them as you please.",
    "My grandmother started walking five miles a day when she was sixty. She's ninety-seven know and we don't know where she is.",
    "Life is hard. After all, it kills you.",
    "All my life, I always wanted to be somebody. Now I see that I should have been more specific.",
    "Everyone's like, 'overnight sensation.' It's not overnight. It's years of hard work.",
]

longest = reduce(lambda a, b: a if (len(a) > len(b)) else b, strings) 
