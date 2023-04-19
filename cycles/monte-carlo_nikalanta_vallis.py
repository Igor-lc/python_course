from sys import argv
import random
n = int(argv[1])

# method Monte-Carlo
inside_the_circle = 0
for i in range(n):
    x = random.uniform(-1, 1)  # get a random floating point number in the range -1...1
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        inside_the_circle += 1

pi = 4 * inside_the_circle / n
print(pi)  # prints a different value every time



# Nikalanta row
pi, pn = 3, 1
for i in range(2, n*2 + 1, 2):
    pi += pn * (4 / (i * (i+1) * (i+2)))
    pn *= -1

print(round(pi, 5))  # 3.14159 - this is the most accurate method


# Vallis formula
pi = 1
for j in range(2, n * 2 + 1, 2):
    pi *= (j / (j - 1)) * (j / (j + 1))

print(round(pi * 2, 5))
