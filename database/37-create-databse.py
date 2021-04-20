.create() - creates a new instance all at once
.select() - finds records in a table
.save() - updates an existing row in the database
.get() - finds a single record in a table
.delete_instance() - deletes a single record from the table
.order_by() - specify how to sort the records
if __name__ == '__main__' - a common pattern for making code only run when the script is run and not when it's imported
db.close() - not a method we used, but often a good idea. Explicitly closes the connection to the database.
.update() - also something we didn't use. Offers a way to update a record without .get() and .save(). 
      Example: Student.update(points=student['points']).where(Student.username == student['username']).execute()



#students.py
from peewee import *

db = SqliteDatabase('student.db')   

class Student(Model):   
  username = CharField(max_length = 255, unique = True)
  points = IntegerField(default = 0)

  class Meta:  
    database = db   
    
students = [
    {'username': 'kennethlove',
     'points': 14718},
    {'username': 'chalkers',
     'points': 11912},
    {'username': 'joykesten2',
     'points': 7363},
    {'username': 'craigsdennis',
     'points': 4079},
    {'username': 'davemcfarland',
     'points': 14717},
]

def add_students():
    for student in students:
        try:
            Student.create(username=student['username'],  
                           points=student['points'])
        except IntegrityError:    #here we create a new username but above we say 'unique = True', so we can't run twice
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()   #save the record


def top_student():                      #desc gets smaller, asc get bigger
    student = Student.select().order_by(Student.points.desc()).get()  #only get us the first record
    return student
    
    
if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print("Our top student right now is: {0.username}.".format(top_student()))  # 0 is what we came from top_student()

    
    
#exercisee

#Import the Challenge class from models.py.
from models import Challenge

#create a variable named all_challenges. 
#It should select all of the available challenges from the database.

all_challenges = Challenge.select()

#Next, create a new Challenge. 
#The language should be "Ruby", the name should be "Booleans".

Challenge.create(language='Ruby', name='Booleans')
    
#make a variable named sorted_challenges that is all of the Challenge records, 
#ordered by the steps attribute on the model. The order should be ascending, which is the default direction.

sorted_challenges = all_challenges.order_by(Challenge.steps)

      
      
# questions 
To prevent code from being executed when you import a module, put it into a function or class, or inside which if condition:
if __name__ = '__main__:

__name__ is a special variable that refers to the current namespace.

What do we call the text in """ as the first thing in a function or class?
Docstring

Peewee's convention is to import everything with *. Why is this usually considered a bad practice?
1. your local namespace suddenly gets floded by a huge number of item
2. things you have identified locally, or already imported, can be overwritten by the import
3. peewee's contents are no longer contained in the peewee namespace
