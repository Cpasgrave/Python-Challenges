'''
Challenge: What about the Knight? by Vardanator

Given a chessboard you should determine how many squares can be attacked by a knight standing alone on the board in a given position.

Input contains two characters: the first character is a lowercase English letter from 'a' to 'h'; the second character is an integer from 1 to 8; they specify the rank and file of the square at which the knight is standing. For example, the knight presented in the image below stands at the position d3. 
Output should contain the number of the squares of the chessboard that are under attack by the knight.

For Example:
Input: g6
Output: 6

Input: a3
Output: 4
'''

p = input().lower()
a = (ord(p[0])-100.5)**2//6+(int(p[1])-4.5)**2//6
moves = 8-round(2*a-a**2/10)

print(moves)

#############
# One Liner #
#############

print((lambda a:8-round(2*a-a**2/10))(sum([(i-4.5)**2//6 for i in(lambda p:[ord(p[0])-96,int(p[1])])(input().lower())])))

#############
# Commented #
#############

# first input is taken and lowercased # in case someone would write 'G3'
p = input().lower()

# next, this input is changed into
# a list of coordinates.
# The letter is turned into an int
# thanks to ord()
# ord(p[0])-96 gives the difference
# with the character before 'a' in
# the Ascii table so that 'a' will
# return 1,b will return 2, and so on ...
# b7 as input will give us :
# [2, 7]
p = [ord(p[0])-96,int(p[1])]

# the idea here is to get the
# distance of the knight to the
# center of board in both directions:
# Because chessboard is 8x8, center
# in each direction is between lines # 4 and 5 (respectively 'd' and 'e')
# So we can have this distance by
# substracting 4.5 to the position
# value in each direction.
p = [i-4.5 for i in p]
# At this point,b7 after giving [2,7]
# now give [-2.5,2.5]
# My goal was to turn these distances
# into integers following this table:
# (first column is a reminder of the original coordinate value):
# 8  ->   3.5  ->  2
# 7  ->   2.5  ->  1
# 6  ->   1.5  ->  0
# 5  ->   0.5  ->  0
# 4  ->  -0.5  ->  0
# 3  ->  -1.5  ->  0
# 2  ->  -2.5  ->  1
# 1  ->  -3.5  ->  2

# 2 and 1 are integers that represent
# by how much the knight is close to a
# border. 2 is when he's right next to
# a border (big influence)
# 1 is one line away, the rest goes
# with 0 because it will have no
# influence on the knight's 
# possibilities.
# I just had to find a simple way
# to jump from column 2 to 3 of my
# table.
# x**2//6 does it !
p = [i**2//6 for i in p]
# now b7 as input became,
# successively :
# [2,7]
# [-2.5,2.5]
# [1,1]
# Next trick is to add those
# 'border influences'
# We'll get an integer representing
# the influence of the closest borders
# in both directions.
a = sum(p)
# with our b7 example, now we obtain 
# 2 as a global border influence on
# the knight.
 
# Only thing to do now is to transform
# our influences into attack
# possibilities for the knight.
# The table is as follows :
# 0  ->   8
# 1  ->   6
# 2  ->   4
# 3  ->   3
# 4  ->   2
# One simple way to get this done
# I found is :
# 8-round(2*x-x**2/10)
# in our example, 2 becomes 
# 8-round(4-0.4) --> 4
# This last operation may seem dirty,
# I actually enjoy dirty programming
# >:)  (e.g. as evolutionary
# algorithms are dirty)
moves = 8-round(2*a-a**2/10)

print(moves)
