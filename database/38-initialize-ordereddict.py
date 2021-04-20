TextField() - a field that holds a blob of text of any size
DateTimeField() - a field for holding a date and a time
/usr/bin/env what?
If you're not sure what to put after /usr/bin/env, test it out in your terminal program.
in the console do chmod - change mode +x diary.py - ./diary.py

OrderedDict - a handy container from the collections module that works like a dict but maintains the order that keys are added
.__doc__ - a magic variable that holds the docstring of a function, method, or class

sys - a Python module that contains functionality for interacting with the system
sys.stdin - a Python object that represents the standard input stream. In most cases, this will be the keyboard

.where() - method that lets us filter our .select() results
.contains() - method that specifies the input should be inside the specified field

os - Python module that lets us integrate with the underlying OS
os.name - attribute that holds a name for the style of OS
os.system() - method to allow Python code to call OS-level programs



#diary.py
#!/usr/bin/env pyhthon 3

from collections import OrderedDict
import datetime
import os
import sys

from peewee import *

db = SqliteDatabase('diary.db')
  

class Entry(Model):
    content = TextField()   #varchar field have to have maximum length, so we use textfield here
    timestamp = DateTimeField(default=datetime.datetime.now) 
                
    class Meta:
        database = db
 #isn't actually defining a new class. 
 #It's defining attributes of the class you're writing 
 #(in this case, where it should look for its database.)
        
def initialize():
    """Create the database and the table if they don't exist."""
    db.connect()
    db.create_tables([Entry], safe=True)
    
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')
    

def menu_loop():
    """Show the menu"""
    choice = None  # without assigning value, no value
    
    while choice != 'q':
        clear()
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()  #strip out extra spaces
        
        if choice in menu:
            clear()
            menu[choice]()    #we run the function being selected and run
                              #some_func = menu[choice]   #some_func() # or combining into one statement: menu[choice]()

def add_entry():
    """Add an entry."""
    print("Enter your entry. Press ctrl+d when finished.")
    data = sys.stdin.read().strip()   #read brings in all the data
    
    if data:
        if input('Save entry? [Yn] ').lower() != 'n':
            Entry.create(content=data)    #save the entry
            print("Saved successfully!")
            
            
def view_entries(search_query=None):
    """View previous entries."""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))   #where filter out the search
    
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print(entry.content)
        print('\n\n'+'='*len(timestamp))
        print('n) next entry')
        print('d) delete entry')
        print('q) return to main menu')
        
        next_action = input('Action: [Ndq] ').lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)
            
            
def search_entries():
    """Search entries for a string."""
    view_entries(input('Search query: '))

    
def delete_entry(entry):
    """Delete an entry."""
    if input("Are you sure? [yN] ").lower() == 'y':
        entry.delete_instance() #delete that instance
        print("Entry deleted!")
        
 
menu = OrderedDict([      #works like a dictionary but always remember the keys
    ('a', add_entry),     #here are objects
    ('v', view_entries),
    ('s', search_entries),
])
            
    
if __name__ == '__main__':
    initialize()    #the database exist before running the loop
    menu_loop()
  
  
  
 
