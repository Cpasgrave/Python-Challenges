'''My answer to the challenge proposed by Pedro Demingos : [Challenge] Normal Distribution
https://www.sololearn.com/Discuss/1048207/challenge-normal-distribution
description after the code
'''
from numpy import sum, random as r
from collections import Counter

# Number of games :
N = 2317

# Number of dices rolled/game
n = 7

g= r.random_integers(6,size=(N, n))
sums= [sum(g[i]) for i in range(len(g))]
tab= Counter(sums)
m= max(tab.values())

print('\n'.join(['{0: >2} '.format(t)+((int(tab[t]*30/m)*chr(219)+' '+str(tab[t])) if t in tab else'')for t in range(n,6*n+1)]))

'''
> Make a game that rolls a dice n times and returns the MEAN result value. 
> Play that game N times and keep track of the returns you're getting. 
> Show the result somehow. 

The distribution of results will be within [1, 6] and should look like a normal distribution around 3.5 (due to the central limit theorem -- see Wikipedia for that). 

I made a python code using the toss of a coin, so it goes from 0 to 1:
PC: https://code.sololearn.com/cLVOcQU9LqiV/#py
Phone: https://code.sololearn.com/cKhrPsZBgD2H/#py
These are my first ones in SoloLearn, so I also accept critics on them. 

You don't need to do it in python. 

Happy coding.

Pedro Demingos'''
