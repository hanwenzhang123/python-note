Since filter(), map(), sorted(), and friends all return iterables, we can chain them together. 
Chained functions resolve, or happen, from the inside out, so the innermost function runs first.

This is another reason why functions usually return a value at the end. It makes it easier to use them all together.

any(iterable) returns True if any of the items in the iterable are truthy. 
Similar is the function all(). all(iterable) returns True if all of the items in the iterable are truthy.



#stock.py
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
    return any(["Roland" in subject for subject in book.subjects]) #anything here passed even just one true will be returned True

def titlecase(book):
    book = copy(book)
    book.title = book.title.title()
    return book

#print(list(map(titlecase, filter(has_roland, BOOKS))))

def is_good_deal(book):
    return book.price <= 5

cheap_books = sorted(
    filter(is_good_deal, map(sales_price, BOOKS)),      #map() here we turn all our book to sales price then filter out if it good deal
    key=attrgetter('price')
)
print(cheap_books[0].price)




#exercise
#map and filter
import datetime

birthdays = [
    datetime.datetime(2012, 4, 29),
    datetime.datetime(2006, 8, 9),
    datetime.datetime(1978, 5, 16),
    datetime.datetime(1981, 8, 15),
    datetime.datetime(2001, 7, 4),
    datetime.datetime(1999, 12, 30)
]

today = datetime.datetime.today()

#Create a function named is_over_13 that takes a datetime and returns whether or not the difference between that datetime and today is 4745 days (13 years × 365 days, ignoring leap years) or more.
def is_over_13(dt):
    # compare total days
    delta = today - dt
    return delta.days >= 4745

#Create a function named date_string that takes a datetime and returns a string like "May 20" using strftime. The format string is "%B %d".
def date_string(dt):
    return dt.strftime("%B %d")

#Use map() and filter(), along with your two functions, to create date strings for every datetime in birthdays so long as the datetime is more than 4745 days (13 years × 365 days, ignoring leap years) old.
birth_dates = map(date_string, filter(is_over_13, birthdays))




#map and filter comprehension
#Using c_to_f and a list comprehension, create a variable named good_temps. 
#Convert each Celsius temperature into Fahrenheit, but only if the Celsius temperature is between 9 and 32.6.

temperatures = [
    37,
    0,
    25,
    100,
    13.2,
    29.9,
    18.6,
    32.8
]

def c_to_f(temp):
    """Returns Celsius temperature as Fahrenheit"""
    return temp * (9/5) + 32

good_temps = [c_to_f(temp) for temp in temperatures if temp > 9 and temp < 32.6]
