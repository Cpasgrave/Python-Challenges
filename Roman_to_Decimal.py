'''
takes roman number and converts it to decimal
'''

r = 'MCMLXXVI'

d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, "V":5, 'I': 1}
 
print(sum([-d[r[i]] if d[r[i]]<d[r[i+1]] else d[r[i]] for i in range(len(r)-1)]+[d[r[-1]]]))
