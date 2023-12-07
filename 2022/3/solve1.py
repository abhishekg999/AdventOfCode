from functools import cache
from collections import defaultdict
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


input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]
raw_data = open(input_file).read()
data = raw_data.strip().split('\n')

alphabet = string.ascii_lowercase + string.ascii_uppercase

total = 0
for line in data:
    a, b = line[:len(line)//2], line[len(line)//2:]
    dif = set(list(a)).intersection(set(list(b)))
    for c in dif:
        total += alphabet.index(c) + 1

print(total)
# Uncomment next two lines 
# from builtins import print
# print(answer)