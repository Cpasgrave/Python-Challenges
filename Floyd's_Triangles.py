'''
Floyd's Triangles Challenge by Danijel Ivanović 

Floyd's triangle is a right-angled triangular array of natural numbers, used in computer science education. It is named after Robert Floyd, who was an eminent computer scientist.
It is defined by filling the rows of the triangle with consecutive numbers, starting with a 1 at the top left corner.
Write a program to print the Floyd's triangle and reverse Floyd's triangle by taking the number of rows as input.

For Example:
Input: 5
Output:
Floyd's triangle:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

Reverse Floyd's triangle:
15 14 13 12 11
10 9 8 7
6 5 4
3 2
1
'''
#########################
# Both
#########################
a = int(input())

for t in [1,-1]:
  print("\n","-- Floyd's triangle --"[::t].center(a*4),"\n")
  for i in range(1,a+1)[::t]:
    m = sum(range(i))
    n = m+i
    line = []
    for i in range(m,n)[::t]:
      line.append(str(i+1).center(3))
    print(' '.join(line).center(a*4 if a>5 else 24))
 #########################
 # Reverse Recursive
 #########################
    x = 7
l = lambda x:[[l(a-1)[0][0]+i for i in range(a,0,-1)] if a>1 else [1] for a in range(x,0,-1)]
[print(' '.join([str(n) for n in r])) for r in l(x)]

#########################
# Both, onelined
#########################
(lambda a:[[print(*[i+1 for i in range(sum(range(i)),sum(range(i+1)))][::t])for i in [*range(1,a+1)[::t],0]]for t in [1,-1]])(int(input()))

#########################
# Older solution
#########################

# https://www.sololearn.com/Discuss/1035685/assignment-reverse-floyd-s-triangle

x=7 ; a=1 ; list=[['1']]
while len(list)<x:
    list.insert(0,[])
    for i in range(len(list[1])+1):
        a+=1
        list[0].insert(0,str(a))
print('\n'.join([' '.join(list[i])for i in range(len(list))]))
