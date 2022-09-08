import time

print(time.ctime()) # convert a time expressed in seconds since epoch a readable string
#   epoch: when your computer thinks time began (reference point)
print(time.ctime(0))

print(time.time())
print(time.ctime(time.time()))  # same time.ctime()

time_object = time.localtime()
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)
print(time.gmtime())


time_string = "20 April, 2020"
time_object2 = time.strptime(time_string, "%d %B, %Y")
print(time_object2)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

time_string2 = time.mktime(time_tuple)
print(time_string2)  # second since epoch a