# -*- coding: utf-8 -*-
from itertools import *

# This is my anser to the challenge from Chintalacheruvu Sravanth Kumar :
# https://www.sololearn.com/Discuss/1005502/challenge-coding-problem/
'''
Challenge # coding problem #
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 12, 1, 11, 2, 11, 1, 22, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.'''
# This challenge has also been proposed here before, by Gaurav Agrawal:
# https://www.sololearn.com/Discuss/853148/assignment-a-man-on-stairs-of-n-steps
'''
A man can jump 1 or 2 steps at a time , find number of ways in which the man can climb  n  number of steps  ?

/*
example :::   input :: 3
                      output :: 3    // because 3 ways 
 1st way) 3 times 1 step (1,1,1)
 2nd way)1 time 2 steps together & then 1 step more(2,1)
 3rd way) 1 step & then 1 time 2 steps together(1,2)
 Remember man can take 1 or 2 steps at a time
*/

//level :: easy & interesting 
//simple approach is welcome , with some explanation

HAPPY CODING ☺👍
'''

# First come the settings : You can play with them. 
# N should not be too big, values in X must be positive integers, indefinite number of values inside X

N=31
X={1,3,5,7}

# defining factorial cause I'll need it later
def fact(x):
    if x<2: return 1
    else: return x*fact(x-1)

# variables definition
Y=[] ; C=[] ; sol=0

# producing P
# P is the list of different combinations that can be used to climb N :
for n in X:
    Y+=(N//n)*[n]
for j in range(len(Y)):
    for co in (combinations_with_replacement(X,j+1)):
        if sum(co) == N:
            C+=[co]
            
# Then because in many situations there are too many possible permutations, I just calculate the number of permutations here for each combination from P, then make a total (sol)
# The math formula is n!/a!b!c!d! if there are 4 repeated elements in the combination, where a is the number of repetitions for the first element and so on ...
for co in C:
    repeated=[] ; A=1
    for i in X:
        repeated+=[co.count(i)]
    for i in repeated:
        A*=fact(i)
    arr=fact(len(co))/A
    sol+=arr
    print("".join([str(i) for i in co]), "->", int(arr), "perm")

print("\nTo climb a staircase with", N, "steps, \nBy jumping one of these hights :", X, "at a time,\n there are", int(sol), "different ways to climb it")
