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

time = time.replace(' ','')
distance = distance.replace(' ','')


time = literal_eval(time)
distance = literal_eval(distance)


tot =  0
for e in range(0, time):
    vel = e
    dist = e*(time-e)
    if dist >= distance:
        tot += 1



print(tot)
# Uncomment next two lines 
# from builtins import print
# print(answer)