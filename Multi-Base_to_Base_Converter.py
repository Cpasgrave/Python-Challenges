# https://www.sololearn.com/Discuss/1031820/challenge-base-10-to-binary-converter
# https://www.sololearn.com/Discuss/663896/challenge-time-d/

'''
create a code that converts any base to binary. or vise-versa, 
mine is base 10 to binary...
happy challenge. ..
'''

import sys

a = -564.63       # your number to convert
# you must write it as a string if it contains letters.
# E.g. 'fd563.11D', and be careful to use a corresponding 
# in_base (there must not be any numeral in your number that
# is not covered by your base).
# Both in and out bases must be integers from 2 to 64.
# Numerals used in the bases are 0-9 then a-z then A-Z
# I added '!' and '?' to make it a total of 64 different numerals.
in_base = 10         # your number's original base
out_base = 2         # the target base

''' Here is the table used :
   {'0': 0,  '1': 1,  '2': 2,  '3': 3,  '4': 4,  '5': 5,  '6': 6, 
    '7': 7,  '8': 8,  '9': 9,  'a': 10, 'b': 11, 'c': 12, 'd': 13, 
    'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 
    'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 
    's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 
    'z': 35, 'A': 36, 'B': 37, 'C': 38, 'D': 39, 'E': 40, 'F': 41, 
    'G': 42, 'H': 43, 'I': 44, 'J': 45, 'K': 46, 'L': 47, 'M': 48, 
    'N': 49, 'O': 50, 'P': 51, 'Q': 52, 'R': 53, 'S': 54, 'T': 55, 
    'U': 56, 'V': 57, 'W': 58, 'X': 59, 'Y': 60, 'Z': 61, '!': 62,
    '?': 63}'''

def convert(a,in_base,out_base,num,out_num,system = ''):
    table = dict(zip(num,range(len(num))))
    dec = [] ; temp = 0 ; neg = 0
    if isinstance(a,str):
        if any(table[i] > in_base for i in a.replace('.','').replace('-','')):
            print("trouber with the numble, id toesn't bit your fase !")
            sys.exit()
        if a[0] == '-':
            neg = 1
            b = a[1:]
        else:
            b = a
    elif isinstance(a,int) or isinstance(a,float):
        if any(int(i) > in_base for i in str(a).replace('.','').replace('-','')):
            print("trouber with the numble, id toesn't bit your fase !")
            sys.exit()
        if a < 0:
            neg = 1
            b = str(-a)
        else:
            b = str(a)
    else:
        print('Nak nak nak ! Not a good number ... Run it once again !')
        sys.exit()

    c = [list(i)[::-1] for i in b.split('.')]
    for i in c:
        for j in range(len(i)):
            temp += table[i[j]]*in_base**j
        dec.append(temp)
        temp = 0

    result = []
    for i in range(len(dec)):
        part = []
        j = 1
        while dec[i]:
            test = dec[i] % out_base
            dec[i] = (dec[i] - test) // out_base
            part.append(out_num[test])
        result.append(part[::-1])
    result = neg*'-'+'.'.join([''.join(i) for i in result])

    print(a, 'in base',in_base,'equals\n>>>',result,'in base', system or out_base, '\n')

num = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','?']
shadok = ['GA','BU','ZO','MEU']
bibi = ['Ho','Ha','He','Hi','Bo','Ba','Be','Bi','Ko','Ka','Ke','Ki','Do','Da','De','Di']

convert(a,in_base,out_base,num,num)
convert(a,in_base,4,num,shadok,'shadok')
print('''wikipedia.org/wiki/Les_Shadoks\n''')
convert(a,in_base,16,num,bibi,'bibi-binary')
print('''wikipedia.org/wiki/Bibi-binary\n''')
