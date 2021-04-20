#exercise

# Write a function named first_number that takes a string as an argument. 
# The function should search, with a regular expression, the first number in the string and return the match object.
# numbers() that takes two arguments: a count as an integer and a string. 
# Return an re.search for exactly count numbers in the string.

import re

def first_number(str):
    return re.search(r'\d', str)

def numbers(count, myString):
    return re.search(r'\d'*count, myString) 


#reate a function named find_words that takes a count and a string. 
#Return a list of all of the words in the string that are count word characters long or longer.
import re

# EXAMPLE:
# >>> find_words(4, "dog, cat, baby, balloon, me")
# ['baby', 'balloon']

def find_words(count, string):
    return re.findall(r'\w' * count + '\w*', string)



#Create a function named find_emails that takes a string. 
#Return a list of all of the email addresses in the string.

import re

# Example:
# >>> find_email("kenneth.love@teamtreehouse.com, @support, ryan@teamtreehouse.com, test+case@example.co.uk")
# ['kenneth@teamtreehouse.com', 'ryan@teamtreehouse.com', 'test@example.co.uk']
def find_emails(str):
    return re.findall(r'\b[\w.+]+@[\w.]+\b', str)



#re.match() against string
#provide two groups, one for a last name match and one for a first name match. 
#The name parts are separated by a comma and a space.

import re

string = 'Perotto, Pier Giorgio'

names = re.match(r'''
    ^(?P<last_name>[\w]*),\s                # Last name
    (?P<first_name>[\w\s\w]*)$           # First name
''', string, re.X)





import re

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'''  
    (?P<email>[-\w\d.+]+@[-\w\d.]+) 
     ,\s
     (?P<phone>\d{3}-\d{3}-\d{4})''' 
     , string, re.X | re.M) 

twitters = re.search(r''' 
    (?P<twitter>@[\w\d]+)$  
    ''', string, re.X|re.M)



#Create a variable named players that is an re.search() or re.match() to capture three groups: last_name, first_name, and score. 
import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'''
  (?P<last_name>[\w ]*)
  ,\s
  (?P<first_name>[\w ]*)
  :\s
  (?P<score>[\d]*)
''', string, re.X | re.M)

class Player


#create a class named Player that has those same three attributes, last_name, first_name, and score. 
class Player:
  def __init__(self, last_name, first_name, score):
    self.last_name = last_name
    self.first_name = first_name
    self.score = score
    
    


#Questions
^ - What symbol starts a set to mean "don't match any of these characters"?
.finditer() - What method gives us an iterable full of match objects?
{5,} - What would I use to match 5 or more occurrences of a pattern?
match_object.group('email') - How would I get the contents of the group named email from my match object?
re.search(r'\d', 'The Mach 5') - Match the number in the string with an escape character.
re.MULTILINE  - makes it so newlines are treated as individual strings.
re.search(r'(?P<name>[\s\w]+)', 'Kenneth Love') - Name the following group "name".

Why would you want to compile a pattern?
    It is going to be used multiple times
    I want to be able to pass it to functions
    I want to be able to use it directly
    I want to provide multiple patterns as part of a library
