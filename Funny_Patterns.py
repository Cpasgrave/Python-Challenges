from random import choice

'''
for i in range(30):
    for j in range(30):
        print(choice([chr(i) for i in [176,177,178,219,220,221,222,223]]),end='')
    print('\n',end='')
'''

colours = [176,177,178,219,220,221,222,223]
print('pattern 1')  
n=1
for i in range(15):
    for j in range(27):
        print(chr(colours[n%8]),end='')
        n = (n+j*i)//2
    print('\n',end='')
print('pattern 2')    
n=1
for i in range(15):
    for j in range(15):
        print(chr(colours[n%8]),end='')
        n = (n+i+j)
    print('\n',end='')
print('pattern 2')
n=1
for i in range(30):
    for j in range(33):
        print(chr(colours[n%8]),end='')
        n = (n+i+j)//3
    print('\n',end='')
