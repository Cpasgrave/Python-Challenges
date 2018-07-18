n = input() # up to 3 999 999

print(''.join([''.join(['IVXLCDMvxlcdm'[int(i)+2*s]for i in'.0.00.000.01.1.10.100.1000.02'.split('.')[int(n[::-1][s])]])for s in range(len(n))][::-1]))
