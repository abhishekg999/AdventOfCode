from functools import cache
from collections import defaultdict
from math import *
from ast import literal_eval
import sys, os
import re

# print = lambda *x: ...

def gen_split_after(char: str):
    def inner(arr: str):
        return arr[arr.index(char) + len(char):]
    return inner

after_colon = gen_split_after(':')

raw_data = open('sample').read()
data = raw_data.split('\n')

class Cell:
    def __init__(self, c):
        self.count = 1 if c in "<>^v" else 0

        self.directions = [c if c in '<>^v' else None]
        self.is_wall = True if c == '#' else False

    def __repr__(self) -> str:
        if self.is_wall:
            return '#'
        elif self.count == 0:
            return '.'
        elif self.count == 1:
            return self.directions[0]
        else:
            return str(self.count)     

    __str__ = __repr__   
            
        
map = [[Cell(y) for y in x] for x in data]
blizzard_pos = []

for i, row in enumerate(map):
    print(''.join([str(x) for x in row]))
