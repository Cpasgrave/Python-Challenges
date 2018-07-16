# https://www.sololearn.com/Discuss/1041633/%EF%B8%8Fchallenge-%EF%B8%8F-typoglycemia
'''
☢️CHALLENGE☢️: Typoglycemia proposed by Murillo Pyaia

Typoglycemia is the mind's ability to decipher a mispelled word if the first and last letters of the word are correct.
Make a program that receives user input and outputs the typoglycemic version of the string.
Example:
Input: "I love SoloLearn"
Output: "I lvoe SLloorean"

Good luck and good coding!'''

import re
from random import sample

text = "Hey! I used regex ... It's keeping punctuation, while typoglyceming words ;)"

pattern = '(\w)(\w+)(\w)(\W*)|(\w{1,2})(\W*)'
cut = [list(i) for i in re.findall(pattern,text)]
for i in cut:
    while True:
        egg = sample(i[1],len(i[1]))
        if ''.join(egg) != i[1] or len(i[1])<2:
            break
    i[1]=''.join(egg)
    print(''.join(i),end='')
