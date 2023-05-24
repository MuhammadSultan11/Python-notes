# Match Case Statements in Python - Python Tutorial - Day #16

# ============ match case with simle example=============
# x = int(input("Enter the value"))
# match x:
#      case 0:
#           print("x is zero:")
#      case 4 :
#           print("case is :")
#      case _:
#           print("defaulte value of x: ",x)

# ============= match case with if-condition=============

y = int(input('enter the value:'))

match y:
     case 0:
          print("y is zero:")
     case 4 :
          print("case is :")
     case _ if y != 80:
          print(y,"is not equal to 80.")
     case _ if y != 90:
         print(y, " is not equal to 90.")
     case _:
          print("defaulte value of x: ",y)


# ============== an other example =============
n = int(input('enter the value:'))

match n:
     case 0:
          print("n is zero:")
     case 4 :
          print("case is :")
     case _ if n == 80:
          print(n,"is equal to 80.")
     case _ if n == 90:
         print(n, " is equal to 90.")
     case _:
          print("defaulte value of n: ",n)


