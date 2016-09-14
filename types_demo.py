import time
import math

current_year = int(time.time() / (60 * 60 * 24 * 365)) + 1970

month = (time.time() / (60 * 60 * 24 * 365)) - int(time.time()/ (60 * 60 * 24 * 365)) 
current_month = int(12 * month)

day = month * 30 
day_converted = day - int(math.ceil((current_year-1970)/4))  #12 Leap years 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016
current_day = int(day_converted)

hour = (day_converted - int(day_converted)) * 24 
current_hour = int(hour)

