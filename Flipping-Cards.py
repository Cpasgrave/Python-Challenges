# Answer to challenge from Ali Gottschall:
# https://www.sololearn.com/Discuss/1016145/challenge-flipping-cards

'''
[Challenge] Flipping Cards
You get a deck of cards with n cards. Then you turn every card, every second, every third, every fourth and so on until you turn the n-th card. The question is how many cards are then face-up? I give you an example of a deck with 4 cards. 0 represents hidden and 1 means open
0: 0 0 0 0
1: 1 1 1 1
2: 1 0 1 0
3: 1 0 0 0
4: 1 0 0 1
So the answer for n = 4 would be two. I now challenge you to write a code to solve this puzzle for a general n. You can also solve it mathematicaly annd you will get a much easier..
'''

for n in range(100):
    print('{} cards - {} face-up'.format(n,int(n**0.5)))
