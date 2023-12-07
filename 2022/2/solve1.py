from functools import cache
from collections import defaultdict
from math import *
from ast import literal_eval
import sys, os
import re

# Uncomment next line to disable prints
# print = lambda *x: ...

def gen_split_after(char: str):
    def inner(arr: str):
        return arr[arr.index(char) + len(char):]
    return inner
after_colon = gen_split_after(':')

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]
raw_data = open(input_file).read()
data = raw_data.strip().split('\n')

o = 'ABC'
m = 'XYZ'

t = 0
for _t in data:
    x, y = _t.split(' ')
    t += m.index(y) + 1
    if (m.index(y) + 0) % 3 == o.index(x):
        t += 3
    if (m.index(y) + 1) % 3 == o.index(x):
        t += 6
    if (m.index(y) + 2) % 3 == o.index(x):
        pass

print(t)


# Uncomment next two lines 
# from builtins import print
# print(answer)