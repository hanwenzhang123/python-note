python delete files and directory directly without moving to the trash
directory needs to be empty before you try to delete them

import os
os.remove('bootstrap/js/treehouse.js')
os.rmdir('bootstrap/img') #empty, so it deleted
os.rmdir('bootscrap/js/') #OSError because it is not empty

>>> for thing in os.scandir('bootstrap/js/')      #remove before deleting
...     if thing.is_file():
...         os.remove(thing.path) 
>>> os.rmdir('bootstrap/js/')   #now deleted

>>> os.makedirs('bootstrap/js/packages/stuff')  #delete multiple directories until non-empty
>>> os.removedirs('bootstrap/js/packages/stuff')

pip3 install send2trash
python
>>> from send2trash import send2trash #not delete directly but send to trash
>>> send2trash('tree.py')



#exercise - purging
import os

# Make a function named delete_by_date.
# It should take date string like 2015-10-31 and delete any files in the "backups"
#local directory that have that date in their filename.
# Just like the last challenge, the files will be named in the format "year-month-day-username.extension".

def delete_by_date(date):
    for f in os.listdir(os.getcwd() + '/backups'):
        if date in f:
            os.remove('backups/' + f)
            
#Now create a second function named delete_by_user that works similarly but deletes files that have a particular username in their filename.
            
def delete_by_user(date):
    for f in os.listdir(os.getcwd() + '/backups'):
        if date in f:
            os.remove('backups/' + f)

