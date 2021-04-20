# A dictionary is a set of key value pairs and contain ',' separated values
# In dictionary, each of its values has a label called the key, and they are not ordered
# Dictionaries do not have numerical indexing, they are indexed by keys.


# [lists]
# {dictionaries}
# {key:value, key:value, key:value} - dictionary
# key is a label for associated values
# {'name':'Hanwen', 'profession':'social worker'}


# store data in dictionary allows you to group related data together and keep it organized
# unlike a list or a tuple, the order of the key value pairs does not matter, but keys have to be unique
# if you add a key value pair to your dictionary that uses a duplicate key, the original one will be forgotten
# key can be any immutable typles. values can be any type.
# dictionaries can be grow or shrink as needed, key value pairs can always be added or deleted. 


course = {'teacher': 'ashley', 'title': 'dictionaries', 'level': 'beginner'}
print(course['teacher'])

course.keys() #access to every keys in the dictionary
course.values() #access to every values in the dictionary

#sorting by the alphabetic order
sorted(course.keys())
sorted(course.values())



#update and mutate dictionaries

#assign it a new value using =, override in the dictionary
course['teacher'] = 'treasure' 
course['level'] = 'intermediate' 

#create a new key-value pair inside the dictionary because no match at the original one
course['stages'] = 2

#del - the value you want to remove, delete
del(course['stages'])




#iterating - iterate over using for loop
for item in course:
  print(item) #only the keys
  print(couse[item]) #only the values

# .items() method to list tuples that represent key value pairs
print(course.items())
#[('teacher': 'ashley'), ('title': 'dictionaries'), ('level': 'beginner')]

for key, value in course.items(): #first element assigned to key, second element assigned to value
  print(key)
  print(value)
  
#one to print the key and one to print the value of the current item.  
pets = {'name':'Ernie', 'animal':'dog', 'breed':'Pug', 'age':2}
for key, value in pets.items():
  print(key)
  print(value)
  

  
  
  # exercises
 # iterate over all the key:value pairs in the student dictionary.

student = {'name': 'Craig', 'major': 'Computer Science', 'credits': 36}

for key, val in student.items():
    print(key)
    print(value)
    
    
# iterate over only the keys in the student dictionary.

student = {'name': 'Craig', 'major': 'Computer Science', 'credits': 36}

for key in student.keys():
    print(key)
    
    
#  iterates over only the values in the student dictionary.

 student = {'name': 'Craig', 'major': 'Computer Science', 'credits': 36}

for val in student.values():
    print(val)
