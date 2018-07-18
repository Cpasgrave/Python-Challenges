# https://www.sololearn.com/Discuss/687816/assignment-hello-world
'''
[ASSIGNMENT] Hello World! by Dom Barter
Though this isn't technically a hard challenge just wanted to see how people did it. 
Create a piece of code that outputs "hello world" in the most silly and/or extensive way possible. I know this is vague but this is my intent - it's just a bit of fun!
All languages welcome.
'''
from itertools import permutations
from random import choice
from numpy.random import choice as choose

# This is my first Genetic Algorithm (if only it can be called so ... ?)
# The goal was to produce random genes and to crossover random pairs of the
# genes, also replacing one gene with a new random one, untill it would use
# the tools I fed it with, to write an 'Hello World' python code
# But it will also produce print(print)

# If you get a "Time limit exceeded", run it again
# If you copy it to your favorite IDE, you can add
# other things inside the tools list.
# By default, it will produce expressions of the same
# length as the tools list, but you can change it
# by writing the length you want as 'n' in evolve(n)
# n is the number of elements, you can have e.g.:
# a list of 4 tools and ask to write an expression 
# using those tools 7 times, or a list of 13 tools
# and ask the algo to write some code using 6 of the
# tools. Well, it's very easily going into infinite loops 
# enjoy (-:

# express function tries to express each gene in genes
def express(dic, genes, evol):
    phenotypes = []
    for gene in genes:
        phenotype = []
        for j in range(int(len(gene) / 3)):
            phenotype.append(dic[gene[0+3*j:3+3*j]])
        phenotypes.append(''.join(phenotype))
    for p in range(len(phenotypes)):
        try:
            evol += 1
            exp = exec(phenotypes[p])
            if exp is None:
                print('\nGene: ', genes[p], 'is functional.\nIt produces the code:\n--->', phenotypes[p])
                exec(phenotypes[p])
                print('\n',evol, 'dysfunctional genes have been created \nbefore finding this one')
                return 1
            else:
                print(genes[p],end='')
                return [0,evol]
        except:
            print(genes[p],end='')
            return [0,evol]


# Crossover function takes random pairs of genes and practice crossover between them
def crossover(genes):
    for g in range(int(len(genes) / 2)):
        cut = choice([i for i in range(len(genes[g]))])
        a, b = [choice(*[range(len(genes))]), choice(*[range(len(genes))])]
        genes[a] = genes[a][:cut] + genes[b][cut:]
        genes[b] = genes[b][:cut] + genes[a][cut:]
    return genes


# Newblood function randomly replaces one gene with a totally random new one
def newblood(genes,length,new=1):
    for n in range(new):
        a = choice(*[range(len(genes))])
        genes[a] = ''.join([choice('ATGC') for i in range(length)])
    return genes

# Mutation func randomly mutates 2% (or another chosen rate) of the total genepool bases 'ATGC'
def mutation(genes,rate=2):
    bases_num = len(genes)*len(genes[0])
    mut_num = sum([choose([0,1],p=[1-rate/100,rate/100]) for i in range(bases_num)])
    for mut in range(mut_num):
        gene = choice(*[range(len(genes))])
        cod = choice(*[range(len(genes[0]))])
        new = choice([i for i in ['A','T','G','C'] if i!=genes[gene][cod]])
        genes[gene]= genes[gene][:cod]+new+genes[gene][cod+1:]


# The main function : it's producin the tools, the dictionary,
# and runs the evolutionnary loop until something functional
# emerges.
def evolve(n=0):
    # The tools are the possible expression of the genes
    # Here the set of tools is reduced at minimum :
    tools = ['(', ')', '"Hello World"','print']
    length = n*3 or len(tools)*3
    # codons is a set of all possible codons made of three characters
    # taken from ATGC
    codons = {''.join(i) for i in permutations('AAATTTCCCGGG', 3)}

    # dictionary attributes a tool to each codon
    dic = {i: choice(tools) for i in codons}
    # genes is a gene pool of ten genes randomly created
    genes = [''.join([choice('ATGC') for i in range(length)]) for j in range(10)]
    evol = 0
    while True:
        test = express(dic, genes, evol)
        if test == 1:
            break
        else:
            newblood(genes,length)
            crossover(genes)
            mutation(genes)
            evol = test[1]

evolve()
