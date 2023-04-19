from sys import argv
args = [int(i) for i in argv[1].split()]
print(max(args), end=' ')
for i in args:
    if i != max(args):
        print(i, end=' ')
