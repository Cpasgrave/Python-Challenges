# https://www.sololearn.com/Discuss/1035685/assignment-reverse-floyd-s-triangle

'''
Challenge by Danijel Ivanović
Write a program that prints 
the reverse Floyd's triangle.

The program should ask the 
user how many rows the triangle 
consists of.
  
Floyd's triangle consisting 
of 5 rows looks like this :
  
     15   14   13   12   11
     10     9     8     7
       6     5     4
       3     2
       1

HappyCodings!:-) 👍😊
'''

x=7 ; a=1 ; list=[['1']]
while len(list)<x:
    list.insert(0,[])
    for i in range(len(list[1])+1):
        a+=1
        list[0].insert(0,str(a))
print('\n'.join([' '.join(list[i])for i in range(len(list))]))
