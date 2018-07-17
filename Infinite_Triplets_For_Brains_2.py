a='123'
# a is a string
while True:
# while true is here to produce an infinite loop
    print(a)
# a will be printed at each iteration.
    a = a[1:]+str(int(a[-1])%9+1)
# and this is the center of the code : at each iteration, 'a' is modified. a[1:] takes the 2 last characters of a (e.g.: if a is '123', a[1:] is '23', if a = '789', a[1:] = '89', ...)
# then a[-1] is the last character of a, for a = '123', a[-1] = '3'. int(a[-1]) turns it to an integer. %9 will keep it unchanged unless it is 9. and then it will give 0. + 1 adds one to this number, and finally str() turns it back to a string.
# The first process is doing :
# a = '123'
# print(a)
# ---> 123
# a = '23' + '4' (='234')
# next iteration :
# print(a)
# ---> 234
# a = '34' + '5' (='345')
# etc ...
