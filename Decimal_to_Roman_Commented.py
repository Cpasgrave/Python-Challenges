n = str(input()) # up to 3 999 999

# pat is the list of patterns corresponding to each decimal
# digital : 0,1,2,3,4,5,6,7,8,9
# e.g. '000' correspond to '3' and will give 'III' or 'XXX' or 'CCC', etc ...
#      '10' comes for '4' and wil give 'IV' or 'XL', etc ...
#      '20' for 9 will produce 'IX' or 'XC', etc ...
# Those patterns are using 0 for 'no modification'
# '1' will fetch the next letter in 'IVXLCDMvxlcdm'
# '2' will fetch the second next letter.
# so when the current letter is 'I', 
# each 0 will add an 'I'
# each 1 will add a 'V'
# each 2 will add an 'X'
# when the current letter is 'X',
# each 0 will add an 'X'
# each 1 will add a 'L'
# each 2 will add an 'C
# You may have notices that the patterns are actually
# reverse, that's because the whole conversion is 
# processed backwards and reversed at the end.
# Lowercase letters are used to represent the
# higher values (highercase letter x 1000)
# v = 5000, x = 10.000, l = 50.000, etc ...
pat = ['','0','00','000','10','1','01','001','0001','20']
res = []

for pos in range(len(n)):
    # The digits from input (as a string) are turned to 
    # an integer and then processed successively, 
    # using pos to point their position, from the last 
    # to the first : it's the reason for n[::-1] next line
    for i in pat[int(n[::-1][pos])]:
        # the current digit is used to find the 
        # corresponding pattern in pat.
        # And in the next line, each 0, 1 or 2
        # associated with the position 'pos' of the 
        # current digit will return the right roman letter.
        # e.g. n = 1369, when it's 6's turn, pos = 1
        # 6 will return '01' from pat from which:
        # 0 will be added to (pos=1)*2, which gives 2
        # and at index 2 in the roman letters string,
        # we find 'X'. Same with the '1':
        # 1+(pos=1)*2 = 3 -> 'L'
        res += ['IVXLCDMvxlcdm'[int(i)+2*pos]]

print(''.join(res[::-1]))
