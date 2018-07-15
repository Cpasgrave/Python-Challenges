# -*- coding: utf-8 -*-

"""
Challenge by Zephyr Koo https://www.sololearn.com/Profile/5654685/
Monday Blue Challenge Series #14
Let's play with alphabets this week! This time we will need to put alphabets onto the balance scale at 2 ends to achieve equilibrium.
If it's impossible to do so, determine the letter need to be added with minimum weight. The letters weight from 1 to 26 which corresponds to A to Z respectively.
TASK
Write a program to accept a string of uppercase letters and split into 2 groups which produce the minimum sum difference by using an underscore character "_".
If the sum difference is not ZERO, we will need to add a letter (surround it with round brackets) on either side to achieve equilibrium.

TEST CASE
"A" ➡ (A)_A or A_(A)
"AA" ➡ A_A
"AAA" ➡ A(A)_AA or AA_A(A)
"ABC" ➡ AB_C
"ABBA" ➡ AB_BA
"ABCD" ➡ ABC_D(B)
"ZEPHYRKOO" ➡ ZEPHY_RKOO(U)
"MONDAYBLUE" ➡ MONDA(R)_YBLUE
"CHRISTMAS" ➡ CHRIS_TMAS(D)
"IS" ➡ I(J)_S
"COMING" ➡ COM_ING(A)
"SOON" ➡ SO_ON(E)
BONUS
 Clear-cut and optimized approach is encouraged.
Happy Coding!!!
"""

# https://www.sololearn.com/Discuss/937081/m-challenge-alphabetical-balance-scale-%EF%B8%8F
test = ["A", "AA", "AAA", "ABC", "ABBA", "ABCD", "ZEPHYRKOO", "MONDAYBLUE", "CHRISTMAS", "IS", "COMING", "SOON", "AAAAAZ"]

def cut(word):
    n_list = [ord(c) - 64 for c in word]
    half = sum(n_list) / 2
    length = weight = 0
    for n in n_list:
        length += 1
        weight += n
        if weight == half:
            return word[:length] + "_" + word[length:]
        if weight > half:
            diff = weight - half
            diff_short = half - (weight-n)
            if diff <= diff_short:
                return word[:length] + "_" + word[length:] + "(" + chr(int(diff*2 + 64)) + ")"
            else:
                return word[:length-1] + "(" + chr(int(diff_short*2 + 64)) + ")" + "_" + word[length-1:]

for i in test:
    print (cut(i))
        
