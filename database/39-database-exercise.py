#exercise

from peewee import *
#Create a variable named db that is an SqliteDatabase with a filename of challenges.db.
db = SqliteDatabase('challenges.db')

class Challenge(Model):
    name = CharField(max_length=100)
    language = CharField(max_length=100)
    steps = IntegerField(default=1)
#Now add db as the database attribute in the Meta class for Challenge
    class Meta:
        database = db
#Your initialize() function should connect to the database and then create the Challenge table. 
#Make sure it creates the table safely.
def initialize():
    db.connect()
    db.create_tables([Challenge], safe=True)
    

    
    
#Import OrderedDict from the collections module.
from collections import OrderedDict

#Now create an OrderedDict named menu. Both keys and values will be strings.
menu = OrderedDict([  
    ('n', 'new challenge'),
    ('s', 'new step'),
    ('d', 'delete a challenge'),
    ('e', 'edit a challenge'),
])

   
  
#Create a function named create_challenge() that takes name, language, and steps arguments. 
#Steps should be optional, so give it a default value of 1. 
#Create a Challenge from the arguments. create_challenge should not return anything.

from models import Challenge

def create_challenge(name, language, steps=1):
  Challenge.create(name=name, language=language, steps=steps)

#Return all Challenges where the name field contains name argument and the language field is equal to the language argument. 
#Use == for equality. You don't need boolean and or binary & for this, just put both conditions in your where().
    
def search_challenges(name, language):
    return Challenge.select().where(
      Challenge.name.contains(name), 
      Challenge.language==language)
  
#Create a function named delete_challenge that takes a Challenge as an argument. 
#Delete the specified Challenge. Your function shouldn't return anything.  

def delete_challenge(challenge):
    challenge.delete_instance()
  
  
  
  
#questions
What field type should I use if I want to store large blocks of text?
TextField()
  
I want to print as many equal signs as there are characters in my title variable:
print('='*len(title))

I want to sort my diary entries based on their timestamp attribute in a descending manner, so newer records are first:
Entry.select().order_by(Entry.timestamp.desc())
  
What method lets you query against part of a string?
We use .contains() to match substrings.

I don't want to be able to have a duplicate record for UPCs in my database. Finish the model below:
class Product(Model):
    name = CharField()
    description = TextField()
    upc = CharField(max_length=100, unique=True)
    
What kind of software library is Peewee?
An ORM

What does the os.system() function let us do?
Use system-level utilities or aplications

What method lets us change how fetched records are sorted?
order_by()

You can use OrderedDict anywhere you'd use dict.
