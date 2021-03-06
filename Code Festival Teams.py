# -*- coding: utf-8 -*-
from itertools import combinations as comb

# Teams of coders are coming to a CODE FESTIVAL:
# Challenge proposed by Cépagrave
# ---------------------------------
# Each team stays united, of course (unless in
# some of BONUS 1 solutions)
# A big final event is organised : a code
# battle between 2 guilds.
# You have been assigned to build those guilds.
# Each team is given a letter,
# according to the number of coders in it:
#
# "a" is a coder who came alone.
# "b" is a team of two
# ...
# "z" is a big team of 26 coders.
#
# "z" will be the max team size allowed.
# When the registrations are closed,
# you receive the list of teams :
# a string of letters. Like "adlskeajb"
# this one would be representing 8 teams,
# with respectively:
# 1, 4, 12, 19, 11, 5, 1, 10, 2
# coders in each team.
# You guessed it, the letter position
# in alphabet gives the number
# of coders in the team.
# ------ And your TASK is:----------
# To organise the 2 guilds.
# The conditions : to get the smaller
# possible difference of size between
# the 2 guilds. Equal sizes is optimal.
# If you get two or more solutions,
# you'll prefer the one with the smallest
# difference of number of teams for each side.
# If there still are more than one respecting
# this condition, they are equivalent.
# Nothing is organised if only one team.
# The code has to work for a string of
# two letters and more.
#
# The output will come this way:
# thankstozephyrkoo -----> (123) aehrttyz    /  hkknooops (124)
#
# BONUS 1:
# After the right distribution is chosen, 
# you can decide to split one team to balance
# the guilds. Show the result before and after
# the split. And show the modification separately.
# The final difference has to be 0 or 1.
#
# BONUS 2 (optimisation):
# For each language, you can challenge whoever 
# wrote another code with the same language. 
# The winner will be the challenger who 
# designs a code able to find a right solution
# (using SL code playground interpreter) with 
# the longest (random-like, not "aaaaaaaa" or so)
# string input.
# Share your inputs, and show your best results to
# challenge the other coders !
#
#
# BONUS 3:
# Hardcore version !!!:
# Same situation, but you're asked to build the 
# biggest number of balanced guilds. You must  
# check the distributions, with 2 to n-1 guilds
# where n is the total number of teams. 
# Your task is to find the solutions with the 
# smallest ratio :
# (biggest guild size - smallest guild size)/(smallest guild size)
# And if you have equal ratios for many solutions,
# you'll prefer the solution with a bigger number 
# of guilds.
#
# TEST CASES :
# ab
#-> (1) a /  b (2)
#
# gg
#-> (7) g  /  g (7)
#
# adlskeajb
#-> (32)  aaks / bdejl (33)
#
# codefestival
#-> (61)  acdlsv / eefiot (60)
#
# testcase
#-> (46)  aett / cess (46)
#
# thankstozephyrkoo
#-> (123) aehrttyz / hkknooops (124)
#
# aaaaaaz
#-> (26) z / aaaaaa (6)
#  >team z splits to: p+j
#  >(16) p / aaaaaaj (16)
#
# crazy
#-> (43) ry / acz (30)
#  >team y splits to: s+f
#  >(37) rs / aczf (36)
#
# what
#-> (24) aw / ht (28)
#  >team t splits to: r+b
#  >(26) awb / hr (26)
#
# venezuelanbeavercheese
# -> (111) aabceeesvvz/eeeeehlnnru (112)
#
# Enjoy coding it ! and don't forget to comment :)

testcases = ("venezuelanbeavercheese",)

def distribute(teams):
    
    #---------var settings---------
    # lt = list of teams (letters)
    lt = list(teams) ; lt.sort()
    # lts = list of team sizes
    lts = sorted(ord(i) - 96 for i in teams)
    # nt = number of teams
    nt = len(teams)
    # nc = number of coders (total)
    nc = sum(lts)
    h = int(nt / 2)
    # p = possible distributions for 1 guild
    p = []
    # s = score (evaluating the solution)
    s = []
    #-------------------------------
    
    # the for loop produces the (half) combinations array
    # p = possibilities, s = score for each entity of p
    # p and s are parallel arrays
    for i in range(1, h+1):
        p.insert(i-1, list(comb(lts, i)))
        s.insert(i-1, [abs(sum(j)-nc/2) for j in p[i-1]])

    # here starts the building of the answer
    # produces a list with the min value
    mini = [min(k) for k in s]
    # r for raw, c for column
    r = len(mini) - 1 - mini[::-1].index(min(mini))
    c = s[r].index(min(s[r]))
    # g1, g2 = guilds 1 and 2
    g1 = "".join([chr(i+96) for i in p[r][c]])
    for l in g1: lt.remove(l)
    g2 = "".join(lt)
    # ng1, ng2 = number of coders in each guild
    ng1 = sum(p[r][c])
    ng2 = nc - ng1
    
    answer = '{}\n-> ({}) {} / {} ({})'.format(teams, ng1,
g1, g2, ng2)
         
    print(answer)

    # starting BONUS 1
    d = abs(ng1 - ng2) # d = difference
    if d > 1:
        big = [g1, g2][[ng1, ng2].index(max(ng1, ng2))][-1]
        b1 = chr(ord(big) - int(d/2))
        b2 = chr(int(d/2)+96)
        if big in g1:
            g1b = g1.replace(big, b1)
            g2b = g2 + b2
            ng1b = ng1 - int(d/2)
            ng2b = ng2 + int(d/2)
        else:
            g1b = g1 + b2
            g2b = g2.replace(big, b1)
            ng1b = ng1 + int(d/2)
            ng2b = ng2 - int(d/2)
        modif = '  >team {} splits to: {}+{} '.format(big, b1, b2)
        new = '  >({}) {} / {} ({})'.format(ng1b, g1b, g2b, ng2b)
         
        print(modif + '\n' + new)
        
for w in testcases:
    distribute(w)
