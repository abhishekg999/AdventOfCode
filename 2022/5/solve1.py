from functools import cache
from collections import defaultdict, Counter, deque
from math import *
from ast import literal_eval
import sys, os
import re
import string


# Uncomment next line to disable prints
# print = lambda *x: ...

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

def gen_split_after(char: str):
    def inner(arr: str):
        return arr[arr.index(char) + len(char):].strip()
    return inner

a_colon = gen_split_after(':')

def g_every_n(arr: list, n: int):
    return zip(*(iter(arr),) * n)

def p_space_separated_integers(s: str):
    return [int(x) for x in s.strip().split()]

def p_comma_separated_integers(s: str):
    s = s.replace(',', ' ')
    return [int(x) for x in s.strip().split()]

def p_char_separated_integers(s: str, char: str):
    s = s.replace(char, ' ')
    return [int(x) for x in s.strip().split()]    

def r_intersect_difference(a: range, b: range):
    """
    Returns a range of the intersection, along with an array of ranges
    of parts of a that were not intersected by b.
    """
    if a.stop <= b.start or a.start >= b.stop:
        return None, []

    if (a.start >= b.start and a.stop <= b.stop):
        return range(a.start, a.stop), []

    if (b.start >= a.start and b.stop <= a.stop):
        return range(b.start, b.stop), [range(a.start, b.start), range(b.stop, a.stop)]

    if (a.start < b.start) and (a.stop+1 >= b.start):
        return range(b.start, a.stop), [range(a.start, b.start)]
    
    if (b.start < a.start) and (b.stop+1 >= a.start):
        return range(a.start, b.stop), [range(b.stop, a.stop)]

    raise Exception("pls")

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]
raw_data = open(input_file).read()
data = raw_data.strip().split('\n')



# Uncomment next two lines 
# from builtins import print
# print(answer)