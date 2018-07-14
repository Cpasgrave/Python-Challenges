"""
This codes takes two letters as input and returns the ordered alphabet letters from the first to the second, in ascending or descending order depending on the given letters.
"""

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
range=[]
first=input("first ?\n")
print(first)
last=input("last ?\n")
print(last)

if (first not in alphabet) or (last not in alphabet) :
 print("Sorry girl, you can enter latine letters only, try harder !")
else :
 range.append(first)
 x=(alphabet.index(first))
 y=(alphabet.index(last))
 while(y>x):
  x+=1
  range.append(alphabet[x])
 while(x>y):
  x-=1
  range.append(alphabet[x])
 print(range)
