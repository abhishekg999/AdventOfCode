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

raw_data = open('input').read()
data = raw_data.strip().split('\n')

time = after_colon(data[0]).strip()
distance = after_colon(data[1]).strip()

while '  ' in time:
    time = time.replace('  ', ' ')

    
while '  ' in distance:
    distance = distance.replace('  ', ' ')

time = literal_eval(time.replace(' ', ','))
distance = literal_eval(distance.replace(' ', ','))

tots = []
for t,d in zip(time, distance):
    tot =  0
    for e in range(0, t):
        vel = e
        dist = e*(t-e)
        if dist >= d:
            tot += 1
    
    tots.append(tot)

print(prod(tots))
# Uncomment next two lines 
# from builtins import print
# print(answer)