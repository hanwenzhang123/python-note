functools.partial lets you preset some arguments to a function. 
You can then call the new function with the remaining arguments as needed. 
This often ends up being really handy when used with map() and filter().
A partial - What do we call an instance of a function with some arguments already filled in?

partially call or partially apply a function
import from functools like reduce

#stock.py
from copy import copy
from functools import partial, reduce
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

### LAMBDA ###
# total = reduce(lambda x, y: x + y, [b.price for b in BOOKS])
# long_books = filter(lambda book: book.number_of_pages >= 600, BOOKS)
# good_deals = filter(lambda book: book.price <= 6, BOOKS)

### PARTIALS ###
def mark_down(book, discount):
    book = copy(book)
    book.price = round(book.price-book.price*discount, 2)
    return book

standard = partial(mark_down, discount=.2)
#print(standard(BOOK[0].price) #10.84
half = partial(mark_down, discount=.5)
#print(standard(BOOK[5].price)  #4
half_price_books = map(half, filter(is_long_book, BOOKS))
#print(list(half_price_books))  #half price for all bookd and return a list


#exercise
#First, import partial from functools.
from functools import partial

prices = [
    10.50,
    9.99,
    0.25,
    1.50,
    8.79,
    101.25,
    8.00
]


def discount(price, amount):
    return price - price * (amount/100)

#use partial to make a version of discount that applies a 10% discount. 
#Name this partial function discount_10
discount_10 = partial(discount, amount=10)

#Follow that same pattern to make discount_25 and discount_50 with 25% and 50% discounts each.
discount_25 = partial(discount, amount=25)
discount_50 = partial(discount, amount=50)

#I need to see all of our prices with each discount applied. 
#Use map() to create prices_10, prices_25, and prices_50 where you discount all of the prices with the appropriate discount.
prices_10 = map(discount_10, prices)
prices_25 = map(discount_25, prices)
prices_50 = map(discount_50, prices)
