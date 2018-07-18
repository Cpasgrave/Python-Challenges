''' 
This code answers the challenge : Fun with Digits by James Flanders
Given the digits 123456789, you can insert the + or - signs anywhere between them, without changing the order of the digits.
Challenge: Write a program to find all possible variations, which result in 100.
Sample solution: 1 + 2 + 3 - 4 + 5 + 6 + 78 + 9 = 100'''
######################################################
operators = ['+','-']

target = 100

lines = ["1"]
for i in range(2,10):
  for j in range(len(lines)):
    for op in operators:
            lines.append(lines[j]+op+str(i))
    lines[j] += str(i)
for line in lines:
  if eval(line) == target:
    print(line,'=',target)
######################################################
# One liner Version
######################################################
from itertools import product as p

[print(k,"= 100") for k in [''.join([''.join([str(j+1)+i[j]]) for j in range(8)])+'9' for i in  p(['','+','-'], repeat=8)]if eval(k)==100]
######################################################
# One liner with 3 operators
######################################################
[print(k,"= 100") for k in [''.join([''.join([str(j+1)+i[j]]) for j in range(8)])+'9' for i in  p(['','+','-','*'], repeat=8)]if eval(k)==100]

######################################################
# Commented Version
######################################################
operators = ['+','-']

target = 100

# the first part of the code creates all the possible strings
# respecting the assignment rules, in a list called lines:
# ['123456789', '1+23456789', '1-23456789', '12+3456789', '12-3456789'
# ...
# '1+2+3+4+5+6+7+8+9', '1+2+3+4+5+6+7+8-9']
# It works by lenghtening the original ["1"]
# At every loop, it will add the new number from range(2,10)
# to each existing string,
# and add two new strings made of the original one + one of 
# the operators + the new number.
# the first steps will be :
# ["1"]
# ["12","1+2","1-2"]
# ["123","12+3","12-3","1+23","1+2+3","1+2-3","1-23","1-2+3","1-2-3"]
# etc ...

lines = ["1"]
for i in range(2,10):
  for j in range(len(lines)):
    for op in operators:
            lines.append(lines[j]+op+str(i))
    lines[j] += str(i)

# The second part loops threw the previously created list (lines)
# the eval() function has the effect to 'run' a string
# as if it was python code, and returns the result.
# So here, it calculates each line and returns the result.
# Easy then is to just check if this result is 100 (target)
# and to print it only in this case.
for line in lines:
  if eval(line) == target:
    print(line,'=',target)
