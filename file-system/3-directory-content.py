>>> import os
>>> os.listdir()  #listing everything in the currrent directory
>>> os.listdir('/') #you can provide a path and it will tell you everything in that path
>>> list(os.scandir())  #all the dir entry, returns directory entries along with file attribute information

>>> files = list(os.scandir())
>>> files[3].name
>>> files[3].is_file()  #true
>>> files[3].stat()

>>> scanner = os.scandir()
>>> scanner.close()


#tree.py
import oos

def treewalker(start):
  total_size = 0
  total_files = 0
  
  for root, dirs, files in os.walk(start):
    subtotal = sum(
      os.path.getsize(os.path.join(root, name)) for name in files
    )
    total_size += subtotal
    file_count = len(files)
    total_files += file_count
    print(root, 'consumes', end='')
    print('bytes in', file_count, 'non-directory files')
 print(start, 'contains', total_files, 'files with a combined size of', total_size, 'bytes')

treewalker('bootstrap')



#exercise
#Create a function named dir_contains takes a path to a directory and a list of file names. 
#If all of the file names exist within that directory, return True, otherwise, return False.

import os
def dir_contains(dir_path, file_names):   #second parameter (the list of file names you want to check)
    dir_files = list(os.listdir(dir_path))  
    for file_name in file_names:  #iterate over all those file names in order to check if they are contained in the directory passed as first parameter
        if file_name not in dir_files:
            return False
    return True
