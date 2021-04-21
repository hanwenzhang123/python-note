lists are mutable
Sorting lists is often required to solve a particular problem, but that changes/replaces the list! 

sorted() takes an iterable to sort and returns a new list from it. If you need to customize the sorting, pass a function in as the key argument. There's an optional reverse argument that will cause the results to be reversed before they're returned.
operator.itemgetter() gets items from an object that supports that operation. We use it to get keys from dicts but it has other uses too.
operator.attrgetter() gets attributes from an object. 

reversed() is important but isn't all the unique or remarkable for a video right next to sorted(reverse=True) so I left it out. But good job, you, finding it here!
reversed() takes an iterable and reverses it, returning a new iterable. This new iterable has to be turned into a list/tuple/etc to get items from it by index.

itemgetter() operates on dictionaries, while attrgetter() operators on objects. 
Itemgetter looks up an index, attrgetter looks up the attribute rather than the index.
With attrgetter(), you must pass in to key, as a string, the name of the object's attribute on which you want to sort.


#stock.py

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

pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))
print(pub_sort[0]['publish_date'], pub_sort[-1]['publish_date'])  #dict # 1975, 2021
pages_sort = sorted(BOOKS, key=attrgetter('number_of_pages'), rerverse = True) #return in reverse,
print(pages_sort[0].number_of_pages, pages_sort[-1].number_of_pages) #obj # 1141, 245

important_list = [5, 3, 1, 2, 4]
#important_list.sort()  # Bad idea, sorts list in place
sorted(important_list)  # Sorts a copy of the list, returns you a sorted copy
print(sorted(important_list)) # [1, 2, 3, 4, 5]
print(important_list)  #[5, 3, 1, 2, 4]


# exercise - itemgetter
# Import itemgetter from the operator module.
from operator import itemgetter

fruit_list = [
    ('apple', 2),
    ('banana', 5),
    ('coconut', 1),
    ('durian', 3),
    ('elderberries', 4)
]

#create a variable named sorted_fruit that uses sorted() and itemgetter() to sort fruit_list by the second item in each tuple.
sorted_fruit = sorted(fruit_list,  key = itemgetter(1))



# exercise - attrgetter
import datetime
from operator import attrgetter

date_list = [
    datetime.datetime(2015, 4, 29, 10, 15, 39),
    datetime.datetime(2006, 8, 15, 14, 59, 2),
    datetime.datetime(1981, 5, 16, 2, 10, 42),
    datetime.datetime(2012, 8, 9, 14, 59, 2),
]

#Use sorted() and attrgetter() to sort date_list by the day attribute of each datetime object. 
#Save this sorting into a variable named sorted_dates.

sorted_dates = sorted(date_list, key = attrgetter("day"))

#class datetime.datetime
#A combination of a date and a time. 
#Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.

