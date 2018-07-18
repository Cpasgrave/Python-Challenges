'''
Kaprekar's constant challenge by Kuba Siekierzynski

The number 6174 is known as Kaprekar's constant. It is the ultimate convergence point of the Kaprekar's routine, an algorithm thought up by Indian mathematician D.R. Kaprekar in 1949.

The routine is as follows:
1. Take any four-digit number (at least two different digits must be used, zeroes allowed).
2. Arrange the digits in descending and then in ascending order to get two four-digit numbers.
3. Subtract the smaller number from the larger and get the result.
4. Repeat steps 2-4 with the new number.

After a few iterations, the algorithm converges to a fixed point and starts to result in the same number  - 6174 - the so-called Kaprekar's constant.

For Example:
n = 5324

5432 - 2345 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174
7641 - 1467 = 6174

For numbers beyond four digits the routine might converge to 0 (zero), other constants or "loops" (infinitely repetitive sequences of the same numbers over and over again).
Challenge - level: Easy
Write a code which finds the Kaprekar's constant for any four-digit number.

Challenge - level: Medium
Write a code which finds Kaprekar's constant for any number in the range of 101-9999, checking if the digits of the number are not too repetitive (no repetitions for three-digit numbers and max 2 repetitions for four-digit ones).

Challenge - level: Hard
Write a code that universally finds Kaprekar's constants and/or loop for any K-digit number. If a sequence is found, all the numbers comprising it have to be returned.
-------------------------------------
-------------------------------------
-------------------------------------
This code is meant to be used on a local interpreter.

The following settings here are very narrow, for it
to run as an example on SL.
'''
# from base
b1 = 2
# up to base (included)
b2 =10
# from d1 digits numbers
d1 = 3
# up to d2 digits numbers (included)
d2 = 3

def convert(a,in_base,out_base):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '}']
    table = dict(zip(num,range(len(num))))
    dec = 0
    b= list(a)[::-1]
    for i in range(len(b)):
        dec += table[b[i]]*in_base**i
    res = []
    while dec:
        test = dec % out_base
        dec = (dec - test) // out_base
        res.append(num[test])
    result = ''.join(res[::-1])
    return result

def kaprekar(n,base):
    chain = [n]
    while True:
        a = sorted(list(n))
        b = a[::-1]
        c = int(convert(b,base,10))-int(convert(a,base,10))
        if c == 0:
            return ['0']
        c = str(c)
        c = convert(c,10,base)
        while len(c)<len(a): c='0'+c
        if c in chain:
            return chain[chain.index(c):]
        chain.append(c)
        n = c

for b in range(b1,b2+1):
    print(chr(1),chr(6),' Base {:2d} {}'.format(b,chr(6)*20),sep='')
    for d in range(d1,d2+1):
        kaps = []
        kapsets = []
        freq = []
        for n in range(b**(d-1),b**d):
            n = convert(str(n),10,b)
            k = kaprekar(n,b)
            if set(k) not in kapsets:
                kaps.append(k)
                kapsets.append(set(k))
                freq.append(1)
            else:
                freq[kapsets.index(set(k))] +=1
        freq_percent = [100*i/sum(freq) for i in freq]
        print(chr(25),chr(6)*6,' with {} digits :'.format(d),sep='')
        for i in range(len(kaps)):
            loop =''
            if len(kaps[i])==1:
                kap = kaps[i][0]
            else:
                kap = "loop"
                loop = '->'.join(kaps[i])
            print(chr(5),' {:<9}-{:>8}--> {:7.3f}%  - {}'.format(kap,freq[i],freq_percent[i],loop),sep='')
        print(chr(3),chr(6)*32,sep='')
    print('')
    
