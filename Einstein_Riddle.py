"""Einstein's Riddle

Einstein's Riddle is a logic puzzle. It is often claimed that only 2% of the population can solve the puzzle.
It has several variants, one of them is this:
1. There are five houses.
2. The Mathematician lives in the red house.
3. The Hacker writes in Python.
4. Brackets (code editor) is used in the green house.
5. The Analyst uses Atom (code editor).
6. The green house is immediately to the right of the ivory house.
7. The man who uses Redis (Database System) writes in Java.
8. Cassandra (Database System) is used in the yellow house.
9. Notepad++ (code editor) is used in the middle house.
10. The Developer lives in the first house.
11. The man who uses Hadoop (Database System) lives in the house next to the man writing in JavaScript.
12. Cassandra is used in the house next to the house where the primary language is C#.
13. The man who uses ArangoDB uses Sublime Text (code editor).
14. The Engineer uses MongoDB.
15. The Developer lives next to the blue house.

Now, who uses Vim? Who writes in C++?

Write a program that solves this riddle and outputs the answer.
"""

# Elements can be edited,
# all the groups must have the same number of elements
# and the number of groups must be the same

Hou  = '1',            '2',        '3',         '4',          '5'
Col  = 'Red',          'Green',    'Yellow',    'Ivory',      'Blue'
Job  = 'Mathematician','Hacker',   'Analyst',   'Engineer',   'Developer'
Lang = 'Python',       'Java',     'JS',        'C#',         'C++'
Edit = 'Brackets',     'Atom',     'Notepad++', 'SublimeText','Vim'
DB   = 'Redis',        'Cassandra','Hadoop',    'ArangoDB',   'MongoDB'

elements = [Hou,Col,Job,Lang,Edit,DB]
m = len(elements[0])
n = len(elements)
# The rules can be easily edited, within the following limits:
# 2 elements can and must be related in each line
# The relation can be:
# = and it's a direct relationship
# a unique positive or negative int (distance)
# two positive or negative ints (choice of possible distances)

rules = """
        Mathematician =    Red,
        Hacker        =    Python,
        Brackets      =    Green,
        Analyst       =    Atom,
        Green        -1    Ivory,
        Redis         =    Java,
        Cassandra     =    Yellow,
        Notepad++     =    3,
        Developer     =    1,
        Hadoop      +1 -1  JS,
        Cassandra   +1 -1  C#,
        ArangoDB      =    SublimeText,
        Engineer      =    MongoDB,
        Developer   +1 -1  Blue
        """

#########################################
#########################################

def apply_rules(solution,rules):
  '''Parse the grid row by row,
  Applying all the rules to each row'''
  G = solution[0]
  def one(G,row_i,j,k):
    '''place a 'one' in a solved cell,
    and the corresponding 'zeros'
    in the column's facing positions'''
    for i,g in enumerate(G):
      if i==row_i: # place 1 for the right element and 0 for other in the good row
        g[j]=[1 if i==k else 0 for i in range(m)]
      else: g[j][k]=0 # place 0 in other cells of the column

  def zeros(G,rows,j,k):
    """Places zeros in a column, excepting the given rows"""
    for i,g in enumerate(G):
      if i not in rows: g[j][k]=0

  for row_i,row in enumerate(G):

    for r in rules:
      shifts = r[2]
      for it in range(2):
        cell_a = row[r[it][0]][r[it][1]]
        row_b = row_i+shifts[0]*[1,-1][it]
        cell_b = G[row_b][r[1-it][0]][r[1-it][1]]if row_b in range(m) else 'out'

        if len(shifts) == 1: # same row and single shift rules
          check = cases.get((cell_a, cell_b))
          if   check in [7,10,12,15]: return 'impossible'
          elif check in [2,4]:        row[r[it][0]][r[it][1]]=0
          elif check == 3:            one(G,row_i,r[it][0],r[it][1])

        else: # 2 possible shifts rules
          row_c = row_i + shifts[1] * [1, -1][it]
          cell_c = G[row_c][r[1-it][0]][r[1-it][1]]if row_c in range(m) else 'out'
          cross = cases.get((cell_b,cell_c))

          if cell_a == 1:
            if   cross in (6,8,11,16): return 'impossible'
            elif cross in (2,4):       one(G,row_b,r[1-it][0],r[1-it][1])
            elif cross in (5,13):      one(G,row_c,r[1-it][0],r[1-it][1])
            elif cross == 1:           zeros(G,[row_b,row_c],r[1-it][0],r[1-it][1])
            elif cross == 3:           G[row_b][r[1-it][0]][r[1-it][1]]=0
            elif cross == 9:           G[row_c][r[1-it][0]][r[1-it][1]]=0

def fill_and_branch(solutions,final):

  branches = []
  badsol = set()
  for sol_i,sol in enumerate(solutions):
    G = sol[0] # G for grid
    # deduction: when only one possibility left, choose it:
    solved = 0 # counting cells with a found value in them
    for row_i,row in enumerate(G):
      for j,col in enumerate(row):
        if col.count(None)==1:
          indx = col.index(None)
          col[indx]=1
          for not_row in {*range(m)}-{row_i}:
            G[not_row][j][indx]=0
          solved +=1
        elif col.count(0)==m:
          badsol.add(sol_i)
        elif 1 in col:
          solved+=1

    # if nothing new happened, a guess is needed
    # two solutions will replace the current one
    # for each cell where only two posssibilities
    # are remaining:
    if solved==sol[-1] and sol_i not in badsol:
      # complete grids detected:
      if solved == m*n:
        if sol[0]not in final: final.append(sol[0])
        badsol.add(sol_i)
      else:
        # stuck grids detected:
        forks=0
        for row_i,row in enumerate(G):
          for col_i,col in enumerate(row):
            if col.count(None)==2:
              forks+=1
              idx=[i for i,j in enumerate(col)if j==None]
              B1,B2=[[col[:] for col in row[:]] for row in G],[[col[:] for col in row[:]] for row in G]

              for it,B in enumerate([B1,B2]):
                for bi,b in enumerate(B):
                  if bi==row_i: b[col_i] = [1 if i == idx[it] else 0 for i in range(m)]
                  else: b[col_i][idx[it]] = 0
              branches.append([sol_i,[B1,sol[-1]+1],[B2,sol[-1]+1]])
        if forks==0: # if there are no cells with only two alternatives
          badsol.add(sol_i)
    else: sol[-1] = solved

  #Next loops are dealing with the solution list
  for b in branches: # branching solutions
    solutions[b[0]]=b[1]; solutions.append(b[2])
  solutions = [s for i, s in enumerate(solutions) if i not in badsol]

  return solutions,final

def solve(elements,rules,formated=0,timed=0):

  global cases,m,n # dictionary used to check pairs of cells
  cases = {(None, None): 1,
           (None, 0): 2,
           (None, 1): 3,
           (None, 'out'): 4,
           (0, None): 5,
           (0, 0): 6,
           (0, 1): 7,
           (0, 'out'): 8,
           (1, None): 9,
           (1, 0): 10,
           (1, 1): 11,
           (1, 'out'): 12,
           ('out', None): 13,
           ('out', 0): 14,
           ('out', 1): 15,
           ('out', 'out'): 16}

  # Formating the rules: (first cell, second cell, shift(s))
  # ex: "Hadoop +1 -1 Javascript" becomes ((5,2),(3,2),(1,-1))
  #     "Green -1 Ivory" becomes ((1,1),(1,3),(-1,))
  #     "Notepad++ = 3" becomes ((4,2),(0,2),(0,))
  if formated==0:
    rules = {(lambda x: (*[(i, j) for i, el in enumerate(elements) for j, e in enumerate(el) if e == x[0]],
                        *[(i, j) for i, el in enumerate(elements) for j, e in enumerate(el) if e == x[-1]],
                        tuple(0 if i == '=' else int(i) for i in x[1:-1])))(r.split()) for r in rules.split(',')}

  # Initial Grid:
  Grid = [[[1 if row == k else 0 for row in range(m)]] + [[None for i in range(m)] for j in range(m)] for k in range(m)]

  # Each solution in the solutions list will contain:
  # its grid and its number of solved cells
  solutions = [[Grid,m],[[[col[:] for col in row[:]] for row in Grid][::-1],m]]
  final = [] # completed grids
  rounds = 0
  if timed:
    t = time()
  while len(solutions):
    c = 0
    while c < len(solutions):
      if apply_rules(solutions[c],rules)=='impossible': del solutions[c]; c-=1
      c+=1
    solutions,final = fill_and_branch(solutions,final)
    rounds += 1
    if timed:
      if time()-t>0.03:
        break
  return final,rounds

def final_print(final,rounds):
  print(f'{rounds} rounds needed to solve it:\n')
  if final == []:
    print("no solution found")
  for G in final:
    G=['|'.join([elements[j][aa.index(1)][:3].center(3)if 1 in aa else' '*15 for j,aa in enumerate(a)])for i,a in enumerate(G)]
    print(*G, sep='\n')
    print()

def create_rules():
  from random import sample,choice
  Target = sorted(zip(*[[[1 if j==s else 0 for j in range(m)] for s in sample([*range(m)],m)]for i in range(n)]))[::-1]
  rulz = set()
  final = []
  while len(final)!=1:
    for _ in range(30):
      shifts_num = choice([1,2])
      cell_a = (choice([*range(m)]),choice([*range(n)]))
      cell_b = (choice([*range(m)]),choice([*range(n)]))
      elem_a = cell_a[1],Target[cell_a[0]][cell_a[1]].index(1)
      elem_b = cell_b[1],Target[cell_b[0]][cell_b[1]].index(1)
      shifts = (cell_b[0]-cell_a[0],)
      if shifts_num == 2:
        shift_2 = choice([i-cell_a[0] for i in range(m) if (i-cell_a[0])!=shifts[0]])
        shifts = tuple(choice([[*shifts,shift_2],[shift_2,*shifts]]))
      rulz.add((elem_a,elem_b,shifts))
    final,rounds = solve(elements, rulz,1)

  for r in set(rulz):
    temp = solve(elements,rulz-{r},1,1)[0]
    if len(temp)==1:
      rulz.remove(r)
  rulz = '\n'.join(['{:>13} {:^5} {:13} '.format(elements[r[0][0]][r[0][1]],' '.join(['+'*(i>0)+(str(i) if (i or len(r[2])==2) else '=') for i in r[2]]),elements[r[1][0]][r[1][1]]+',') for r in rulz])
  return rulz

from time import perf_counter as time
t = time()

final_print(*solve(elements,rules))

print("    !! Your turn now !!\n(there's only one solution)\n       new rules:\n")
new_rules = create_rules()
print(new_rules)
