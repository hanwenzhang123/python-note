dir(datetime)
#common ones here
date
time
datetime
timedelta
timezone

#datetime - Only days, seconds and microseconds are stored internally. 
# A millisecond is converted to 1000 microseconds.
# A minute is converted to 60 seconds.
# An hour is converted to 3600 seconds.
# A week is converted to 7 days.

# Always! # import the datetime library
import datetime 

datetime.datetime.now()

treehouse_start = datetime.datetime.now()
treehouse_start = treehouse_start.replace(hour = 9, minute = 0, second = 0, microsecond = 0)

datetime.datetime.now() - treehouse_start # how long has been treehouse

time_worked = datetime.datetime.now() - treehouse_start

hours_worked = round(time_worked.seconds/3600)




# timedelta - a duration of time, represent gaps in time. 
class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# They are returned when you subtract one datetime from another. 
# They can also be assigned to a variable and then used to augment datetime objects.
now = datetime.datetime.now()
datetime.timedelta(hours = 3) #datetime.timedelta(0, 18000)
datetime.timedelta(days = 3) #datetime.timedelta(3)
now + datetime.timedelta(days = 3) # 3days from now
now + datetime.timedelta(days = -5) # 5days ago
now - now + datetime.timedelta(days = 5)

now.date() # get date
now.time() # get time

hour = datetime.timedelta(hours = 1) #datatime.timedelta(0, 3600) second
workday = hour * 9
tomorrow = datetime.datetime.now().replace(hour=9, minute=0) + datetime.timedelta(days=1)
tomorrow + workday  #check what time getting off work tomorrow

appointment = datetime.timedelta(minutes = 45)  #meeting block
start = datetime.datetime()
end = start + appointmenet



#today and tomorrow
now = datetime.datetime.now()
today = datetime.datetime.today()

today = datetime.datetime.combine(datetime.date.today(), datetime.time()) # (2021, 04, 17, 0 0)
today.month #4
today.hour  #0
today.year  #2021
now.hour    #12
today.weekday() #6 start from Monday, today is Saturday
now.timestamp()




# Dating methoods
# strftime - string from time, string formatted time.Method to create a string from a datetime, takes a datetime and gives back a string in the format
# strptime - string parse into time. Method to create a datetime from a string according to a format string

import datetime 
now = datetime.datetime.now()
now.strftime('%B %d')
now.strftime('%m/%d/%y')    # US standard datetime format

birthday = datetime.datime.strptime('2015-04-21', '%Y-%m-%d') # datatime.datetime(2021, 4, 17, 0, 0) time not specified.
birthday_party = datetime.datime.strptime('2015-04-21 12:00', '%Y-%m-%d %H:%M')



