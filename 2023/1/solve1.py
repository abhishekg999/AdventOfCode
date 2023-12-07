data = open('input').read().split("\n")
data = [''.join(c for c in x if c in '1234567890') for x in data]
print([(x[0] + x[-1]) for x in data])
print(sum(int(x[0] + x[-1]) for x in data))