import math
import re
import functools
import sys, os
from multiset import *
from icecream import ic
from collections import defaultdict

data = open('input').read().split('\n')

acc = Multiset({
    'red': 12,
    'green': 13,
    'blue': 14
})

def parse(arr):
    res = defaultdict(int)
    for x in arr:
        print(x.lstrip(' ').rstrip(' '))
        num, val = x.lstrip(' ').rstrip(' ').split(' ')
        res[val] += int(num)
    
    return Multiset(res)

tot = 0

for line in data:
    valid = True
    id = int(line[5:line.index(':')])
    games = [x.split(',') for x in line[line.index(':')+2:].split(';')]
    
    m = Multiset()
    for g in games:
        m = m.union(parse(g))
    
    tot += math.prod(m.multiplicities())
   
    
print(tot)