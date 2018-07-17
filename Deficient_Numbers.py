# Challenge by Krishna Teja Yeluripati
'''
Deficient Numbers

A number is considered deficient if the sum of its factors is less than twice that number.

For Example:
10 is a deficient number.
Factors of 10 are 1, 2, 5, 10
Sum is 1 + 2 + 5 + 10 = 18 < 2 * 10

Tasks:
(Easy) Write a program to verify whether a given number is deficient or not.
(Medium) Write a program to find all the deficient numbers in a range.
(Hard) Given a number, write a program to display its factors, their sum and then verify whether it's deficient or not.
'''

x = 2557834

fac = [n for n in range(1,x+1) if x%n==0]
tot = sum(fac)
#----printing addition----------------
w=len(str(max(fac)))+2
print('{:{w}}'.format(1,w=w))
for i in fac[1:]:
  print('{:=+{w}}'.format(i,w=w))
print(chr(196)*w)
print('=','{:{w}}'.format(tot,w=w-1),sep='')
#----printing explanation-------------
de = tot<2*x
print('\n',x,' is',' not'*(not de),' a deficient number, because :',sep='')
print(tot,' < ' if de else ' > ',2*x,' (2 x ',x,')',sep='')
#----All deficient from 1 to 600------
print('\nFollowing numbers are all deficient numbers from 0 to 1000:')
for i in range(1001):
  if sum([n for n in range(1,i+1) if i%n==0]) < 2*i:
    print(i,', ',sep='',end='')
