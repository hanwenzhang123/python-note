filter() takes a function and an iterable. The function, like with map(), takes only a single argument and is applied to each item in the iterable. 
If the function returns a truthy value for the item, the item is sent back to filter() which, ultimately, returns a new iterable of the filtered items.

You can achieve the same effect with [item for item in iterable if func(item)]. Again, like with map(), this can be more quickly readable for small applications.

I mentioned filterfalse(). This function works just like filter() but only returns things where the filter function gives back a False or non-truthy value. 


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

# sales_books = list(map(sales_price, BOOKS)) #if we want to get each of them into a list, we need list()
# sales_books2 = [sales_price(book) for book in BOOKS]

### FILTER ###
def is_long_book(book):   #like asking question usually start with is_
    """Does a book have 600+ pages?"""
    return book.number_of_pages >= 600
  
long_books = list(filter(is_long_book, BOOKS)) #like map(), if we want to get each of them into a list, we need list()
print(len(BOOKS)) #same result
                  
long_books2 = [book for book in BOOKS if book.number_of_pages >= 600]
print(len(long_books2)) #same result
                  

    
#exercise
#filter
import datetime

dates = [
    datetime.datetime(2012, 12, 15),
    datetime.datetime(1987, 8, 20),
    datetime.datetime(1965, 2, 28),
    datetime.datetime(2015, 4, 29),
    datetime.datetime(2012, 6, 30),
]
#Write a function named is_2012 that accepts a single argument and returns whether that argument's year attribute is equal to 2012.
def is_2012(argument):
    if argument.year == 2012:
        return True
#create a variable named dt_2012 that uses filter() and is_2012 to return only the datetimes from dates that are from the year 2012.
dt_2012 = filter(is_2012, dates)



#filter comprehension
words = [
    'yellow',
    'red',
    'yesterday',
    'tomorrow',
    'maybe',
    'zucchini',
    'eggplant',
    'year',
    'month',
    'yell',
    'yonder',
    'today',
]

#Create a variable named y_words that uses a list comprehension to only contain the words from words that start with the letter "y".
y_words = [letter for letter in words if letter[0] == 'y']
