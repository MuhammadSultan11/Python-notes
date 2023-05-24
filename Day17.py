# For Loops in Python | Python Tutorial - Day #17

# ==========The for Loop======
# for loops can iterate over a sequence of iterable objects in python.
# Iterating over a sequence is nothing but iterating over
#  strings, lists, tuples, sets and dictionaries.

# =============Simple For loop===============
print('Example: iterating over a string:')
name = 'SULTAN'
for i in name:
    print(i)#, end=", ")
    if (i == 'S'):
     # this line just for logic building.
        print("First letter of name is:", i)

# =============Simple For loop===============
print('\n', "An Other example of for loop with list:")
Brothers = ['Sultan', 'Musa', 'Iqbal', 'Urs', 'Adil']
for i in Brothers:
    print(i)
    if (i == "Sultan"):
        print('1st NO brother.')
    elif (i == 'Musa'):
        print('2nd NO brother.')
    elif (i == 'Iqbal'):
        print('3rd NO brother.')
    elif (i == 'Urs'):
        print('4th NO brother.')
    elif (i == 'Adil'):
        print('5th NO brother.')
    else:
        print("List is over.")

# =========== range() ===================
print('\n Here, we can use the range() function:')
for n in range(4):
    print(n)
    if (n == 3):
        print("Total Range is: ", n+1)

# =========================================
# Here, we can see that the loop starts from 0 by default and increments at each iteration.
# But we can also loop over a specific range.
for p in range(0, 1001):
    print(p, end=",")

#=======================================
# i want to print 5 from 1 not from 0.
print('\n I want to print 5 from 1: ')
for f in range(5):
    print(f+1)

# an other way to print 5 from 1.
print("\n an other way print 5 from 1:")
for e in range( 1,6):
    print(e)

#====================================
for r in range(0,10,2):
    print(r,end=",")

print("\n Quick Quiz: Explore about third parameter of range (ie range(x, y, z))?")



