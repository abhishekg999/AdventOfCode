#from pprint import pprint as print
from multiset import Multiset
from functools import cache

data = open('input').read().split('\n')
data = [x[x.index(':')+2:].split(' | ') for x in data]

formatted = []
for line in data:
    lucky = [int(x) for x in line[0].split(' ') if x != '']
    guess = [int(x) for x in line[1].split(' ') if x != '']
    formatted.append([lucky, guess])

total = 0

@cache
def win(n):
    total = 1
    l, g = formatted[n]
    matches = len(Multiset(l).intersection(Multiset(g)))
    for i in range(n+1, n+1+matches):
        total += win(i)
    return total

from tqdm import tqdm
for i, (l, g) in tqdm(enumerate(formatted)):
    total += win(i)

print(total)