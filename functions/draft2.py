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
print(pi)
