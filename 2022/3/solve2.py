from functools import cache
from collections import defaultdict, Counter, deque
from math import *
from ast import literal_eval
import sys, os
import re
import string


# Uncomment next line to disable prints
# print = lambda *x: ...

def gen_split_after(char: str):
    def inner(arr: str):
        return arr[arr.index(char) + len(char):]
    return inner
after_colon = gen_split_after(':')

def group_every_n(arr: list, n: int):
    return zip(*(iter(arr),) * n)

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]
raw_data = open(input_file).read()
data = raw_data.strip().split('\n')

alphabet = string.ascii_lowercase + string.ascii_uppercase

total = 0
for g in group_every_n(data, 3):
    a, b, c = g
    res = set(a).intersection(set(b)).intersection(set(c))
    print(res)
    total += alphabet.index(list(res)[0])+1
    print(total)

print(total)
# Uncomment next two lines 
# from builtins import print
# print(answer)