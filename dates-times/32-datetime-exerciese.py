
# exercise
import datetime

now = datetime.datetime.now()
two = now.replace(hour = 14)    # holds the value of now with the hour set to 14
two = now.replace(hour=14, minute=30)   #change two so its minute is 30


import datetime

def far_away(time): # takes one argument, a timedelta
    return time + datetime.datetime.now()
#Add that timedelta to datetime.datetime.now() and return the resulting datetime object.


#Write a function named minutes that takes two datetimes and, using timedelta.total_seconds()
#get the number of seconds, returns the number of minutes, rounded, between them.

import datetime

def minutes(datetime1, datetime2):
    time_delta = datetime2 - datetime1 
    minutes = round(time_delta.total_seconds() / 60)
    return minutes



  
  ## Examples
# to_string(datetime_object) => "24 September 2012"
# from_string("09/24/12 18:30", "%m/%d/%y %H:%M") => datetime
import datetime 

def to_string(time):
    return time.strftime("%d %B %Y")    #takes a datetime and gives back a string in the format "24 September 2012".

def from_string(arg1, arg2):
    return datetime.datetime.strptime(arg1, arg2)
#takes two arguments: a date as a string and an strftime-compatible format string




import datetime
def time_tango(date, time):
    return datetime.datetime.combine(date, time)

#The two parameters date and time are not strings, they are date and time objects. 
#The package datetime actually has a method called combine, combine a date object with a time object (into a datetime object)
# datetime.combine(date, time)





#Write a function named delorean that takes an intege
#Return a datetime that is that many hours ahead from starter.

import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

def delorean(ahead):
    return starter.replace(hour=starter.hour+ahead)




# Write a function named time_machine that takes an integer and a string of "minutes", "hours", "days", or "years". 
# This describes a timedelta. Return a datetime that is the timedelta's duration from the starter datetime.
import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

# Remember, you can't set "years" on a timedelta! Consider a year to be 365 days.
## Example: time_machine(5, "minutes") => datetime(2015, 10, 21, 16, 34)

def time_machine(integer, string1):
  if string1 == 'hours':
      return starter + datetime.timedelta(hours=integer)
  elif string1 == 'days':
      return starter + datetime.timedelta(days=integer)
  elif string1 == 'minutes':
      return starter + datetime.timedelta(minutes=integer)
  elif string1 == 'years': 
      return starter + datetime.timedelta(days=integer*365)

time_machine(3, 'days')



# If you need help, look up datetime.datetime.fromtimestamp()
# Also, remember that you *will not* know how many timestamps are coming in
# Create a function named timestamp_oldest that takes any number of POSIX timestamp arguments. 
# Return the oldest one as a datetime object.

import datetime
import datetime

def timestamp_oldest(*args):
  return datetime.datetime.fromtimestamp(min(args))
