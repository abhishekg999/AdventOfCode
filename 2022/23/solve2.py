from functools import cache
from collections import defaultdict, Counter, deque
from math import *
from ast import literal_eval
import sys, os
import re
import string


# Uncomment next line to disable prints
print = lambda *x: ...

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase


def gen_split_after(char: str):
    def inner(arr: str):
        return arr[arr.index(char) + len(char) :].strip()
    return inner
a_colon = gen_split_after(":")

############################################
# Functions involving Grouping (g_)
############################################
def g_every_n(arr: list, n: int):
    return zip(*(iter(arr),) * n)

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
        return None, []

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
    if isinstance(arr[0], str):
        for a in arr:
            print(a)
    elif isinstance(arr[0], list) and isinstance(arr[0][0], str):
        for a in arr:
            print("".join(a))
    else:
        for a in arr:
            print(a)


input_file = "input" if len(sys.argv) == 1 else sys.argv[1]
raw_data = open(input_file).read()
data = raw_data.strip().split("\n")


class Elf:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.delta_groups = []
        self.delta_groups.append([(-1, 0), (-1, -1), (-1, 1)])
        self.delta_groups.append([(1, 0), (1, -1), (1, 1)])
        self.delta_groups.append([(0, -1), (1, -1), (-1, -1)])
        self.delta_groups.append([(0, 1), (1, 1), (-1, 1)])

    def propose(self):
        if not any(board[i, j] in elfs for i, j in b_get_neighbors(self.x, self.y)):
            pass
        else:
            for deltas in self.delta_groups:
                if any(board[b_modify_position((self.x, self.y), d)] for d in deltas):
                    continue

                proposals[b_modify_position((self.x, self.y), deltas[0])].append(self)
                print(f"ELF at ({self.x}, {self.y}) proposing to move to {b_modify_position((self.x, self.y), deltas[0])}")
                break

        self.delta_groups = self.delta_groups[1:] + self.delta_groups[:1]

    def execute(self, pos):
        del board[(self.x, self.y)]
        board[pos] = self
        self.x, self.y = pos
        moved.append(self)

moved = []

elfs = []
proposals = defaultdict(list)
board = defaultdict(lambda: None)

height = len(data)
width = len(data[0])


dist = max(width, height) * 2

pre_post = ["." * (width + 2*dist) for _ in range(dist)]
data = ["." * dist + x + "." * dist for x in data]

data = pre_post + data + pre_post
m_print(data)

height = len(data)
width = len(data[0])

for i, row in enumerate(data):
    for j, col in enumerate(row):
        if col == "#":
            e = Elf(i, j)
            elfs.append(e)
            board[(i, j)] = e

round = 0
while 1:
    round += 1
    for e in elfs:
        e.propose()

    for p in proposals:
        print(proposals[p])
        if len(proposals[p]) == 1:
            proposals[p][0].execute(p)

    proposals = defaultdict(list)

    if len(moved) == 0:
        from builtins import print
        print(round)
        sys.exit(0)
    
    moved = []


# Uncomment next two lines
from builtins import print

min_x, min_y = float("inf"), float("inf")
max_x, max_y = -1, -1
for e in elfs:
    print(e.x, e.y)
    min_x = min(min_x, e.x)
    min_y = min(min_y, e.y)
    max_x = max(max_x, e.x)
    max_y = max(max_y, e.y)

print(min_x, max_x)
print(min_y, max_y)

tot = 0
for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        if not board[x,y]:
            tot += 1

print(tot)
