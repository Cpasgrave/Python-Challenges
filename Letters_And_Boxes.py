# Challenge proposed by D_Stark
# https://www.sololearn.com/Discuss/1052933/letters-boxes-challenge/
'''
🔡Letters & Boxes [Challenge]
The idea of this is like musical chairs 😂

You start off with say 5 letters and 5 boxes.

Each shuffle a box is removed forcing one letter to be nocked out of the game this repeats untill theres only one letter and 1 box left

Catch: Numbers are to be randomly shuffled around each time as follows

[a][b][c][d] < all letters have a box 

Shuffle 1,  --box

[c][d][b]    < "a" missed out and removed

Shuffle 2,  --box

[b][c]  <  "d" missed out

Shuffle 3, --box

[c]  < "b" missed out 

[c] < Won

Have fun ☺
'''

from random import randint, sample, choice
# initial number of chairs :
chairs = 8

players = [chr(i+97) for i in range(chairs)]
print(''.join(['['+i+']' for i in players]),'\n',sep='')
while len(players)>1:
    print("Dance around ... and ... sit !")
    out = players.pop(randint(0,len(players)-1))
    print(''.join(['['+i+']' for i in sample(players,len(players))]),' < '+out+' missed out','\n',sep='')
print(choice(['Monsieur','Madame']),players[0],'won this round !')
