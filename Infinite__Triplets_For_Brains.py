 '''
Brains asked for a function to produce infinite triplets following next pattern:
123
234
345
456
567
678
789
891
912
123
...
'''

print('\n'.join([''.join([str(i)for i in range(1,10)]*2)[a%9:a%9+3] for a in range(500)]))
