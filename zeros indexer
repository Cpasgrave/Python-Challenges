"""
this code returns the index of the 3 first zeros in the input number or string if there are any.
"""

data = input("come on give me your number !  --->\n")
list = [i for i in range(len(data)) if data.startswith('0', i)][:3]
order = ['first:', 'second:', 'third:']
for i in range(3) :
    if i < data.count('0') :
        print (order[i]+str(list[i]))
    else :
        print ('not found')
        break
