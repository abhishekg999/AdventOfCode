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

raw_data = open('input').read()
data = raw_data.split('\n')


