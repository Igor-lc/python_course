from sys import argv
from decimal import Decimal as D
pn = D(argv[1]) - D(argv[2]) < 0

if pn:
    for i in range(int(D(argv[1]) * 10),  int(D(argv[2]) * 10) + 1, 1):
        print(i / 10, end=' ')
else:
    for i in range(int(D(argv[1]) * 10),  int(D(argv[2]) * 10) - 1, -1):
        print(i / 10, end=' ')
print()

# ver 2
start = float(argv[1])
end = float(argv[2])

if start > end:
    step = -1
    end = int(end * 10) - 1
else:
    step = 1
    end = int(end * 10) + 1

start = int(start * 10)

values = []
for value in range(start, end, step):
    values.append(str(value / 10))


print(" ".join(values))
