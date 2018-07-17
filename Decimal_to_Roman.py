'''
Challenge Roman Numerals proposed by William SELLIER
    
Converts decimal number to Roman'''

n = str(input()) # up to 3 999 999

pat = ['','0','00','000','01','1','10','100','1000','02']

res = [''.join(['IVXLCDMvxlcdm'[int(i)+2*s] for i in pat[int(n[::-1][s])]]) for s in range(len(n))]

print(''.join(res[::-1]))
