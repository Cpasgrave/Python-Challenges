# https://www.sololearn.com/Discuss/1058514/challange-tricky-sequence
''' Challenge proposed by Oma Falk:

Find the secret of the following sequence.
Find all sequences following the same rule.

1,7,1,2,5,6,2,3,4,7,5,3,6,4

All weapons welcome
Have fun'''

def tricky(x):
    solution = [[None for i in range(x*2)]]
    step(solution,x)
def step(solution,x,index=0):
    n=0
    while n<len(solution):
        temp=[]
        keep = 0
        for i in range(1,x+1):
            sol = [j for j in solution[n]]
            if sol[index] is not None:
                keep = 1
                n+=1
                break
            elif i in sol:
                continue
            else:
                if index + i + 1 >= len(sol):
                    continue
                else:
                    if sol[index + i + 1] is not None:
                        continue
                    sol[index] = i
                    sol[index + i + 1] = i
                    temp.append([k for k in sol])
        if keep == 0:
            solution.remove(solution[n])
        for s in temp:
            solution.insert(n,s)
            n+=1
    if index == 2*x-2:
        for s in solution:
            if s[::-1] in solution:
                solution.remove(s[::-1])
        for seq in solution:
            print(','.join([str(i) for i in seq]))
        print(len(solution),'different solutions (after removing reverse)')
    else:
        step(solution,x,index+1)

tricky(7)
