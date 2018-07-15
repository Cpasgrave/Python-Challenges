# -*- coding: utf-8 -*-

# Given values and treir fixed probability of return.
# 10 => 60%,
# 20 => 20%,
# 30 => 10%,
# 40 => 5%,
# 50 => 1%,
# 60 => 1%,
# 70 => 1%,
# 80 => 1%,
# 90 => 0.5%,
# 100 => 0.5%

# So, probability of returning 10 is 60%,
# probability of returning 20 is 20%,
# probability of returning 30 is 10% and so on.

# Task:
# Generate a random value depending on its fixed probability of return.

# You can use separate arrays for values and their fixed probabilities 
# or an associative array for both, it doesn't matter.
# Here's my OOP version.
# https://code.sololearn.com/wP4NJk0sdIK0/?ref=app

import random
# My answer to CHALLENGE : Custom Randomizer (details at the end of code)
# proposed by Igor Makarsky  

def ratatandom():
    rates = [1, 2, 4, 6, 8, 10, 20, 40, 80, 200]
    r = random.randint(1, 200)
    for n in range(10):
        if r <= rates[n]:
            return 10*(10-n)

# Checking if the function gives the right distribution :
values = [10*x for x in range(1, 11)]
hits = [0]*10
for i in range(10000):
    r = ratatandom()
    hits[values.index(r)] += 1
for v in range(10):
    print(values[v], (3 - len(str(values[v])))*" "+"--> ", hits[v]/100, "%")
