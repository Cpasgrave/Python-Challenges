 
"""
Write a function that receives an array of integers and returns the minimal sum of the array (sum of products of each two adjacent numbers).

For Example: 
Without sorting the array [40,25,10,5,1], the sum is:
(40*25) + (25*10) + (10*5) + (5*1) = 1305

The challenge is to find the best possible sort of the array elements, to have the minimal sum result.
"""

a = [40,25,10,5,1]

b = [sorted(a)[::-1][i] for i in [j*(-1)**(j+len(a)%2*(j>len(a)//2)) for j in range(len(a))]]

c = sum([i*j for i,j in zip(b[:-1],b[1:])])

print(b,c)
