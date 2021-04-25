>>> import os
>>> os.getcwd()
>>> os.path.join(os.getcwd(), 'backups')  #join to a new directory called backups
>>> os.path.join(os.getcwd(), '...', 'backups')

>>> import pathlib
>>> path = pathlib.PurePath(os.getcwd())
>>> path2 = path / 'examples' / 'paths.txt' # a txt in the example directory of current path

>>> path2.parts  #gets all the tuples
>>> path2.root  #'/'

>>> path2.parents[2]  #PurePosixPath('/~~/~~/~~') the first three

>>> path2.name # the final name here is paths.txt
>>> path2.suffix # the final extension here is .txt


#exercise
If I'm using os.path.join(), do I need to provide the separator between path pieces?
Nope

Complete the following code snippet to get to the examples/python/ directory inside of the current directory:
os.path.join(os.getcwd(), "examples", "python")

When using Pathlib, is this a valid way to make a path? Yes
partial_path / "examples" / "pathlib.txt"

I need to get to the directory above the one I'm currently in. Finish this code snippet for me:
os.path.join(os.getcwd(), "..")
