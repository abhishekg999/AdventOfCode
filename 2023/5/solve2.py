from functools import cache
from collections import defaultdict, deque
from math import *
from ast import literal_eval

raw_data = open('input').read()
data = raw_data.split('\n')

def gen_split_after(char: str):
    def inner(arr):
        return arr[arr.index(char) + len(char):]
    return inner
after_colon = gen_split_after(':')

seeds = literal_eval(after_colon(data[0]).replace(' ', ',')[1:])

value_group = []
for d in raw_data.split('\n\n'):
    value_group.append(d.split('\n'))
value_group.pop(0)

def range_intersect(a: range, b: range):
    # no overlap
    if a.stop <= b.start or a.start >= b.stop:
        return None, []

    #full overlap (a inside b)
    if (a.start >= b.start and a.stop <= b.stop):
        return range(a.start, a.stop), []
    
    #full overlap (b inside a)
    if (b.start >= a.start and b.stop <= a.stop):
        return range(b.start, b.stop), [range(a.start, b.start), range(b.stop, a.stop)]
    
    #partial overlap (a < b):
    if (a.start < b.start) and (a.stop+1 >= b.start):
        return range(b.start, a.stop), [range(a.start, b.start)]
    
     #partial overlap (b < a):
    if (b.start < a.start) and (b.stop+1 >= a.start):
        return range(a.start, b.stop), [range(b.stop, a.stop)]
    
    raise Exception("pls")


class RangeElement:
    def __init__(self):
        self.src_base = []
        self.dst_base = []
        self._range = []
        self.src = []

    def add_range(self, dst, src, _range):
        self.src_base.append(src)
        self.dst_base.append(dst)
        self._range.append(_range)
        self.src.append(range(src, src+_range))

    def map(self, i):
        to_check = deque([i])
        while to_check:
            found = False
            i = to_check.popleft()    
            for range_el, dst, src in zip(self.src, self.dst_base, self.src_base):
                resp, rest = range_intersect(i, range_el)
                if resp:
                    delta = dst - src
                    found = True
                    yield range(resp.start+delta, resp.stop+delta)
                for r in rest:
                    to_check.append(r)
            if not found:
                yield i

    def __repr__(self):
        return f"RangeElement({self.dst_base}, {self.src_base}, {self._range})"

group_dicts = {}
keys = []
for group in value_group:
    src, _, dest = group[0][:-5].split('-')
    keys.append(src)
    group_dicts[src] = RangeElement()
    for line in group[1:]:
        _dst, _src, _range = literal_eval(line.replace(' ', ','))
        group_dicts[src].add_range(_dst, _src, _range)

final_mapping = []
seed_groups = [range(seeds[i], seeds[i+1]+seeds[i]) for i in range(0, len(seeds), 2)]

for seed in seed_groups:
    cur_vals = deque([seed])
    next_vals = []
    for key in keys:
        while cur_vals:
            cur = cur_vals.popleft()
            for x in group_dicts[key].map(cur):
                next_vals.append(x)  
        cur_vals = deque(next_vals)
        next_vals = []

    for v in cur_vals:
        final_mapping.append(v)

print(min([r.start for r in final_mapping]))