#from pprint import pprint as print
from multiset import Multiset

data = open('input').read().split('\n')
data = [x[x.index(':')+2:].split(' | ') for x in data]

formatted = []
for line in data:
    lucky = [int(x) for x in line[0].split(' ') if x != '']
    guess = [int(x) for x in line[1].split(' ') if x != '']
    formatted.append([lucky, guess])

total = 0
for l, g in formatted:
    exp = len(Multiset(l).intersection(Multiset(g)))
    if exp:
        val = pow(2, exp-1)
        total += val

print(total)