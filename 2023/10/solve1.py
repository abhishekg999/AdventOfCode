from functools import cache
from collections import defaultdict, Counter, deque
from multiset import Multiset
from math import *
from ast import literal_eval
import sys, os
import re
import string
import inspect

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase


def gen_split_after(char: str):
    def inner(arr: str):
        return arr[arr.index(char) + len(char) :].strip()
    return inner
a_colon = gen_split_after(":")

############################################
# Postfix (then)
############################################
class CustomOperator:
    def __init__(self, callback):
        self.callback = callback
    def __rmatmul__(self, other):
        return CustomOperator.I(self, other)
    class I:
        def __init__(self, parent, value):
            self.parent = parent
            self.value = value
        def __matmul__(self, other):
            return self.parent.callback(self.value, other)

# 123 @then@ print
# Result: prints 123  
@CustomOperator
def then(val, func):
    return func(val)
t = then

# 123 @store@ 'asdf'
# print(asdf)
# Result: prints 123
@CustomOperator
def store(val, key):
    globals()[key] = val
    return val
s = store

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

def g_build_graph_from_2d_array_of_key_and_list_of_edges(arr):
    G = {}
    for k, v in arr:
        G[k] = v
    return G


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
def m_print(arr: list, format=lambda id: id):
    for a in arr:
        print(format(a))

############################################
# Functions involving dictionaries (d_)
############################################
def d_print(dic: list):
    for k in dic:
        print(k, dic[k])

############################################
# Infinite iterator
############################################
from typing import Iterable
def inf_iter(a: Iterable):
    while 1: yield from a


############################################
# SETUP
############################################

# Uncomment next line to disable prints
# print = lambda *x: ...

input_file = "input" if len(sys.argv) == 1 else sys.argv[1]
raw_data = open(input_file).read()
data = raw_data.strip().split("\n")

height = len(data)
width = len(data[0])

############################################
# Your Code
############################################

top_vert = "|7FS"
bot_vert = "|JLS"
left_hor = "-LFS"
righ_hor = "-J7S"


def b_modify_position(i, j):
    if ((i) % height, (j) % width) != ((i), (j)):
        return 'X'
    return data[(i)][(j)]


def validate(i, j):
    match data[i][j]:
        case '|':
            return b_modify_position(i-1, j) in top_vert and b_modify_position(i+1, j) in bot_vert
        case '-':
            return b_modify_position(i, j+1) in righ_hor and b_modify_position(i, j-1) in left_hor 
        case 'L':
            return b_modify_position(i-1, j) in top_vert and b_modify_position(i, j+1) in righ_hor 
        case 'J':
            return b_modify_position(i-1, j) in top_vert and b_modify_position(i, j-1) in left_hor 
        case '7':
            return b_modify_position(i+1, j) in bot_vert and b_modify_position(i, j-1) in left_hor 
        case 'F':
            return b_modify_position(i+1, j) in bot_vert and b_modify_position(i, j+1) in righ_hor
        case 'S':
            return True
        case '.':
            return None 

def valid_move(i, j, ni, nj):
    match data[i][j]:
        case '|':
            if (ni, nj) == (i-1, j) and b_modify_position(i-1, j) in top_vert:
                return True
            if (ni, nj) == (i+1, j) and b_modify_position(i+1, j) in bot_vert:
                return True
            return False
        case '-':
            if (ni, nj) == (i, j+1) and b_modify_position(i, j+1) in righ_hor:
                return True
            if (ni, nj) == (i, j-1) and b_modify_position(i, j-1) in left_hor:
                return True
            return False
        case 'L':
            if (ni, nj) == (i-1, j) and b_modify_position(i-1, j) in top_vert:
                return True
            if (ni, nj) == (i, j+1) and b_modify_position(i, j+1) in righ_hor:
                return True
            return False
        case 'J':
            if (ni, nj) == (i-1, j) and b_modify_position(i-1, j) in top_vert:
                return True
            if (ni, nj) == (i, j-1) and b_modify_position(i, j-1) in left_hor:
                return True
            return False
        case '7':
            if (ni, nj) == (i+1, j) and b_modify_position(i+1, j) in bot_vert:
                return True
            if (ni, nj) == (i, j-1) and b_modify_position(i, j-1) in left_hor:
                return True
            return False
        case 'F':
            if (ni, nj) == (i+1, j) and b_modify_position(i+1, j) in bot_vert:
                return True
            if (ni, nj) == (i, j+1) and b_modify_position(i, j+1) in righ_hor:
                return True
            return False
        case 'S':
            return True
        case '.':
            return None     

grid = []

for i, row in enumerate(data):
    cur = []
    for j, val in enumerate(row):
        if val == 'S':
            start = i, j
        cur.append(validate(i, j).__str__()[0])
    grid.append(cur)

m_print(data)
m_print(grid)



queue = deque([])
queue.append((start, 0, False))

distance = -1
another_map = [['.' for _ in range(width)] for _ in range(height)]
seen = set()
while queue:
    (i, j), distance, come_from = queue.popleft()
    # print(f"Now at {i},{j}, {come_from} = {data[i][j]}")
    seen.add((i, j))
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for (dx, dy) in delta:
        ni, nj = i+dx, j+dy
        if valid_move(i, j, ni, nj):
            if data[ni][nj] == 'S' and not come_from:
                print((distance+1) // 2)
                break
            
            if (ni, nj) in seen:
                continue
            
            queue.append(((ni, nj), distance+1, True if data[i][j] == 'S' else False))
            break



for i, j in seen:
    another_map[i][j] = '#'


m_print(another_map, lambda r: "".join(r))