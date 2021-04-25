>>> import os
>>> os.path.exists('bootstrap')#True
>>> os.path.exists('bootstrap/js/npm.js')#True

>>> open('test_file.txt', 'a').close()  #open then exit

os.mkdir('templates')
os.makedirs('templates/layouts/mobiles')
os.makedirs('templates/layouts/mobiles', exist_ok=True)#if the directory exist, still move on


#exercise daily backup
#Create a function named create_daily_dir in backup.py. 
#This function should take a string which will be a date in either year-month-day (2012-12-22) or month-day-year (12-22-2012) format. 
#Use that to create a directory like 2012-12-22 (year-month-day) in the financial directory (which is in the current directory).
#This means that by calling create_daily_dir("04-22-2017"), we'd have a directory structure like financial/2017-04-22/.

import os
import datetime

def create_daily_dir(string, path='financial'):
    # try to decode date string to a datetime
    try:
        this_date = datetime.datetime.strptime( string, "%Y-%m-%d" ) #format type YYYY-mm-dd
    except:
        this_date = datetime.datetime.strptime( string, "%m-%d-%Y" ) #format type mm-dd-YYYY
    # convert back to the proper format    
    date_str = datetime.datetime.strftime(this_date, '%Y-%m-%d')
    os.makedirs(os.path.join(path, date_str))
    
    
    
import os

def create_daily_dir(string):
    if int(string.split("-")[2]) > 31:
        new_str = string.split("-")[2] + '-' + string.split("-")[0] + '-' + string.split("-")[1]
    else:
        new_str = string
    os.makedirs('financial/' + new_str, exist_ok=True)
