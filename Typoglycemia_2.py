# https://www.sololearn.com/Discuss/1041633/%EF%B8%8Fchallenge-%EF%B8%8F-typoglycemia
'''
☢️CHALLENGE☢️: Typoglycemia proposed by Murillo Pyaia

Typoglycemia is the mind's ability to decipher a mispelled word if the first and last letters of the word are correct.
Make a program that receives user input and outputs the typoglycemic version of the string.
Example:
Input: "I love SoloLearn"
Output: "I lvoe SLloorean"

Good luck and good coding!'''

from re import findall
from random import shuffle
text = "If you are coming from Java world, you might already have heard about the method overloading in Java. " \
       "Kotlin, with the help of default parameters and named arguments helps us to reduce the number " \
       "of overloads that we generally need in Java world."

pattern = r'(\w+)(\W+)'
matches = findall(pattern,text)
words = []
for m in matches:
    words.append(m[0])
    words.append(m[1])
glyc = [] ; s = ''
for i in range(len(words)):
    if len(words[i])<4 or (len(words[i])==4 and words[i][1]==words[i][2]):
        glyc.append(words[i])
    else:
        s = words[i][1:-1]
        while True:
            l = list(s)
            shuffle(l)
            if ''.join(l) != words[i][1:-1]: break
        glyc.append(words[i][0]+''.join(l)+words[i][-1])
print(''.join(glyc))
