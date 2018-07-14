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
# This was my first attempt to the challenge, not doing what was asked for,
# But the result was very interesting too.
# This code doesn't keep the order of the letters, it recombines them
# Doing so, it can reach some perfect balance without adjusting letters more often
# And it also gets situations with balancing with a 'smaller' letter
# But yes, in the end, id does not keep the order of letters.
# You can check my codes, I made a second code respecting the rules :)
from itertools import combinations as comb

test = ["GLYDPAK", "PLOUKHAZIEN", "A", "AA", "AAA", "ABC", "ABBA", "ABCD", "ZEPHYRKOO", "MONDAYBLUE", "CHRISTMAS", "IS", "COMING", "SOON", "AAAAAZ"]


def balance(inword):
    n_list = sorted([ord(c) - 64 for c in inword])
    l_list = sorted([c for c in inword])
    half = sum(n_list) / 2
    solution = [''] * (len(inword) + 1)
    combi = [''] * (len(inword))

    for i in range(len(inword)):
        combi[i] = list(comb(l_list, i))

    score = []
    for i in range(len(combi)):
        score.append([])
        for j in range(len(combi[i])):
            score[i].append([])
            tot = 0
            for k in range(len(combi[i][j])):
                tot += ord(combi[i][j][k]) - 64
            score[i][j] = half - tot
    x = []
    y = []
    for i in score:
        mini = min(abs(j) for j in i)
        x.append(mini)
        if mini in i:
            y.append(i.index(mini))
        else:
            y.append(i.index(-mini))

    diff = min(x)
    left = combi[x.index(min(x))][y[x.index(min(x))]]
    for i in range(len(left)):
        solution[i] = left[i]
    solution[len(left)] = "_"
    for i in left:
        l_list.remove(i)
    for i in range(len(l_list)):
        solution[len(left) + i + 1] = l_list[i]
    if diff != 0:
        adjust = "(" + chr(int(2 * diff) + 64) + ")"
    else:
        adjust = ""
    if sum(ord(i)-64 for i in left) < half:
        bal = adjust + "".join(solution)
    else:
        bal = "".join(solution) + adjust
    return bal

for i in test:
    print(i, (12-len(i))*"-" + ">", balance(i))
