#writing to files

open(filename, mode="r")opens a file. More info in the docs.
file.write("hello world") would write "hello world" to whatever file the file variable points at.
file.close() closes the pointer to the file file.
The two most common modes or flags for writing are "w", for truncating and then writing, and "a" for appending to the file.

The context manager pattern for dealing with files is:
with open("my_file.txt", "a") as file:
    file.write("Hello world")
    
    
    
def rememberer(things):
  #open file      # file = open("database.txt", "a") 
  with open('database.txt', 'a') as file: # make a block and it will goes away itself once it is done so we don't need close()
    #write thing on file
    file.write(thing+"\n")  #\n - starts a new line
#   #close file
#   file.close()    # we don't need to close file now because we use the with as block
  
if __name__ == '__main__':
  rememberer(input('What should I remember?'))
  

  
  
#reading from files

open(filename, mode="r")opens a file. More info in the docs.
file.read(bytes=-1) would read the entire contents of the file. You can control the number of bytes read by passing in an integer. Relatedly, file.seek() will move the read/write pointer to another part of the file.
file.readlines() reads the entire file into a list, with each line as a list item.

The context manager pattern for dealing with files is:
with open("my_file.txt", "r") as file:
    file.read(10)

sys.argv - The list of command line arguments passed to a Python script. 
argv[0] is the script name (it is operating system dependent whether this is a full pathname or not). 
all the argument after your filename 
#console
python remember.py juice boxes
#here juice boxes is argv[1:], remember.py is argv[0]



import sys

def rememberer(things):
  #open file use with as context manager     # file = open("database.txt", "a")  - original code with close()
  with open('database.txt', 'a') as file: # make a block and it will goes away itself once it is done so we don't need close()
    #write thing on file
    file.write(thing+"\n")  #\n - starts a new line
    
def show():
  #open file
  with open('database.txt', 'r') as file:   # 'r' is the default, we do not need to indicate
    for line in file:   #python treats files like they are iterable
      print(line)
      # we do not need to close it because the context manager does it for us
    
if __name__ == '__main__':
  if sys.argv[1].lower() == '--list':   #in the console 'python remember.py --list'
    show()
  else:
    rememberer(' '.join(sys.argv[1:]))  #join together with space
    

#in the console
python
>>> file = open('teachers.txt')
>>> file.read(10)   # only show the 10 bytes of the file
>>> file.read() or file.read(-1)    #read the entire file
>>> file.seek(0) # need that argument 0 to reset the reading process, otherwise read keeps going from last record
>>> file.read(15) # 15 bytes

>>>lines = file.readlines()
>>>len(lines)     #check how many lines in the file
>>>for line in lines:
...   print(line[::1])    # everything reverse

  
  
