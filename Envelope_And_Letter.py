# https://www.sololearn.com/Discuss/1065546/challenge-envelope-letter
''' My answer to Challenge by Gaurav Agrawal :'''
from itertools import permutations as perm

n = 7

def how_many (n):
    letters = [i for i in range(1, n + 1)]
    permuts = [j for j in perm(letters)]
    p = 0
    while p < len(permuts):
        for k in range(n):
            if permuts[p][k] == k + 1:
                permuts.remove(permuts[p])
                p-=1
                break
        p += 1
    print('{} letters and envelopes - {} possible ways to totally fail the mailing'.format(n,len(permuts)))

how_many(n)
    
'''👉👉👉 CHALLENGE ::: ENVELOPE 📧 & LETTER 💌
U have to find number of ways in which no letter goes to correct envelope 
example ::: if in.put is 3 
then , 3 envelope  E1,E2,E3  
           3 letters   L1,L2,L3
//correct combination :::  (E1L1 , E2L2 , E3L3)
👉 possible arrangements
 (E1L2 , E2L3 , E3L1)
 (E1L3 , E2L1 , E3L2)
/*therefore 2 such combinations for 3 letters and 3 envelopes such that no letter goes in correct envelope*/
//output must be 2 

Bonus ::: print the combinations 🙌

all languages are welcome ☺ 

//best of luck  & happy coding ☺👍'''
