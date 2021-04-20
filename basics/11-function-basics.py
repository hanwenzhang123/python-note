# What is a Function?
# A function is a reusable block of code that’s given a name. Functions should accomplish one programming task, and do that task very well. They allow us to keep our code clean and DRY - dry meaning "Don’t Repeat Yourself".

# How to Write a Function?

# A function definition
def my_function_name():
    print("Hello, I'm a function!")

# Calling/invoking the my_function_name function
my_function_name()



def print_name():
  print("Hanwen")

def print_favorite_movie():
  print("Mean Girls")
  
  print_favorite_movie() #run the python

  
#scope
 # scope - refers to the visibility of parts of our program
 # the code that you write in a function that is only accessible inside a function
 # When the program is executing inside a function, that’s called the local context. 
# Variables inside the local context, or inside a function, are only visible inside that function. 
# Variables in the global context, or the highest level of the program, can be seen and accessed by the entire program.
  

num = 10 # gloobal context
  
  def set_num():
    num = 5 # new num, local context, only exist here but you can use global inside a function
    letter = 'a' # it is only exist here, only can use inside the function
    print(letter)
    
# set_num()

    
# return
# without the return what happen inside them, stay inside them
# we have to retun in order to access outside the function
# return is the keyword used to get values back out of functions.

def two_plus_two():
  val = 2 + 2
  return val    # return value sends back to the function
  
print(two_plus_two()) # the two_plus_two() itself is a function, need to print it out

sum = two_plus_two() # create a variable here
print(sum)
  
  
  
# parameter - function can receive value too
def add_two(num):  # num here serves as a special variable
  print (num) # The variable, num is printed before the addition is done.
  val = num + 2
  return val

add_two(5)   # 5
# rewrite our function so it can receive a value which stored in the parameter variable called num


# two parameters
def add_two_nums(num1, num2):  # no 2 same names and order matters
  val = num1 +  num2
  return val

print(add_two_nums(5, 10))   # 15



# exercise
def hello_student(name):
   return 'Hello ' + name

hello = hello_student("Hanwen")
