# I added a pre-treatment to VcC code to enable the treatment of much longer strings.
# Array split problem, pseudo polynomial solution  O(N*S) where S=sum of array, N=array size
# VcC 2017 implementing the dynamic programming algo
# https://en.wikipedia.org/wiki/Subset_sum_problem#Pseudo-polynomial_time_dynamic_programming_solution
cnv = " abcdefghijklmnopqrstuvwxyz"
let2num = lambda v: [cnv.index(x) for x in v]
num2let = lambda x: [cnv[a] for a in x]


def sumset(x, s, q={}):
    for i in range(len(x)):
        for j in range(1, s + 1):
            if x[i] == j:
                q[(i, j)] = (True, [j])
            elif i >= 1 and q[(i - 1, j)][0]:
                q[(i, j)] = (True, q[(i - 1, j)][1])
            elif i >= 1 and j >= x[i] and q[(i - 1, j - x[i])][0]:
                q[(i, j)] = (True, q[(i - 1, j - x[i])][1] + [x[i]])
            else:
                q[(i, j)] = (False, [])
        if q[(i, s)][0]:
            for k in q[(i, s)][1]:
                x.remove(k)
            return [q[(i, s)][1], x]
    return ([[], []])


guild = lambda v: (lambda x: (num2let(x[0]), num2let(x[1])))(sumset(let2num(v), sum(let2num(v)) // 2))

h = 'venezuelanbeavercheesetartinewithchampagnehoneyandcaviartoastsandcandlesonthetableandwhynotalittl' \
    'ebitofabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzeellenvenezuelanbeavercheesetartinewith' \
    'champagnehoneyandcaviartoastsandcandlesonthetableandwhynotalittlebitofabcdefghijklmnopqrstuvwxyza' \
    'bcdefghijklmnopqrstuvwxyzeellenvenezuelanbeavercheesetartinewithchampagnehoneyandcaviartoastsandc' \
    'andlesonthetableandwhynotalittlebitofabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzeellenve' \
    'nezuelanbeavercheesetartinewithchampagnehoneyandcaviartoastsandcandlesonthetableandwhynotalittleb' \
    'itofabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzeellenvenezuelanbeavercheesetartinewithch' \
    'ampagnehoneyandcaviartoastsandcandlesonthetableandwhynotalittlebitofabcdefghijklmnopqrstuvwxyzabc' \
    'defghijklmnopqrstuvwxyzeellenvenezuelanbeavercheesetartinewithchampagnehoneyandcaviartoastsandcan' \
    'dlesonthetableandwhynotalittlebitofabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzeellenvene' \
    'zuelanbeavercheesetartinewithchampagnehoneyandcaviartoastsandcandlesonthetableandwhynotalittlebit' \
    'ofabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzeellenvenezuelanbeavercheesetartinewithcham' \
    'pagnehoneyandcaviartoastsandcandlesonthetableandwhynotalittlebitofabcdefghijklmnopqrstuvwxyzabcde' \
    'fghijklmnopqrstuvwxyzeellenvenezuelanbeavercheesetartinewithchampagnehoneyandcaviartoastsandcandl' \
    'esonthetableandwhynotalittlebitofabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzeellentesque' \
    'venezuelanbeavercheesetartinewithchampagnehoneyandcaviartoastsandcandlesonthetableandwhynotalittl' \
    'ebitofabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzeellenvenezuelanbeavercheesetartinewith' \
    'champagnehoneyandcaviartoastsandcandlesonthetableandwhynotalittlebitofabcdefghijklmnopqrstuvwxyza' \
    'bcdefghijklmnopqrstuvwxyzeellenvenezuelanbeavercheesetartinewithchampagnehoneyandcaviartoastsandc' \
    'andlesonthetableandwhynotalittlebitofabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzeellenve' \
    'nezuelanbeavercheesetartinewithchampagnehoneyandcaviartoastsandcandlesonthetableandwhynotalittleb' \
    'itofabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzeellenvenezuelanbeavercheesetartinewithch' \
    'ampagnehoneyandcaviartoastsandcandlesonthetableandwhynotalittlebitofabcdefghijklmnopqrstuvwxyzabc' \
    'defghijklmnopqrstuvwxyzeellenvenezuelanbeavercheesetartinewithchampagnehoneyandcaviartoastsandcan' \
    'dlesonthetableandwhynotalittlebitofabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzeellenvene' \
    'zuelanbeavercheesetartinewithchampagnehoneyandcaviartoastsandcandlesonthetableandwhynotalittlebit' \
    'ofabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzeellenvenezuelanbeavercheesetartinewithcham' \
    'pagnehoneyandcaviartoastsandcandlesonthetableandwhynotalittlebitofabcdefghijklmnopqrstuvwxyzabcde' \
    'fghijklmnopqrstuvwxyzeellenvenezuelanbeavercheesetartinewithchampagnehoneyandcaviartoastsandcandl' \
    'esonthetableandwhynotalittlebitofabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzeellentesque' \
    'venezuelanbeavercheesetartinewithchampagnehoneyandcaviartoastsandcandlesonthetableandwhynotalittl' \
    'ebitofabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzeellenvenezuelanbeavercheesetartinewith' \
    'champagnehoneyandcaviartoastsandcandlesonthetableandwhynotalittlebitofabcdefghijklmnopqrstuvwxyza' \
    'bcdefghijklmnopqrstuvwxyzeellenvenezuelanbeavercheesetartinewithchampagnehoneyandcaviartoastsandc' \
    'andlesonthetableandwhynotalittlebitofabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzeellenve' \
    'nezuelanbeavercheesetartinewithchampagnehoneyandcaviartoastsandcandlesonthetableandwhynotalittleb' \
    'itofabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzeellenvenezuelanbeavercheesetartinewithch' \
    'ampagnehoneyandcaviartoastsandcandlesonthetableandwhynotalittlebitofabcdefghijklmnopqrstuvwxyzabc' \
    'defghijklmnopqrstuvwxyzeellenvenezuelanbeavercheesetartinewithchampagnehoneyandcaviartoastsandcan' \
    'itofabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzeellenvenezuelanbeavercheesetartinewithch' \

left = []
right = []
temp = list(h)
temp.sort()
if len(h) > 20 and len(set(h)) > 20:
    for i in range(0, len(temp) - 2, 2):
        l = temp[i]
        if temp[i + 2] == l:
            left.append(l)
            right.append(l)
    for c in left:
        temp.remove(c)
    for c in right:
        temp.remove(c)
    g = ''.join(temp)

print("total team number : ", len(h))
print("guild 1 : ")
print("(", sum(let2num(guild(g)[0] + left)), ")")
print("".join(guild(g)[0] + left))
print("guild 1 : ")
print("(", sum(let2num(guild(g)[1] + right)), ")")
print("".join(guild(g)[1] + right))
