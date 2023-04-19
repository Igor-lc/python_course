from sys import argv
import string
from functools import reduce
letters = list(argv[1])

u = list(filter(lambda letter: letter if letter in string.ascii_uppercase else False, letters))
l = list(filter(lambda letter: letter if letter in string.ascii_lowercase else False, letters))
print(reduce(lambda x, y: x + y, l + u))


lower_text = upper_text = ""
for c in letters:
    if c.islower():
        lower_text += c

    if c.isupper():
        upper_text += c

print(lower_text + upper_text)
