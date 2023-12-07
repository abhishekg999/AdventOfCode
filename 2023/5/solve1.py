from functools import cache
from collections import defaultdict
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
        for m, d, s in zip(self.src, self.dst_base, self.src_base):
            if i in m:
                return d + (i - s)
        return i
    
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

print(group_dicts)
final_mapping = []

for seed in seeds:
    cur_val = seed
    for key in keys:
        cur_val = group_dicts[key].map(cur_val)
    
    final_mapping.append(cur_val)

print(final_mapping)
print(min(final_mapping))
