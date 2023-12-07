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
    """
    Returns a function that takes a string, and returns the string
    after the character "char".
    """
    def inner(arr: str):
        """
        Returns a string from input string that starts after the specified character.
        """
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

def r_intersect(a: range, b: range):
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



tot = 0
for l in data:
    a, b = l.split(',')
    a_s, a_e = p_char_separated_integers(a, '-')
    b_s, b_e = p_char_separated_integers(b, '-')

    a = range(a_s, a_e+1)
    b = range(b_s, b_e+1)
    
    if r_intersect(a, b)[0] or r_intersect(a, b)[0]:
        tot += 1

    
print(tot)


# Uncomment next two lines 
# from builtins import print
# print(answer)