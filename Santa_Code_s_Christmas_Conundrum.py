# -*- coding: utf-8 -*-

'''
[Challenge] Santa Code's Christmas Conundrum

Merry Christmas, SoloLearners! It's been a while since I've made a challenge, hasn't it?

WARNING
Incidentally, this code *can* be run, and you might get a surprising output if you do. ;)

INTRODUCTION
Once every year, on a very mystical date, it is the day of every programmer's dream. Santa Code goes around SoloCity to help every programmer debug their code. Naturally, this makes programmers lazy and refuse to debug their code, so Santa Code has changed his routine.

Instead of going around every house, now he runs a predetermined route around SoloCity debugging codes that take the least time. His aim is now to cross SoloCity taking the least time possible.

Being an experienced programming elf in Santa Code's Programming Factory, you are required to write a program to calculate Santa's optimal route.

INPUT
Conveniently, SoloCity is completely rectangular. A two dimensional matrix will be used to represent each house in SoloCity, and the time taken to debug the lazy resident's code within. Santa cannot move diagonally, but only left/right or up/down.
Example:
[[1, 5, 4, 3],
 [4, 7, 8, 2],
 [5, 3, 1, 4],
 [3, 6, 4, 2]]
Start = 12, End = 3 
Two more numbers, start and end, will represent where to start and where to end. The first square [1] will be the 0th index, and the second square [5] will be the 1st index, and so on. Here our start is 12 (bottom left square) and end is 3 (top right square).

OUTPUT
Your code should output a string, the directions Santa Code will move, and the time taken.
U->Up, D->Down, L->Left, R->Right
Example:
URRRUU 21

EXPLANATION
Santa starts off at the bottom-left, taking 3 minutes to debug the first house's code. 
He should then move upwards, then right thrice, then upwards twice, taking a time of 21 minutes (3+5+3+1+4+2+3). He then reaches his target destination, the top-right corner.

BONUS
Of course, SoloCity isn't that conveniently structured. A debug time of 0 would represent an obstruction; Santa cannot move to that square under any circumstances.
Example Input:

[[1, 5, 4, 3],
 [4, 7, 0, 2],
 [5, 3, 1, 0],
 [3, 6, 4, 2]]

Start = 12, End = 3

The 0 tiles cannot be passed, so the optimal route has changed;
Example Output:
UUURRR 25

Oh, and that's not all. We must prepare for all circumstances, mustn't we? What if this happens?

Example Input 2:
[[1, 0, 4, 3],
 [4, 7, 0, 2],
 [5, 3, 1, 0],
 [3, 6, 4, 2]]
Start = 12, End = 3

Or this:
Example Input 3:
[[1, 5, 4, 0],
 [4, 7, 8, 2],
 [5, 3, 1, 4],
 [3, 6, 4, 2]]
Start = 12, End = 3

The horror! He cannot even reach the destination square now. What do we do, then?
Well, in this case you should return 0.

Example Output 2, 3:
0
0

ADDITIONAL TEST CASE (Contributed by @Cpasgrave)
[
[1, 1, 1, 9, 1, 1, 1, 1, 9, 9]
[1, 9, 1, 9, 2, 9, 9, 1, 9, 1]
[1, 9, 1, 1, 1, 1, 9, 1, 9, 1]
[1, 9, 9, 9, 9, 9, 9, 1, 1, 2]
[1, 9, 9, 9, 9, 9, 9, 9, 1, 1]
[1, 9, 9, 9, 9, 9, 9, 9, 9, 9]
[1, 3, 2, 1, 9, 9, 9, 9, 9, 9]
[1, 9, 9, 1, 9, 9, 9, 9, 9, 9]
[1, 9, 9, 1, 9, 9, 9, 9, 9, 9]
[1, 1, 2, 1, 9, 9, 9, 9, 9, 9]
[9, 9, 9, 2, 9, 2, 9, 9, 9, 9]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 5]]
Start : 111, End : 10

Output:
RRUULLLUUUUUUUU 18

COMMENTS
This is the hardest challenge thus far I have created (though it may not be hard. Well.)! Depending on your reactions, I may decide to come up with more challenging challenges. As always, good luck, and have fun coding!
😉
(I must really find a way for my wild imaginations to fit in a 512 character limit... *Sigh*.)
'''


from random import choice

# My answer to [Challenge] Santa Code's Christmas Conundrum by blackcat1111
# https://www.sololearn.com/Discuss/952423/challenge-santa-code-s-christmas-conundrum
# Description after code

# function creating random rectangle grid with definable max side length:
def create(max):
    H = choice( range(2, max+1))
    L = choice(range(2, max+1))
    S = E = choice(range(1, H*L+1))
    while E == S:
        E = choice(range(1, H*L))
    G = [] # G for grid
    for i in range (H):
        G.append([choice(range(0, 10)) for r in range(L)])
    return G, S, E


def findpath(G, S, E):  # G for Grid, S for Start, E for End
    Gh = len(G)                 # Grid Height
    Gl = len(G[0])              # Grid Length
    St = ((S)//Gl, (S)%Gl)  # Starting point (row, column)
    En = ((E)//Gl, (E)%Gl)  # Ending point (row, column)
    Sv = (G[St[0]][St[1]])      # Starting point value
    Ev = (G[En[0]][En[1]])      # Ending point Value
    Paths = [[]for i in range(Gh*Gl)]  # one sublist for each possible endpoint of possible paths
    Paths[S].append([St, Sv])  # Injecting startpoint to the Paths
    Tree = []       # Used to receive the finished paths (those that reached endpoint)

    # ----------------------------------------------------------
    # function returning the "next possible steps" from a point
    def nps(path):
        pos = path[-2]
        ns = [(pos[0]-1, pos[1]) if pos[0] > 0 else "",   # up
              (pos[0], pos[1]+1) if pos[1] < (Gl-1) else "",  # right
              (pos[0]+1, pos[1]) if pos[0] < (Gh-1) else "",  # down
              (pos[0], pos[1]-1) if pos[1] > 0 else ""]   # left
        for p in range(4):
            if ns[p] in path:  # makes it impossible to reach an already passed point
                ns[p] = ""
            if ns[p]:
                if G[ns[p][0]][ns[p][1]] == 0:  # situation of a 0 on the way
                    ns[p] = ""
        ns = list(filter(lambda x: x != "", ns))
        return ns

    # ------------------------------------------------------------
    # function sorting each group of paths reaching the same point
    # keeping only the one(s) with the lowest count
    def shake(paths):
        for i in range(len(paths)):
            if paths[i]:
                opt = min(p[-1] for p in paths[i])
                red = []
                for j in range(len(paths[i])):
                    if paths[i][j][-1] == opt:
                        red.append(paths[i][j])
                paths[i] = red
        return paths

    # ---------------------------------------------------
    # function giving the result in the asked string form
    def translate(path):
        URDL = ""
        for i in range(1, len(path)-1):
            if path[i][0] == path[i-1][0]-1: URDL += 'U'
            if path[i][1] == path[i-1][1]+1: URDL += 'R'
            if path[i][0] == path[i-1][0]+1: URDL += 'D'
            if path[i][1] == path[i-1][1]-1: URDL += 'L'
        return URDL

# ----------------------
# Here starts the Engine
# ----------------------

    if Sv == 0 or Ev == 0: return 0  # Situation when Start or End = 0
    while True:  # --> engine producing all the paths
        for m in Paths: # m for move (one from start to each square of the grid)
            for p in m:
                if p[-2] == En:  # moving finished paths to Tree (remove it from Paths at line 91)
                    Tree.append(p)
                else:
                    br = nps(p)  # br for branches
                    for b in br:
                        pa = list(p)
                        pa.insert(-1, b)  # adding the new step to each path
                        pa[-1] += G[b[0]][b[1]]  # updating total for new path
                        Paths[Gl * b[0] + b[1]].append(pa)  # and moving the path to the right "move" = grid square
                m.remove(p)
                
        Paths = shake(Paths) # Shaking the tree to remove long paths
        
        if all(len(m) == 0 for m in Paths):  # Stops when Paths is empty
            best = min(p[-1] for p in Tree)
            for p in Tree:
                if p[-1] == best:
                    print(translate(p), p[-1])
            break

# ------------
# My test Grid
# ------------
Grid = [
[1, 1, 1, 9, 1, 1, 1, 1, 9, 9],
[1, 9, 1, 9, 2, 9, 9, 1, 9, 1],
[1, 9, 1, 1, 1, 1, 9, 1, 9, 1],
[1, 9, 9, 9, 9, 9, 9, 1, 1, 2],
[1, 9, 9, 9, 9, 9, 9, 9, 1, 1],
[1, 9, 9, 9, 9, 9, 9, 9, 9, 9],
[1, 3, 2, 1, 9, 9, 9, 9, 9, 9],
[1, 9, 9, 1, 9, 9, 9, 9, 9, 9],
[1, 9, 9, 1, 9, 9, 9, 9, 9, 9],
[1, 1, 2, 1, 9, 9, 9, 9, 9, 9],
[9, 9, 9, 2, 9, 2, 9, 9, 9, 9],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 5]]
for r in Grid: print(r)
print("Start :", "110", "End :", "9")
findpath(Grid, 110, 9)

# ----------------
# Random test case
# -----------------
new_G = create(20)
for r in new_G[0]: print(r)
print("Start :", new_G[1],"End :", new_G[2])
findpath(new_G[0], new_G[1], new_G[2])

