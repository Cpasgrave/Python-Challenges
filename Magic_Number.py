# https://www.sololearn.com/Discuss/1163537/assignment-magic-number

'''
[ASSIGNMENT] Magic Number ✨ by Donna
If the single digit comes to be 1 then the number is a magic number.

Example- 199 is a magic number as 1+9+9=19 but 19 is not a sigle digit number so 1+9=10 and then 1+0=1 which is a single digit number and also 1. Hence it is a magic number.
'''

def magic(x):
    while(len(str(x))!=1):
        x = list(str(x))
        print('+'.join(x),end='')
        x = eval('+'.join(x))
        print('=',x,sep='')
    return x
x = input()
if magic(x) == 1:
    print("yek,",x,"is magic !")
else:
    print("noke,",x,"not magic.")
