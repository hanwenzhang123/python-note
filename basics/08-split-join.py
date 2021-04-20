# .join() - join your element together into a single string, Join takes an iterable and turns it into a string
# .split() - split each word, Split is on strings, but that creates a list from string
# .sleep() - put in the second in the ()


>>> mary = 'Mary had a little lamb'
>>> mary.split() 
['Mary', 'had', 'a', 'little', 'lamb'] 


>>> list('hello world')
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'] 

	
>>> mwords
['Mary', 'had', 'a', 'little', 'lamb'] 
>>> ' '.join(mwords)
'Mary had a little lamb'



# meeting.py

attendees = ['Ken', 'Alena', 'Treasure']
attendees.append('Ashley')
attendees.extent(['James', 'Guil'])
optional_invitees = ['Ben', 'Dave']
potential_attendees = attendees + optional_invitees
print('there are', len(potential_attendees), 'attendees currently') #8

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)
print("To: " + to_line)
print("To: " + cc_line)




quote = "the greatest teacher failure is"
words = quote.split() # now we have strings with each word

import time
for word in words:
    print(word)
    time.sleep(.5) # each word comes out half second

	

# 	exercise
# If I had a list and I wanted to turn it into a string by combining each value together with a specified separator.
# What method would I use?  
# # join. it is on string


# I saw a pretty great shirt today.
# If I had that text in a string like so:
# text = "Ada&Jean&Grace&Margaret"
# What code could I use to convert it to a list?
# # text.split('&')
