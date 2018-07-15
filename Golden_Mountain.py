# -*- coding: utf-8 -*-

'''
   Challenge: 'The Golden Mountain'

At one international Olympiad in Informatics, the following task was given.
Let's solve it!

        7
      3  8
    8  1  0
  2  7  4  4
4  5  2  6  5

The figure shows an example of a triangle of numbers. 
Write a program that calculates the largest sum of numbers through which the path starts, starting at the top and ending somewhere on the bottom.
Each step can go diagonally down to the right or diagonally to the left.

In the example - this is the path 7➡3➡8➡7➡5,
given a max amount of 30.


         by rudolph flash

'''

from random import choice

# this code is better suited to watch with computers than phones.

# P(n, m, M) will produce a random pyramid,
# n being its height,
# m = min value M = max value :

P = lambda n,m,M:[[choice(range(m, M+1))for j in range(i)]for i in range(1,n+1)]

# You can tune the settings here (first height, then min and max values):

pyramid = P(1000,-999,999)

# V(p) prints the pyramid with a readable form:

V=lambda p:[[print("{}{}".format("  "*(len(p)-len(r)),''.join([str(c)+(" "*(5-len(str(c))))for c in r])))]for r in p]

# solve function returns max path
# and a solved pyramid

def solve(p):
    t=[p[-1]] ; s = [] ; k = 0
    # Here it makes a new pyramid, adding each local value
    # with the max from both values under it
    for r in range(-1,-len(p),-1):
        t.insert(0,[max(i,j)+k for i, j, k in zip(t[r], t[r][1:], p[r-1])])
    # extracting total (max path) to be able to return it
    tot = t[0][0]
    # here, replacing all the values not in the path with "-" 
    # and bringing back path valules from the original
    # (not summed) pyramid
    for g in range(len(p)):
        t[g] = [" - " for i in t[g][:k]]+[p[g][k]]+[" - " for i in t[g][k+1:]]
        if g != len(p)-1:
            if t[g+1][k] < t[g+1][k+1]: k += 1
    return t, tot

# applying :
# V(pyramid)
solution = solve(pyramid)
print(" ")
# V(solution[0])
print(" ")
print("max path :", solution[1])
