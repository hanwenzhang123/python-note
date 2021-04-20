# Parameters are what you use to define the function.
# Arguments are what you pass in. 

# def keyword to define a new function named yell here

def yell(text):
  text = text.upper()
  number_of_characters = len(text)
  result = text +  '!' * (number_of_characters // 2)
  print(result)
# body of the function

yell("you are doing great")
yell("don't forget to ask for help")
yell("don't repeat yourself, keep things dry")




def display_blanks(word):
    blanks = "-" * len(word)
    print(blanks)

print("Puzzle 1:")
display_blanks("treehouse")
print("Puzzle 2:")
display_blanks( "python")


# Puzzle 1:
# ---------
# Puzzle 2:
# ------



# check_please.py

import math

def split_check(total, number_of_people):
  return math.ceil(total / number_of_people)

total_due = float(input("What is the total?"))
number_of_people = int(input("How many people?"))


amount_due = split_check(total_due, number_of_people)
                             
print("each person owes ${}".format(amount_due)) 

# return a value within a function
# import math - import the math module
# math.ceil(~) - the integer round up 
# help(math) - check the math function



def square(number):
    return number * number

result = square(3)
print(result)



# exceptions

import math

def split_check(total, number_of_people):
  if number_of_people <= 1:
      raise ValueError  ('more than 1 person is required to split the check')
  return math.ceil(total / number_of_people)

try:
  total_due = float(input("What is the total?"))
  number_of_people = int(input("How many people?"))
  amount_due = split_check(total_due, number_of_people)
except ValueError as err:
  print("oh no! that is not a valid value, try again...")
  print("({})".format(err))
else:
  print("each person owes ${}".format(amount_due)) 




# raise a ValueError if the product_idea is less than 3 characters long
  
def suggest(product_idea):
    if len(product_idea) < 3:
        raise ValueError("Please try again.")
    return product_idea + "inator"
