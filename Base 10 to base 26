# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
# Challenge for Nerds!!!
# From - Jacob Pembleton
# Use C++ or Java to have an integer input (base 10) and convert it to base 26.
# For example, 28=bc, 25=z. Binary is 0’s and 1’s, meaning that it is base2.
# Base 26 means a=0, b=1, ... z=25 ba=26 and it is like 10.
# Comment links to your code.
# ----------------------------------------------------------------------------

# any base 10 positive integer can be given (b10)
b10 = 2334199994
n = 0;list = [];myint = b10

# finding the number of columns in base 26
while True:
    if b10 < 26**(n + 1): break
    n += 1
    
# producing a list with the number in base 26 to place in each column
while n >= 0:
    list.append(b10//26**n)
    b10 %= 26**n
    n -= 1
    
# transforming the numbers in the list to a string of letters
result = ''.join(chr(i+97) for i in list)
print(myint,"-->",result)

# I made the oneline reverse function, producing the base10 number
# corresponding to a given string of letters (only from the 26 basic latin)

b26 = "tryme"
print(b26,"-->",sum((ord(b26[::-1][i])-97)*26**i for i in range(len(b26))))
