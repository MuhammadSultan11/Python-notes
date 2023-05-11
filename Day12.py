# Strings Slicing and Operations on Strings in Python | Python Tutorial - Day #12.

# I want to print first 6 string values whit help of counting index.
print("Strings Slicing: \nHere i print only sultan and hassan not comna that is wetween them.")
name = "sultan,hassan"  # here is 13 index.
print(name[0:5])      # it will print sultan name from S to N.
print(name[7:13])     # it will print hassan name from H to N.
print("===========================================")

# ===============================================================
# Length of a String.
print("Length of a String...")
name1 = 'SULTAN'      # string values
print(" Sultan have ", len(name1), ' letters.')
print("===========================================")

# ===============================================================
bookName = 'hyperfocus'
print('Total length: ', len(bookName))   # answer 10 (length).
print('A. spacific index: ', bookName[0:5])  # answer hyper. # including 0 but not 5
print('B. spacific index: ', bookName[5:10])  # answer focus.# including 5 but not 10
print('C. spacific index: ', bookName[2:7])  # answer perfo. # including 2 but not 7
# negative slicing...
print('D. spacific index: ', bookName[-2:-4]) # answer is nothing. #[8:6] 1st degit smaller and 2nd bigger after you get an answer like [6:8].
print('F. spacific index: ', bookName[-4:-2]) # answer is oc.
print('G. spacific index: ', bookName[-2:len(bookName)-1]) # answer is u.

# ======================================
print('Quick Quiz')
nm = 'HARRY'
print('spacific index:', nm[-4:len(nm)-2]) # answer AR
