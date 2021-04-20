# timezone - datetime type that holds an offset from UTC and allows us to move a datetime around the world
# astimezone - method for converting an aware datetime to another timezone

import datetime
pacific = datetime.timezone(datetime.timedelta(hours=-8))
eastern = datetime.timezone(datetime.timedelta(hours=-5))
naive = datetime.datetime(2014, 4, 21, 9, 0)
aware = datetime.datetime(2014, 4, 21, 9, tzinfo=pacific)
 # datetime.datetime(2014, 4, 21, 9, 0, tzinfo=datetime.timezone(datetime.timedelta(-1, 57600)))
aware.astimezone(eastern)
 # datetime.datetime(2014, 4, 21, 12, 0, tzinfo=datetime.timezone(datetime.timedelta(-1, 68400)))
aukland = datetime.timezone(datetime.timedelta(hours=13))
aware.astimezone(aukland)
# datetime.datetime(2014, 4, 22, 6, 0, tzinfo=datetime.timezone(datetime.timedelta(0, 46800)))
mumbai = datetime.timezone(datetime.timedelta(hours=5, minutes = 30))
aware.astimezone(mumbai)
# datetime.datetime(2014, 4, 21, 22, 30, tzinfo=datetime.timezone(datetime.timedelta(0, 19800)))



#utc = pytz.utc  - utc = pytz.timezone('UTC') always start from utc in pytz
#.localize() - usually convert the original utc. take a naive datetime to an aware one. take a datetime to a certain time zone

import datetime
import pytz  #pip install pytz

pacific = pytz.time('US/Pacific')
eastern = pytz.time('US/Eastern')
format = '%Y-%m-%d %H:%M:%S %Z%z'
utc = pytz.utc 
start = pacific.localize(datetime.datetime(2014, 4, 21, 9)) 
start.strftime(fmt) # for formatting'2014-04-21 09:00:00 PDT-0700'
start_eastern = start.astimezone(eastern)
start_eastern # datetime.datetime(2014, 4, 21, 12, 0, tzinfo=<DstTzInfo 'US/Easterrn' EDT-1 day, 20:00:00 DST>)
start # datetime.datetime(2014, 4, 21, 9, 0, tzinfo=<DstTzInfo 'US/Pacific' PDT-1 day, 17:00:00 DST>)
start_utc = datetime.datetime(2014, 4, 21, 1, tzinfo = utc)
start_utc.strftime(fmt) #'2014-04-21 01:00:00 UTC+0000'
start_pacific = start_utc.astimezone(pacific)
start_pacific #datetime.datetime(2014, 4, 21, 9, 0, tzinfo=<DstTzInfo 'US/Pacific' PDT-1 day, 17:00:00 DST>)
auckland = pytz.timezone('Pacific/Aucland')
mumbai = pytz.timezone('Asia/Calcuta')
apollo_13_naive = datetime.datetime(1970, 4,  11, 14, 13)
apollo_13_eastern = eastern.localize(apllo_13_naive) # datetime.datetime(1970, 4,  11, 14, 13, tzinfo=<DstTzInfo 'US/Eastern' EST-1 day, 19:00:00 DST>)
apollo_13_utc = apollo_13_eastern.astimezone(utc)
apollo_13_utc.astimezone(pacific).strftime(fmt) # '1970-04-11 11:13:00 PST-0800'
apollo_13_utc.astimezone(auckland).strftime(fmt) # '1970-04-12 07:13:00 NZST+1200'

pytz.all_timezones #list all the timezone
pytz.country_timezones['us'] #put the name of the country inside the ['~']



#exercise

import datetime
#a variable named moscow that holds a datetime.timezone object at +4 hours
moscow = datetime.timezone(datetime.timedelta(hours=4))
# a timezone variable named pacific that holds a timezone at UTC-08:00.
pacific = datetime.timezone(datetime.timedelta(hours=-8))
# make a third variable named india that hold's a timezone at UTC+05:30.
india = datetime.timezone(datetime.timedelta(hours=5, minutes = 30))



#Make a new timezone that is UTC+01:00 and set it to a variable called tz.
#Create a new variable named paris that uses hill_valley and the astimezone() method to change hill_valley to the new timezone.
import datetime

naive = datetime.datetime(2015, 10, 21, 4, 29)
pacific = datetime.timezone(datetime.timedelta(hours=-8))
hill_valley = datetime.datetime(2015, 10, 21, 4, 29, tzinfo=pacific)

tz = datetime.timezone(datetime.timedelta(hours=1))
paris = hill_valley.astimezone(tz)



# starter is a naive datetime. Use pytz to make it a "US/Pacific" datetime instead
# ssign this converted datetime to the variable local.

import datetime
import pytz

fmt = '%m-%d %H:%M %Z%z'
starter = datetime.datetime(2015, 10, 21, 4, 29)

pacific = pytz.timezone('US/Pacific')
local = pacific.localize(starter)
pytz_string = local.strftime(fmt)
#create a variable named pytz_string by using strftime with the local datetime. Use the fmt string for the formatting.



# Create a function named to_timezone that takes a timezone name as a string. 
# Convert starter to that timezone using pytz's timezones and return the new datetime.

import datetime
import pytz

starter = pytz.utc.localize(datetime.datetime(2015, 10, 21, 23, 29))

def to_timezone(*arg):
    timezone = pytz.timezone(*arg)
    return starter.astimezone(timezone)




#question
.localize() -  What pytz method is used to convert a naive datetime to an aware one?

Create a timedelta that goes back 30 days.datetime.timedelta(days=-30)

The datetime methods .today() and .now() give back the same values by default.

UTC - What timezone should you try to always convert from?

timedeltas represent the difference between two points in time. Subtracting one datetime from another gives back what type of data?

