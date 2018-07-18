'''
Summations Calculator by Faisal

Create a program that takes 3 inputs, a lower bound, an upper bound and the expression. Calculate the sum of that range based on the given expression and output the result.

For Example:
Input: 2 4 *2
Output: 18 (2*2 + 3*2 + 4*2)

Input: 1 5 %2
Output: 3 (1%2 + 2%2 + 3%2 + 4%2 + 5%2)'''

print((lambda a:sum([eval('i'+a[2]) for i in range(int(a[0]),int(a[1])+1)]))(input().split()))
