# *-* coding: utf-8 *-*
# https://www.sololearn.com/Discuss/1075091/double-base-palindromic-numbers

'''
This code's purpose is to find out multi-base palindromic numbers.
Original idea is from Dmytro Kovryzhenko and the challenge :
https://www.sololearn.com/Discuss/1075091/double-base-palindromic-numbers

I pushed it a little further, using my multi-base converter code:
https://code.sololearn.com/cYcOQFySB6C9/#py

The code will not go very far on Code Playground.
The settings here are making it check numbers
from 1 to 300 only (line 87). Those numbers are converted to 
all the bases from 2 to 64, and then tested to see
if they are palindromic.
Taking the 64 different bases expressions of the same number,
the code prints if there are at least 2 palindromic forms.
And kept palindromic numbers only when they are made of
at least 3 characters. I considered numbers like 33 not
palindromic, just doubles (even if technically 
they are palindromic numbers, but less interesting)

At the end of the process, the code prints the "most palindromic"
number(s). It means : the number that has the biggest number of 
palindromic expressions.
E.g. from 1 to 300, the most palindromic numbers are :

['121(b.10)', '11111(b.3)', '232(b.7)', '171(b.8)'], 
['3223(b.4)', '454(b.7)', '353(b.8)', '151(b.13)'], 
['11111111(b.2)', '3333(b.4)', '313(b.9)', '212(b.11)'], 
['100000001(b.2)', '10001(b.4)', '515(b.7)', '101(b.16)'], 
['100010001(b.2)', '10101(b.4)', '333(b.9)', '111(b.16)']

each list represents one number expressed in different bases.
between parenthesis is the base of each expression.
So we have 5 numbers with 4 palindromic forms each.

I ran the code on my pc to check numbers up to 10.000.000
and the 'most palindromic' number happens to be :

['1000100010001(b.2)', '1010101(b.4)', '1111(b.16)', 'd8d(b.18)', '373(b.37)', '1H1(b.48)', '1w1(b.52)', '1m1(b.56)']
There is only one number with 8 palindromic forms in the 64 first bases.
This number, in base 10, is: 
---- 4369 ! ----

You can see the entire list of the multi-base palindromic numbers 
from 1 to 10.000.000 here :
https://code.sololearn.com/cA2yJVl2P3Sg/#py

edit : I checked again, including 1 characters and 2 character 
palindromic numbers and it gives the same result.
4369 appears to really be the most palindromic number.
'''

def convert(a,in_base,out_base,num,out_num):
    table = dict(zip(num,range(len(num))))
    dec = [] ; temp = 0
    b = [list(i)[::-1] for i in str(a).split('.')]
    for i in b:
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
    result = '.'.join([''.join(i) for i in result])
    return result

num = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','?']

def ispalyndrome(a):
    if not isinstance(a,str):
        a = str(a)
    pal = True
    for i in range(len(str(a))//2):
        if a[i] == a[-i-1]:
            continue
        else:
            pal = False
            break
    return pal

max = 2 ; best = []
for i in range(1,300):
    temp = []
    a = i
    if ispalyndrome(a):
        temp.append('{}(b.10)'.format(a))
    in_base = 10
    k_list = [*range(2,64)]
    k_list.remove(10)
    for k in k_list:
        out_base = k
        b = convert(a,in_base,out_base,num,num)
        if ispalyndrome(b) and len(b)>2:
            temp.append('{}(b.{})'.format(b,k))
    if len(temp)>1:
        print(' - '.join(temp))
        if len(temp) == max:
            best.append(temp)
        if len(temp) > max:
            max = len(temp)
            best = [temp]
print('best - ',best)
