print(46 + 37 + 38)
print(2016-1996)
print(15/3)
print(2**6)

#Exercise 2 below

#1
print('Number 1')
minute = 60 #seconds
print((minute * 42) + 42)
total_seconds = (minute * 42) + 42
total_minutes = 42 + (42/60)
total_hours = (total_minutes/60)

#2
print('Number 2')
mile = 1.61 #km
print(10/mile)
miles=(10/mile)

#3
print('Number 3')
print(total_seconds/miles)
print(total_minutes/miles)
print(miles/total_hours) 

#---------------------------
#Session 2
#Number 1
import math
r = 5
sphere_volume = math.pi*(4/3)*r**3
print('The volume of the sphere is:', sphere_volume)

#Number 2
cover_price = 24.95 
bookstore_price = (1-0.4) * cover_price
shipping = 3
number_of_books = 60 
costs_for_more_books = 0.75 * number_of_books

print('The Total Cost is:', '$', bookstore_price + shipping + costs_for_more_books)

#Number 3

first_and_third_speed = 8 + 15/60 #minutes 
first_and_third_run = 2 * first_and_third_speed #minutes 

second_speed = 7 + 12/60 #minutes 
second_run = 3 * second_speed #minutes 

total_time_minutes = first_and_third_run + second_run #minutes 

#but we still need to get rid of the decimal places after the whole numbers to get seconds 

total_time_seconds = total_time_minutes - int(total_time_minutes)

minutes_from_run = int(total_time_minutes)           #Minutes from Run 
seconds_from_run = round(total_time_seconds * 60 ,2) #Seconds from Run 

total_time_from_run_in_seconds = minutes_from_run * 60 + seconds_from_run

#convert current time to seconds 
current_hour = 6
current_minutes = 52 
current_time_in_seconds = current_hour * 60 * 60 + current_minutes * 60

new_total_time = total_time_from_run_in_seconds + current_time_in_seconds

#get the hour from the new time  
new_total_time_hour = new_total_time / 60 / 60 
new_hour = int(new_total_time_hour)

#get the minutes from the new time
new_total_time_minutes = new_total_time_hour - int(new_total_time_hour)
new_minutes = new_total_time_minutes * 60 
new_minute = int(new_total_time_minutes * 60)

#get the seconds from the new time
new_total_time_seconds = new_minutes - int(new_minutes)
new_second = int(new_total_time_seconds * 60)

print(new_hour,'HR :',new_minute,'Min :',new_second,'Secs')
print('%.0f' % new_hour,':', '%.0f' % new_minute,':', '%.0f' % new_second)

#4 
first_grade = 82
last_grade = 89

percentage_increase = (89-82)/82 
print(round(percentage_increase*100,1),"%",'Increase')