from functools import cache
from collections import defaultdict, Counter, deque
from multiset import Multiset
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
        return arr[arr.index(char) + len(char) :].strip()
    return inner
a_colon = gen_split_after(":")

############################################
# Functions involving Grouping 
############################################
def group_every_n(arr: list, n: int):
    return zip(*(iter(arr),) * n)

############################################
# Functions involving Graphs (g_) 
############################################
def g_shortest_path_to_all_from_source(G, start):
    ret = {start: 0}
    queue = deque([(0, start)])
    while queue:
        dist, node = queue.popleft()
        for neighbor in G[node]:
            if neighbor not in ret:
                queue.append((dist+1, neighbor))
                ret[neighbor] = dist+1
    return ret

############################################
# Functions for Parsing strings (p_)
############################################
def p_space_separated_integers(s: str):
    return [int(x) for x in s.strip().split()]

def p_comma_separated_integers(s: str):
    s = s.replace(",", " ")
    return [int(x) for x in s.strip().split()]

def p_char_separated_integers(s: str, char: str):
    s = s.replace(char, " ")
    return [int(x) for x in s.strip().split()]

############################################
# Functions involving Boards (b_)
# MUST HAVE height and width defined global
############################################
def b_get_neighbors(i, j):
    """
    Gets neighbors with wrap in an height x width board.
    height and width must be globally defined.
    """
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if (x, y) != (i, j) and x in range(0, height) and y in range(0, width):
                yield (x, y)

def b_modify_position(pos, dpos):
    i, j = pos
    di, dj = dpos
    return (i + di) % height, (j + dj) % width


############################################
# Functions involving ranges (r_)
# Uses python range object
############################################
def r_intersect(a: range, b: range):
    """
    Returns a range of the intersection, along with an array of ranges
    of parts of a that were not intersected by b.
    """
    if a.stop <= b.start or a.start >= b.stop:
        return None, [a]

    if a.start >= b.start and a.stop <= b.stop:
        return range(a.start, a.stop), []

    if b.start >= a.start and b.stop <= a.stop:
        return range(b.start, b.stop), [range(a.start, b.start), range(b.stop, a.stop)]

    if (a.start < b.start) and (a.stop + 1 >= b.start):
        return range(b.start, a.stop), [range(a.start, b.start)]

    if (b.start < a.start) and (b.stop + 1 >= a.start):
        return range(a.start, b.stop), [range(b.stop, a.stop)]

    raise Exception("pls")

############################################
# Functions involving matrices (m_)
############################################
def m_print(arr: list):
    for a in arr:
        print(a)

############################################
# Functions involving dictionaries (d_)
############################################
def d_print(dic: list):
    for k in dic:
        print(k, dic[k])

input_file = "input" if len(sys.argv) == 1 else sys.argv[1]
raw_data = open(input_file).read()
data = raw_data.strip().split("\n")

height = len(data)
width = len(data[0])


