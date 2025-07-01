# importing the module 
from datetime import date 

# storing today's date in a variable 
today = date.today() 

# Printing the variable 
print(f"Today's date: {today}")  
from datetime import date 
today = date.today() 

# to print the present year 
print(f"Present Year:{today.year}") 

# to print the present month 
print(f"Present Month:{today.month}") 

# to print the present date 
print(f"Present Date:{today.day}") 

# By using now(), We will get both current  
# date and time Storing current time and 
# date into a variable 
from datetime import datetime 
today = datetime.now() 

# Storing the date and time you want to calculate 
# In this you have to give the time as the input 
graduation_day = datetime(2023, 8, 11, 0, 0, 0) 

# finding the difference from 
days_left = abs(graduation_day - today) 

# Displaying the no.of.days left with time 
print(f"Time left till the graduation: {days_left}") 

import time 
time.time()
from datetime import date, time, datetime 
date(year=2020, month=1, day=31) 
date.today() 
datetime.now()

import time; 

localtime = time.asctime( time.localtime(time.time()) ) 
print ("Local current time :", localtime)

import calendar 
cal = calendar.month(2008, 1) 
print ("Here is the calendar:" )
print (cal) 

# importing sqrt() and factorial from the 
# module math 

from math import sqrt, factorial 

# if we simply do "import math", then 
# math.sqrt(16) and math.factorial() 
# are required. 

print(sqrt(16)) 
print(factorial(6)) 

# importing sys module 

#For system commands 
import sys 
# importing sys.path 
print(sys.path) 
print(sys.version) 

# importing sqrt() and factorial from the 
# module math 

import math as mm 

# if we simply do "import math", then 
# math.sqrt(16) and math.factorial() 
# are required. 
print(mm.sqrt(16)) 
print(mm.factorial(6)) 

import random
print(dir(random)) 

#importing built in module math
import math

# doing sqrt
print(math.sqrt(25))

#using pi
print(math.pi)

print(math.degrees(2))
print(math.radians(60))

print(math.sin(2))
print(math.cos(0.5))
print(math.tan(0.23))

#factorial
print(math.factorial(4))

# importing built in module random 
import random 

# printing random integer between 0 and 5 
print(random.randint(0, 5))

# print random floating point number between 0 and 1 
print(random.random())

# random number between 0 and 100 
print(random.random() * 100)
List = [1, 4, True, 800, "python", 27, "hello"]
 
# using choice function in random module for choosing  
# a random element from a set such as a list 
print(random.choice(List))

#importing built in module datetime
import datetime
from datetime import date
import time

#returns seconds since unix epoch - january 1, 1970
print(time.time())

#converts a number of seconds to a date object 
print(date.fromtimestamp(454554)) 

import time
start = time.time()

for i in range(1000000):
    pass
end = time.time()
print('elapsed time is {}'.format(end-start))

