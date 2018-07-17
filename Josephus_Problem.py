'''
N people (numbered 1 to N) are standing in a circle. Person 1 kills Person 2 with a sword and gives it to Person 3. Person 3 kills Person 4 and gives the sword to Person 5. This process is repeated until only one person is alive.

Task:
(Medium) Given the number of people N, write a program to find the number of the person that stays alive at the end.
(Hard) Show each step of the process.
'''

N=17

a = [str(i) for i in range(1,N+1)]

sw = 0
for i in range(N-1):
  dead = a[(sw+1)%len(a)]
  a = a[:(sw+1)%len(a)]+a[(sw+2)%len(a):]
  sw=(sw+1)%len(a)
  print('_'.join(a),'\n...',dead,'is dead,',a[sw],'has the sword\n')
  
print(a[0],'is a happy lonesome killer')
