# -*- coding: utf-8 -*-

#Rules:
# 1) You can  NOT use a built-in function, module or anything ready.
#
# 2) You can use just these operators:
# + - * / %
# (do not use power operation)
# 
# 3) You can use any language
#
# Challenge by SMhd Asadi

from math import sqrt

nums2 = [0.000000013, 0.00061, 0.005, 0.031, 0.118, 0.276, 0.343, 0.561, 0.784, 0.912, 0.992]
nums = [0, 0.0003, 0.5, 1, 1.00007, 1.3, 2, 3, 36, 17994564, 3719, 78954656321, 64564561231223, -5]
def squaroot(num):
    cy = 8
    if num == 0 or num == 1:
        return (num, "")
    if num < 0:
        c = squaroot(-num)[0]
        return (c, "x i")
    n = 0
    t = 0
    if num < 1:
        z = 10*num
        c = 1
        while z < 1:
            cy += 1
            c /= 10
            z *= 10
        n = (c+num)/2
    else :
        cy = 5
        while t < num:
            n += 1
            t = n * n
        n -= 1
    for x in range(cy):
        temp = num / n
        n = (n + temp) / 2
    return (n, "")

for i in nums + nums2:
    s = squaroot(i)[0]
    a = squaroot(i)[1]
    print("num = {}\n > square root = {}{}\n > check : diff with math sqrt = {}".format(i, "%.5f" % s, a, sqrt(abs(i))-s))

