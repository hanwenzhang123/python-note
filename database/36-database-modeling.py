ORM - object relational mapping
ORMs are for converting data sources into Python objects and vice versa, usually through SQL.
Models - are the classes that represent tables in our ORM called

pip install peewee - install peewee on your local device 

model - A code object that represents a database table, models in peewee are Python classes
SqliteDatabase - The class from Peewee that lets us connect to an SQLite database
Model - The Peewee class that we extend to make a model
CharField - A Peewee field that holds onto characters. It's a varchar in SQL terms
max_length - The maximum number of characters in a CharField
IntegerField - A Peewee field that holds an integer
default - A default value for the field if one isn't provided
unique - Whether the value in the field can be repeated in the table
.connect() - A database method that connects to the database
.create_tables() - A database method to create the tables for the specified models.
safe - Whether or not to throw errors if the table(s) you're attempting to create already exist


#students.py
from peewee import *

db = SqliteDatabase('student.db')   #make database connection

class Student(Model):   #always name a singular name, model is single data
  username = CharField(max_length = 255, unique = True)
  points = IntegerField(default = 0)

  class Meta:   #class inside the class
    database = db   #the database we created
    
 if __name__ == '__main__':   #here to connect the database to get data out
  db.connect()        #conncet to a database
  db.create_tables([Student], safe = True)    #create a table called student, need to pass safe = True
  
  
  
#exercise
  
#Import everything from the peewee library.
from peewee import *

#make a database connection.
#Make an SqliteDatabase() named "challenges.db". 
#Assign it to the variable db.
db = SqliteDatabase('challenges.db')

#Make a model named Challenge that has two fields, name and language. 
#Both fields should be of the type CharField with a max_length of 100.
class Challenge(Model):
    name = CharField(max_length=100)
    language = CharField(max_length=100)
#add a Meta class to Challenge and set the database attribute equal to db.
    class Meta:   
      database = db
  
# db.connect() -  What method would we call on our database (db) to create a connection to it?
# db.create_tables([Challenge], safe = True)


 
