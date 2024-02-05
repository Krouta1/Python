import time
#time and dates

#reference time
print(time.ctime(0)) #converts seconds since epoch to a string

print(time.time()) #returns the current time in seconds since epoch

print(time.ctime(time.time())) #current time in string format

print(time.localtime()) #returns the current time in a tuple format

formated_current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) #converts the time tuple to a string
print(formated_current_time)

print(time.strptime(formated_current_time, '%Y-%m-%d %H:%M:%S')) #converts the string to a time tuple