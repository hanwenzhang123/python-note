#CSV
CSVs, or comma-separated value files, are a common file-based database-like format.
Python has a built-in `csv` module that makes working with these files quick and easy.
DicReader() - read and return back as dictionary - working with reader, read and parse the value
DictWriter() - write and edit files

#artifacts.py     
import csv

with open('museum.csv', newline='') as csvfile: #here we use newline with an empty string is because we have a new line inside of a quoted section then we want to be sure and be able to differentiate that from an actual new line making a new line
  artreader = csv.DicReader(csvfile, delimeter='|')  #using '|' to separate file
  rows = list(artreader)
  for row in row[1:3]:
    print(row['ManuCity'])
   

#teachers.py
import csv

with open('teachers.csv', 'a') as csvfile:
  fieldnames = ['first_name', 'last_name', 'topic']
  teachwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
  
  teachwriter.writeheader()
 
  teachwriter.writerow({
    'firstname': 'Kenneth',
    'lastname: 'love',
    'topic': 'python'
  })
  teachwriter.writerow({
    'firstname': 'Alena',
    'lastname: 'Holligan',
    'topic': 'PHP'
  })

  
  
# JSON
JSON is quickly becoming the de facto standard for Web-based communication. 
JSON modual is handy for encoding and decoding data from JSON, you will use it when you receive info in you API or sending to an API
Most APIs expect, accept, and return JSON and many pieces of desktop software use JSON for configuration files. 
Let's see how to use Python's built-in `json` module to read and write this handy format.
  
# Parse JSON - Convert from JSON to Python
JSON decoding - turn JSON encoded/formatted data into Python Types 
load() takes a file object and returns the json object. a JSON formatted value into Python object
If you have a JSON string, you can parse it by using the json.loads() method.
 
json.load() method (without “s” in “load”) used to read JSON encoded data from a file and convert it into a Python dictionary.
json.loads() method, which is used to parse valid JSON string into Python dictionary.
To parse JSON from URL or file, use json.load(). For parse string with JSON content, use json.loads().

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
  
  
  
# Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
json.dumps() method can convert a Python object into a JSON string.
json.dump() method can be used for writing to JSON file.

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)



#art.py
import json

with open('148.json') as artfile:
  art = json.load(artfile)      #take a file-like object and tried to turn that into a python object 
  print(art['description'])    #get the description from the artfile json file
  
  
  
#in the console
>>> import json
>>> nums = json.loads("[1, 2, 3]")    #parse a valid JSON string and convert it into a Python Dictionary
>>> nums[2] #3

>>> json.dumps([5, 4, 3, 2, 1])   #opposit of loads

me = {'first_name': Kenneth, 'last_name': 'Love', topic: 'Python'}
>>> json.dumps(me)    #same print out as >>> str(me) but different outcome
>>> craig = {'first_name': Craig, 'last_name': 'Dennis', topic: 'Java'}
>>> with open('teachers.json', 'a') as teacherfile:
...   json.dump([me, craig], teacherfile)   # we put the me and craig dicts we just created to a new json file called teachers.json
 

   
