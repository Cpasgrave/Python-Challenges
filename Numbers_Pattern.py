# https://www.sololearn.com/Discuss/993048/new-challenge-numbers-pattern
# Challenge by Daniel
'''
Try to develop a code in any language which calculate that numbers pattern and complete each row until five numbers per row

1-2-5-27-
2-3-11-
3-4-19-
4-5-29-
5-6-41-

Good Luck!!!
'''

for x in range(-9,10):
    s = [x,x+1]
    for i in range(3):
        s.append(s[-1]**2+s[-2])
    print([n for n in s])
