os library

Paths:
  absolute - entire full path from root to where you are
  relative - one location to another location like ..
  
  .. move up one directory
  . current directory


>>> import os
>>> os.getcwd() #see where we are
>>> os.chdir('..') #change current working directory

>>>os.path.isabs('/home/treehouse/workspace') #True
>>>os.path.isabs('workspaces') #False, it is relative here



#exercise
#write a function named absolute that takes two arguments, a path string and a root string.
#If the path is not already absolute, return the path with the root prepended to it.
#For example: absolute("projects/python_basics/", "/") would return "/projects/python_basics/" while absolute("/home/kenneth/django", "C:\") would return "/home/kenneth/django".

import os

def absolute(path, root):
    if(not os.path.isabs(path)):
        new_path = ''.join((root, path))
        return new_path
    else:
        return path
