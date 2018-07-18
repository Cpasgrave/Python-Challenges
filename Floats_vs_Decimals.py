'''
This code demonstrates the danger of floats when making an increasing number of operations on them.
It also shows the benefits of the Decimal module solution.
'''

import decimal

def iterate(n):
    a = decimal.Decimal('1')
    b = decimal.Decimal('2')
    aa = 1
    bb = 2
    def process(a, b, n):
        for i in range(n):
            b = (b + a * b) / a
            a = 100 - b
        return b
        
    b=process(a,b,n)
    bb=process(aa,bb,n)
    
    bb = decimal.Decimal(str(bb))
    print('--',n,'iterations:\npython float->',bb,'\ndecimal     ->',b,'\n',b-bb,'(difference)\n')

for n in [1,10,100,200,300,400,500,600,620,640,645,650,660,670,671,675,680,690,700,800,900,1000,10000,100000,1000000]:
    iterate(n)
