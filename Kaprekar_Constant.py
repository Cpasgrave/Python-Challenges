'''Kaprekar's constant challenge by Kuba Siekierzynski

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
'''

n = 14365

def kaprekar(n):
    chain = [n]
    while True:
        a = sorted(list(str(n)))
        b = a[::-1]
        c = int(''.join(b)) - int(''.join(a))
        print(int(''.join(b)),'-', int(''.join(a)),'=',c)
        if c in chain:
            chain.append(c)
            print("Convergence took",len(chain),"steps\n")
            print("The loop is :\n",' -> '.join(str(i) for i in chain[chain.index(c):]),'\n')
            break
        chain.append(c)
        n = c
print('four digits example :')
kaprekar(9135)
print('example with n =',n)
kaprekar(n)
