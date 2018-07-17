# Challenge by Fabio
# https://www.sololearn.com/Discuss/1156970/challenge-even-or-odd-number
'''
Challenge - Even or Odd number.
Make a program that takes a given number and let know to the user whether that number is even or not, but you can't use any condition nor loop statement like if-else, switch, ternary, while, do while, for, for-each. 
All languages are welcome. 
Any question or suggestion is welcome too. 
Have fun!
'''
a = 19254157
print(a,'is',['even','odd'][a%2])

a = 19254158
print(a,'is',['even','odd'][a%2])


a = 238
c = str(a/2).replace('.0','even').replace('.5','odd ')[-4:]
print(a,'is',c)

a = 239
c = str(a/2).replace('.0','even').replace('.5','odd ')[-4:]
print(a,'is',c)

a = 3477
c = int(int(str(a/2)[-1])/5)*'odd'+int(int(str(a/2-0.5)[-1])/5)*'even'
print(a,'is',c)

a = 3478
c = int(int(str(a/2)[-1])/5)*'odd'+int(int(str(a/2-0.5)[-1])/5)*'even'
print(a,'is',c)

a = 111143
b = ['oden','even','odd'][(-1)**int(str(a)[-1])]
print(a,'is',b)

a = 111142
b = ['oden','even','odd'][(-1)**int(str(a)[-1])]
print(a,'is',b)
