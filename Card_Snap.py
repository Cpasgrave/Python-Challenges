from random import shuffle
from re import findall
'''Answer to challenge proposed by D_Stark (explanations after code)'''
# https://www.sololearn.com/Discuss/1053866/card-snap-challenge

#you can choose to check only the first n cards, by giving this number here:
num = 0 # if you leave 0, it checks the whole deck

deck = [i for i in ['A','K','Q','J','10','9','8','7','6','5','4','3','2'] for j in range(4)]

def shuffle_and_check(deck,num=52):
    if num>52 or num<1: num = 52
    shuffle(deck)
    deck = '.'.join(deck[:num])
    print('your cards : ',deck,'\n',sep='')
    pattern = r'([^.]+).\1'
    matches = findall(pattern,deck)
    n = 0
    if matches:
        for m in matches:
            n += 1
            print('pair n.{}: {}'.format(n,m+'-'+m))
    else:
        print('no pair found')

shuffle_and_check(deck)

'''Hey
Shuffle 52 cards and run through the deck to find out how many snaps/pairs  there are in the deck as follows.
first 20 cards of a shuffled deck.
A,A,3,4,2,6,8,8,8,8,J,J,K,A,6,Q,Q,Q,A,4
running through the deck to find pairs in order.
snap 1 was AA
snap 2 was 88
snap 3 was 88
snap 4 was JJ
snap 5 was QQ
Challenge by D_Stark'''
