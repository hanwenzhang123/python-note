lists are mutable
Sorting lists is often required to solve a particular problem, but that changes/replaces the list! 

sorted() takes an iterable to sort and returns a new list from it. If you need to customize the sorting, pass a function in as the key argument. There's an optional reverse argument that will cause the results to be reversed before they're returned.
operator.itemgetter()gets items from an object that supports that operation. We use it to get keys from dicts but it has other uses too.
operator.attrgetter() gets attributes from an object.

reversed() is important but isn't all the unique or remarkable for a video right next to sorted(reverse=True) so I left it out. But good job, you, finding it here!
reversed() takes an iterable and reverses it, returning a new iterable. This new iterable has to be turned into a list/tuple/etc to get items from it by index.



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

# pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))
# print(pub_sort[0]['publish_date'], pub_sort[-1]['publish_date'])
# pages_sort = sorted(BOOKS, key=attrgetter('number_of_pages'))
# print(pages_sort[0].number_of_pages, pages_sort[-1].number_of_pages)

#important_list = [5, 3, 1, 2, 4]
#important_list.sort()  # Bad idea, sorts list in place
# sorted(important_list)  # Sorts a copy of the list


