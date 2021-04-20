__method name__ - dunder is for double udners by python community
usually used for conditional check

The __name__ variable (two underscores before and after) is a special Python variable. 
It gets its value depending on how we execute the containing script. 

'__main__' is the name of the scope in which top-level code executes. 

The print(__name__) is being used to show how the variable __name__ changes
depending if the current module is the top level (called directly using python)
or if the current module was imported into another module

the __name__ is changed to "__main__" to indicate the file was called directly. 
Therefore, any code within the if __name__ == "__main__" block will be executed. 


def func1():
   print 'The value of __name__ is ' + __name__
if __name__ == '__main__':
   func1()


#app.py
def print_hello():
  print("hello from app.")

print(__name__)

if __name__ == '__main__':
  print_hello()

  

#second_app.py
import app  #Since app.py was imported, __name__ keeps the module name "app".
              #All other execution during import is block by the if __name__ == "__main__" statement
print("hello from second_app.")
app.print_hello() #referencing the function in the imported file.




#console
python app.py
__main__
hello from app.


python second_app.py
app
hello from second_app.
hello from app.


