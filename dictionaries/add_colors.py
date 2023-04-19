import sys
from functools import reduce
args = sys.argv[1:]

colors = {
    "black": "черный",
    "white": "белый",
    "blue": "синий"
}


def update_color(dict, k, v):
    dict[k] = v


for i in range(0, len(args), 2):
    update_color(colors, args[i], args[i + 1])


print(', '.join(sorted(colors.keys())))
