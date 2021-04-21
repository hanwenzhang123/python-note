Python decorators let you wrap your existing functions, classes, etcetera with another Python cullible


#Examples

#Nested function:
def outer():
    number = 5

    def inner():
        print(number)
    inner()

outer()  # prints 5


#First-class functions

def apply(func, x, y):
    return func(x, y)

def add(a, b):
    return a + b

print(apply(add, 5, 5))  # prints 10




def apply(func, x, y):
  return func(x, y)

def add(x, y):
  return x + y

def sub(x, y):
  return x - y

print(apply(add, 5, 5)) #10
print(apply(sub, 2, 8)) #-6



#Closures

def close():
    x = 5

    def inner():
        print(x)  #scope
    return inner

closure = close()  # closure is actually a pointer to inner()
closure()  # prints 5


def add_to_five(num):
  def inner():
    print(num+5)
  return inner

fifteen = add_to_five(10)
fifteen()   #print 15



#Decorators - function that accept functions as argument
#A function that return a function, which in turn, returns a function that was acceptde by the outermost function
#you don't want to change every function in the same way over and over again, just change the @ decorator

from functools import wraps

def logme(func):
    import logging  # because we don't want to require users to import it
    logging.basicConfig(level=logging.DEBUG)    #write better python course

    def inner(*args, **kwargs):
        logging.debug("Called {} with args {} and kwargs {}".format(
                  func.__name__, args, kwargs))
        return func(*args, **kwargs)    #tuple and dictionary
    inner.__doc__ = func.__doc__
    inner.__name__ = func.__name__    
    return inner

  @logme
  def sub(x, y):
    '''Returns the difference between two numbers'''
    return x - y
  

  
  #in the shell
from dec import logme
@logme  #syntax sugar
def say_hello():
        print("Hello there!")

say_hello()  # logs the call and then prints "Hello there!"
 
  
from dec import logme
@logme 
def sub(x, y, switch=False):
  return x - y if not switch else y - x

sub(5, 2)   #DEBUG:root:Called sub with args (5, 2) and kwargs {}" 
#3
sub(5, 2, switch=True) #DEBUG:root:Called sub with args (5, 2) and kwargs {'switch': True} 
#-3
                      
from dec import logme
sub.__name__ #sub
