# Strings in Python | Python Tutorial - Day #11

# Simple Single line string.
# print("Simple Single line string...\n")
# a = " sultan "
# b = ' best   '
# print( ' Hey, this ', a, 'and I am the', b)

# ===============================================
# Multiline string.
# print("Multiline string...\n")
# Multiline = """ My name is sultan and I am the best in python programming 
#         I will creat many modules in Machine learning, It work in best case.
#         After many research I created these modules."""
# print(a)

# ===============================================
# Accessing Characters of String [ with index]
print( ' Accessing Characters of String...\n')
name = "SULTAN " # here 6 index as letters of sultan name and 7th index is space.
print( name )
print( name[0])
print( name[1])
print( name[2])
print( name[3])
print( name[4])
print( name[5])
print( name[6]) # on this has a space and that will be counted as an index.
# print( name[7]) # and if you find 8th index it will give an error.

# ===================================================
# looping through the string.
# {If you have multiline string so there is 100 or 1000 index therefor we using loop with strings}
print( 'looping through the string...\n')
multiline = ''' I am good I am best,
               And I am bad I am worst.'''
for character in multiline:
    print(character)






