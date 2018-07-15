# Challenge :
# Mike's Challenge Series #1
# https://www.sololearn.com/Discuss/805779/mike-s-challenge-series-1

"""
Question:
A network tower has a range of 0.35 miles, and is located 1.75 miles from your WIFI access point which has a range of 0.02 miles.
Display the area of positions you can access both your WIFI and Network signals in metres.

HINT: ()
"""

# d = distance from tower to wifi
# tr = tower's range
# wr = wifi range

import math

d = 1.75
tr = 1.35
wr = 1.0

if tr+wr<d :
    print("There is no overlapping area of the signals,\nyour wifi and the tower are just too far from each other !\n---)--(---")
else :
    h=((tr+wr)-d)/2
    Ax=(tr*tr)*math.acos((tr-h)/tr)-(tr-h)*math.sqrt((2*tr*h)-(h*h))
    Az=(wr*wr)*math.acos((wr-h)/wr)-(wr-h)*math.sqrt((2*wr*h)-(h*h))
    A=Ax+Az
    print("Area available is...") 
    print(str(round(A,3))+' square miles')
    print("And in metres")
    Area=A*1609.344
    print(str(round(Area,1))+' square meters')
