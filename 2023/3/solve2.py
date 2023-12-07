from pprint import pprint as print
import collections

data = open("input").read().split("\n")

height = len(data)
width = len(data[0])


def get_neighbors(i, j):
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if (x, y) != (i, j) and x in range(0, height) and y in range(0, width):
                yield (x, y)


class Num:
    def __init__(self, n):
        self.n = int(n)

    def __repr__(self):
        return str(self.n)


m = {}

cur_num = None

start_pos = None
in_num = False

for i, row in enumerate(data):
    for j, val in enumerate(row):
        if not in_num:
            if val in "0123456789":
                in_num = True
                start_pos = j
                cur_num = val

        else:
            if val in "0123456789":
                cur_num += val
            else:
                m[Num(cur_num)] = (i, start_pos, j)
                in_num = False
                cur_num = None
                start_pos = None

    if in_num:
        m[Num(cur_num)] = (i, start_pos, len(row))
        in_num = False
        cur_num = None
        start_pos = None


s = 0

gmap = collections.defaultdict(set)

for k in m:
    val = k.n
    row_index, start, end = m[k]

    valid = False
    i = row_index
    for j in range(start, end):
        for x, y in get_neighbors(i, j):
            if data[x][y] == "*":
                gmap[(x, y)].add(k)


s = 0
for k in gmap:
    if len(gmap[k]) == 2:
        a, b = gmap[k]
        s += a.n * b.n

print(gmap)
print(s)