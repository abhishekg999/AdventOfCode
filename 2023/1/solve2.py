import re

data = open("input").read().split("\n")

nums = "one,two,three,four,five,six,seven,eight,nine".split(",")
nmap = {}
for i, v in enumerate(nums):
    nmap[v] = str(i + 1)
    nmap[str(i + 1)] = str(i + 1)

g = f"({'|'.join(nmap.keys())})"
r = re.compile(f"^(?:.*?{g}.*{g}.*?)|(?:.*{g}.*)$")


def patch(s: str):
    g = re.match(r, s).groups()
    return int(nmap[g[0]] + nmap[g[1]]) if not g[2] else int(nmap[g[2]] * 2)


print(sum(patch(x) for x in data))

# 54706
