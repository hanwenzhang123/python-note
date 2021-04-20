# lists are a data structure that allow you to group multiple values together in a single container.
# lists are mutable, we can change them, data type not matter
# empty string literal - ""
# empty list literal - []
# .append() - append items, modify exsiting list
# .extend() - combine lists
# ~ = ~ + ~ - combine and make a new list, not affecting the original one
# indexing in Python is 0-based
# python -i ~.py - -i: makes python docs interactive
# .insert(#, '~') - Insert adds elements to a specific location, and the first element is 0.
# .insert(0, '~') - insert to the beginning of the list
# You can access a specific character on a String by using an index, but you cannot change it.
# '\N{~}' - add Unicode in python
# del - delete, only the label not the value, you can still use and access the value
#.pop() - delete the last item and you can also put in an index number




# meeting.py

attendees = ['Ken', 'Alena', 'Treasure']
attendees.append('Ashley')
attendees.extent(['James', 'Guil'])
optional_invitees = ['Ben', 'Dave']
potential_attendees = attendees + optional_invitees
print('there are', len(potential_attendees), 'attendees currently') #8




# wishlist.py

books = [
    "Learning Python: Powerful Object-Oriented Programming - Mark Lutz",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

print("suggested_gift: {}".format(books[0]))
    
    
python -i wishlist.py  # -i: makes python docs interactive
books[0] #first element
books[-1] #last element
books[len(books) -1] #last element

books.insert(0, 'learning Python: powerful object-oriented programming')
books[0] += ' - Mark Lutz'




# What is stored in the variable advisor? - "Rasputin"
surname = "Rasputin"
advisor = surname
del surname
# del just deletes the label, not the value. surname is no longer available, but advisor still is.

