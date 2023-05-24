# Exercise 2 :  (solving) say to user Good Morning Sir according to time | Python Tutorial - Day #15

# this code is from harry for learning.
import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
# "Here is a sample program and documentation link for you:
# https://docs.python.org/3/library/time.html#time.strftime"


# Question: Create a python program capable of greeting you with Good Morning,
# Good Afternoon and Good Evening. Your program should use time module to get the current hour.
# 4:00am to  11:59:59am Morning
# 12:00pm to 16:59:59pm afternoon
# 17:00pm to 18:59:59pm  evening
# 19:00pm to 3:59:59  Night


name = input("Enter your name: ")
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
print(hour)
if (4<= hour and hour <= 11 ):
    print(" good morning ",name)
elif(12 >= hour <= 16):
    print("good afternoon", name)
elif(17 >= hour <= 18):
    print('good evening', name)
else:
    print('good night', name) 


