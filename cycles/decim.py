from sys import argv
from decimal import Decimal as D

iteration_count = int((float(argv[2]) - float(argv[1])) * 10) + 1
new, j = [], D(argv[1])

for i in range(iteration_count):
    new.append(j.quantize(D('1.0')))
    j += D(0.1)

print(*new)



# ver 2
start = float(argv[1])
end = float(argv[2])

start = int(start * 10)
end = int(end * 10) + 1

values = []
for value in range(start, end):
    values.append(str(value / 10))

print(" ".join(values))
