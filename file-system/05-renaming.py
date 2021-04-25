>>> import os
os.rename('bootstrap', 'assets') #change bootstrap to assets

os.rename('tree.py', 'script/python/') #error, it is directory

os.renames('assets', 'static/raw') #move assets to static/raw, and make the directory if they are not exist

os.replace('static/raw', 'bootstrap') #replace all things inside the raw to bootstrap

#exercise

#This function should take a string which will be a path to a local directory. 
#The file names in this directory are messy. I need you to clean them up so they all follow the same pattern.

import datetime
import os
import re

# Filenames consist of a username (alphanumeric, 3-12 characters)
# and a date (four digit year, two digit month, two digit day),
# and an extension. They should end up in the format
# year-month-day-username.extension.

# Example: kennethlove2-2012-04-29.txt becomes 2012-04-29-kennethlove2.txt

def cleanup(path):
    for name in os.listdir(path):
        # find the date in the pre-formatted file name
        orig_date = re.search(r'\d{4}-\d{2}-\d{2}', name)
        # format the date correctly
        formatted_date = datetime.datetime.strptime(orig_date.group(), '%Y-%m-%d').date()
        # the file extension is the last 4 characters (i.e. .txt)
        ext = str(name[-4:])
        # concatenate new string as date with a dash plus username plus extension
        # username is found by slicing name up to index of dash (start of date)
        new_str = str(formatted_date) + "-" + str(name[:name.index('-')]) + ext
        # rename files, make sure to join path with file name 
        os.rename(os.path.join(path, name), os.path.join(path, new_str))
