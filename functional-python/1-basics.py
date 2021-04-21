Computation is the evaluation of functions
Programming is done with expressions
No side-effects from computation
Functions are first-class citizens
Functions should be limited in scope and functionality

global and nonlocal let you work with variables from a higher scope. You should have a really good reason before using either of these!
global keyword lets you change variables outside of your current scope

Bad examples using in the function:
del student['Kenneth']
students.sort()
students.pop(0)


#functions.py

def log_and_run(func):
    print("I just got {}".format(func.__name__))
    return func()   #return another function


def log_and_return(func):
    print("I just got {}".format(func.__name__))
    return func  #return another function, so the example  say_hello  works

def say_hello():
    print('Hello!')
    
print("log and run:")
log_and_run(say_hello)

print("log and return:")
hola = log_and_return(say_hello)
hola()

'''
log and run:
I  just  got  say_hello
Hello!
log and return:
I  just  got  say_hello
Hello!
'''


#fist class function exercise

'''Create a function named apply that should take three arguments: a function and two arguments. 
    apply should return the result of calling the function with the two arguments.'''

def apply(func, arg1, arg2): #The variable func is going to be the function to use. 
    return func(arg1, arg2)
  
  
  
    
