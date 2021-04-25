#make your own slugify function in slug.py. Your function should accept two arguments, a string to make into an acceptable file or directory name, and a path.
#Slugs should be unique for their path (you can't have two files or directories with the same name in the same directory), slugs shouldn't have spaces in them, and slug should start with a number, letter, or underscore. 

import os
import re
import unicodedata

def slugify(my_string, my_path=''):
    my_string = unicodedata.normalize('NFKC', my_string)
    if not re.match(r'^[\w\d_]', my_string): # Is the first character valid?
        my_string = 'stub_' + my_string
    my_string = re.sub(r'\s+', '_', my_string) # Remove spaces.
    if my_path:
        my_slug = os.path.join(my_path, my_string) # If there's a path, add the stub.
        if os.path.exists(my_slug):
            print("File exists.  Try again.")
            return
        else:
            return my_slug
    else:
        return my_string
    return
