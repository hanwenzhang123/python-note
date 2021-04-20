# logging 
# records an information passed in by the user and ask for those logs if something unexpected happens
# you can also log exception in your except blocks

# level - The level that you want to start logging messages at. Any message at this level or above will be logged.
# Logging Levels:
# CRITICAL - horribly wrong
# ERROR - horribly wrong
# WARNING - questionable things
# INFO
# DEBUG
# NOTSET

# Example:
#   import logging
# try:
#     [1, 2, 3].remove(4)
# except ValueError:
#     logging.error("tried to remove an invalid value")
#     print("Sorry, that value doesn't exist.")

import logging #just like import random

# logging.info ("you won't see this")
# logging.warn("oh no") #this will show up in console

logging.basicConfig(filename = 'game.log', level = logging.DEBUG)
# what file to log into, here the name is called game,
# level tells when to pay attention to, won't show lower level

monster, door, player['location'] = get_locations()
logging.info('monster: {}; door: {}; player: {}'.format(
  monster, door, player['location']))
# logging the info at that particular level like info, debug, waning



#debugging - PDB - python debugger

import pdb  #import pdb just like import logging, 1st to do

my_list = [5, 2, 1, True, "abcdefg", 3, False, 4]

pdh.set_trace()     # you can do in one line as import pdb; pdb.set_trace(), only time to use ; in python
del my_list[3] #[5, 2, 1, "abcdefg", 3, False, 4]
del my_list[3] #[5, 2, 1, 3, False, 4]
del my_list[4] #[5, 2, 1, 3, 4]
print(my_list)


# in the cnsole
# (Pdb) my_list - check my_list value
# (Pdb) n - next
# (Pdb) c - continue
# (Pdb) q - quit

# afer checking the Pdb, clear the original code, delete the import pdb and pdh.set_trace()



#exercise
# Log a message with a level of DEBUG. The message can say anything you want.
# Log "The French have the Grail" as a WARNING level message.

import logging

logging.basicConfig(filename='cc.log', level=logging.DEBUG)

logging.debug('bug here')
logging.warning("The French have the Grail")



#Import PDB and call set_trace() where it's needed.

import pdb

def something_silly(arg1, arg2):
    if len(arg1) > len(arg2):
        pdh.set_trace()
        arg1[0] = arg2[0]
    return arg1, arg2
