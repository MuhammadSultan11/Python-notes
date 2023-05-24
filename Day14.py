# If Else Conditional Statements in Python | Python Tutorial - Day #14

# Sometimes the programmer needs to check the evaluation of certain expression(s), 
# whether the expression(s) evaluate to True or False. If the expression evaluates to False, 
# then the program execution follows a different path than it would have if the expression had evaluated to True.

# if
# if-else
# if-else-elif
# nested if-else-elif.
# Conditional Operators: [>, <, <=, >=, ==, != ]

# print("============If-else=============")
# age = int(input("Enter your age: "))
# print('Your age is: ', age)
# if(age>18):
#     print('Yes, You can drive.') # True
# else:
#     print("No, You can't drive.") # False
# # examples
# print(age<18)
# print(age<=18)
# print(age>=18)
# print(age!=18)

# print("anothe example")
# budget = int (input('Enter your budget:'))
# applesPrice = 220
# if(applesPrice<=budget):
#     print('Yes, You can buy 1kg of apples.')
# else:
#     print('No, you can not buy 1kg apples because 1kg of apples is = ',applesPrice,'but your budget is =',budget)


# print("============If-elif-else=============")
# num = int(input("Enter your number:"))
# if(num<0):
#     print("Number is Negetive:",num)
# elif(num==0):
#     print('Number is Zero:',num)
# else:
#     print("Number is Positive:",num)

print("============Nested-If-Statment=============")
number = int(input('Enter your number: '))

if(number < 0):
    print('number is negative:',number)
elif(number > 0):
    if(number <= 10):
        print('number is between 1 to 10: ',number)
    elif(number > 10 and number <= 20):
        print('number is between in 11 to 20: ', number)
    else:
        print('number is greater than 20: ',number)
else:
    print('number is zero:', number)
