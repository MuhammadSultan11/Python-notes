# String Methods in Python | Python Tutorial - Day #13

print("find length on string")
book = 'hyperfocus'
print("Length is :", len(book))
print('=============upper() Method1=================')

print('convert lower case string to upper case')
book1 = "philosophy!!!!!!!"
print('philosophy converted to upper case = ',book1.upper()) # this method convert to upper case letters.

print('===========lower() Method2===================')

print('convert upper case string to lower case')
book1 = "PHILOSOPHY!!!!!!"
print('PHILOSOPHY converted to upper case = ',book1.lower()) # this method convert to lower case letters.

print('==========rstrip() Method3===============')

# rstrip can't remove leading characters but it can remove trailing characters. 
# Exp: (leading characters comes before words=> !!!!!!!maths!!!!!!! <=trailing characters comes after  words.)
print('the rstrip() removes any trailing character')
book2 = '!!!maths!!!!!!' # these are trailing character => !!!!!!!.
print('removes trailing character:', book2.rstrip('!') )
print(book2.replace("maths", "mathematics"))

print('==========replace() Method4===============')
print('the replace() method removes current string with an other string')
name = "sultan"
print("replace method will cahange sultan to Mr. Muhammad Sultan ")
print(name.replace("sultan", " Mr. Muhammad Sultan"))
print('==========replace() Method5===============')
name1 = "sultan!!! sultan!!! is comming!!!! sultan" # all sultan replace with Mr. Muhammad Sultan
print(name1.replace('sultan', 'Mr. Muhammad Sultan'))

print('==========split() Method6===============')
print("split method convert string values into a list and seprate with comnna")
splitmethod = 'hello !!!!!! sultan How are you !!!! here !!!??? '
print(splitmethod.split(" "))

print('==========capitalize() Method7===============')
# capitalize method convert 1st word of 1st letter in capital letter, 
# but without 1st letter all letter convert in lower case.
blogHeading = "introduction to technology" # inroduction => Introduction to technolgy
print(blogHeading.capitalize())
print("another example: ")
BlogHeading = 'inTroducTion tO teCHnoLogY'# answer is Introduction to technology.
print(BlogHeading.capitalize())

print('==========center() Method8===============')
# center method aligns the string at center
string1 = 'wellcom to the console!!!'
print( string1.center(10))
print("length of string1: ",len(string1))
print("length of string1.center: ", len(string1.center(50)))

print('==========count() Method09===============')
# count() Method returns a string value how many times occurred in string values.
Name = "sultan!!! sultan!!! is comming!!!! sultan sultan sultan sultan"
 # here we count how many times sultan written in string values.
print("sultan name written ",Name.count('sultan'),"times.")
print("Other example:")
str2 = "Abracadabra"
print("a letter written ",str2.count('a'),"times.")
#=====OR================
countStr = str2.count("a")
print("a letter written ",countStr,"times.")

print('==========endswith() Method10===============')
#The endswith() method checks if the string ends with a given value. 
# If yes then return True, else return False.
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
print('Another example')
#We can even also check for a value in-between the string by providing start and end index positions.
str1 = "Welcome to the Console !!!"
print(str1.endswith("to",3,10))

print('==========Find() Method11===============')
# The find() method searches for the first occurrence of the given value 
# and returns the index where it is present. 
# If given value is absent from the string then return -1.
str1 = "Welcome to the Console !!!"
root = str1.find("to") # to is occurres at 8th index.
print("'to' is occurre at ",root,"index")
# If i want to fined too?
print(str1.find("too")) # It will return -1 because too is not occurres at all over sentence or index.

str2 = "He's name is Dan. He is an honest man." # here 2 'is' but we take 1st 'is' because it comes 1st. 
print("'is' occurre at ",str2.find("is"),"index")

print('==========index() Method12===============')
#The index() method searches for the first occurrence of the given value and returns the index where it is present.
#  If given value is absent from the string then raise an exception.

# If you search some value and that is not in your string values. 
# so here you want to compiler give you an error not -1 thats why we use endex() method.
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))

# As we can see, this method is somewhat similar to the find() method. The major difference being
# that index() raises an exception if value is absent whereas find() does not.
str1 = "He's name is Dan. Dan is an honest man."
# print(str1.index("Daniel"))

print('==========isalnum() Method13===============')
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9.
# If any other characters or punctuations are present, then it returns False.
method13 = "WellcomeToTheConsole420"# true because this string value written with A-Z, a-z, 0-9 alphabets and numbers.
Method13 = "<!@#$%^&*>" # False because this string value written with spacial characters.
print(method13.isalnum())
print(Method13.isalnum())

print('==========isalpha() Method14===============')
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z.
# If any other characters or punctuations or numbers(0-9) are present, then it returns False.
method14 = "WellcomeToTheConsole" # True
Method14 = 'hi! this sultan 100%' # False
print(method14.isalpha())
print(Method14.isalpha())

print('==========islower() Method15===============')
# The islower() method returns True if all the characters in the string are lower case, else it returns False.
method15 = "hello sultan"  # True
print(method15.islower())
Method15 = 'hello SULTAN!' # Fales
print(Method15.islower())

print('==========ispritnable() Method16===============')
#The isprintable() method returns True if all the values within the given string are printable, 
# if not, then return False. like: \n , etc
printable = "Happy Birthday sultan! I am happy for you 100... time "
print(printable.isprintable()) # True
printable1 = "Happy Birthday sultan! I am happy for you 100... time\n "
print(printable1.isprintable()) #false

print('==========isspace() Method17===============')
# The isspace() method returns True only and only if the string contains white spaces, else returns False.
space = "     " # white space
print(space.isspace()) # True
space1 = " hi " # False because you write hi but rule is white spase and no letter or number
print(space1.isspace())

print('==========istitle() Method18===============')
# The istitile() returns True only if the first letter of each word of the string is capitalized,
# else it returns False.
title = " Hello Sultan!"
print(title.istitle()) # True B/C eact string word 1st letter is capital.
title1 = " hello sultan!"
print(title1.istitle())# False B/C eact string word 1st letter is small.

print('==========isupper() Method19===============')
# The isupper() method returns True if all the characters in the string are upper case, 
# else it returns False.
upper = "HELLO SULTAN"
print(upper.isupper()) # True
upper1 = "hello sultan"
print(upper1.isupper()) # False

print('=============startswith() Method20===============')
# The startswith() method similar endswith() method checks if the string starts with a given value. If yes then return True,
#  else return False.
start = "python is good for you sultan"
print(start.startswith("python")) # true b/c python word is in starting of sentence.
start1 = "Hey, sultan python is good for you"
print(start1.startswith("python")) # false b/c python word is not in starting of sentence.

print('=============endswith() Method21===============')
print(start1.endswith("you")) # oppesite to startswith() method.

print('=============swapcase() Method22===============')
# The swapcase() method changes the character casing of the string. 
# Upper case are converted to lower case and lower case to upper case.
swap = " hello sultan"
print(swap.swapcase())  # answer is: HELLO SULTAN.
swap1 = " HELLO SULTAN"
print(swap1.swapcase()) # answer is: hello sultan.
swap2 = " HELLO sultan"
print(swap2.swapcase()) # answer is: hello SULTAN.

print('=============title() Method23===============')
#The title() method capitalizes each letter of the word within the string.
Title = ' hello sultan '
print(Title.title())
print("an other example:")
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())
print('=============title() Method24===============')








