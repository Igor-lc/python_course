from sys import argv
n = int(argv[1])

pi = 0
for j, i in enumerate(range(1, n * 2, 2)):
    if j & 1 == 1:
        pi -= 1 / i
    if j & 1 == 0:
        pi += 1 / i
print(round(pi * 4, 5))

pi = 0
zn = "+"
for i in range(1, n * 2, 2):
    if zn == "+":
        pi += + 1 / i
        zn = "-"
    else:
        pi -= 1 / i
        zn = "+"
print("{:.5f}".format(pi * 4))

pi = 0
zn = 1
for i in range(1, n * 2, 2):
    pi += zn * (1 / i)
    zn *= -1
print("{:.5f}".format(pi * 4))

pi = 0
for i in range(n):
    pi += ((-1) ** i) / (2 * i + 1)
print("{:.5f}".format(pi * 4))
