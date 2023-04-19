from sys import argv
import sys
import re
from functools import reduce
text = ''.join(list(argv[1]))

'''for i in argv[1]:
    if i.isdigit():
        print(i, end='')


text = sys.argv[1]
codes = re.search(r"\d+", text)
if codes is not None:
    print(codes.group())
'''

def is_digit(j):
    return j.isdigit()

print(reduce(lambda x, y: (x) + (y), filter(is_digit, text)))
