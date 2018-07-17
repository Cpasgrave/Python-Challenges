# https://www.sololearn.com/Discuss/1142841/assignment-challenge-tetrahedron
# https://www.sololearn.com/Discuss/1148022/assignment-challenge-tetrahedron-2

'''
answer to Gaurav Agrawal's funky challenge :
CHALLENGE ::: TETRAHEDRON [2]

previous challenge was :

Your task is to find number of ways in which we can reach from point 'A' to point 'A' in n-steps .
'n' will be provided as the user #input .

Example : inp : 3 
          out : 6
          [ABCA,ABDA,ACBA,ACDA,ADBA,ADCA]
          
the only difference in this challenge is that , now we have to find no. of paths of n steps possible for reaching from pt. A to pt. B 
//1 step means 1 jump 
//give it a try , be simple 👍
//WARNING : forget U know some basic math
'''

start = 'A'
end = 'B'

def travel(n,start,end):
    paths = [start]
    tetra = 'ABCD'
    for i in range(n):
        temp = []
        if i == n-2:
            tetra.replace(end,'')
        if i == n-1:
            tetra = end
        for p in paths:
            for vertice in tetra.replace(p[-1],''):
                temp.append(p + vertice)
        paths = temp
    return len(paths),paths

print('from',start,'to',end,':')
for i in range(1,13):
    print(i,'steps -->',travel(i,start,end)[0],'different paths')
#    print(travel(i,start,end)[1])

# printing the paths is commented, because it's taking too long on CodePlayground.
