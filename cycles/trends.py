from sys import argv
values = list(map(int, argv[1:]))

print(' '.join(['green' if j - values[i] > 0 else 'red' if j - values[i] < 0 else 'green' for i, j in enumerate(values[1:])]))


colors = ["green"]
for i, j in enumerate(values[1:], 1):
    if j > values[i-1]:
        colors.append("green")
    elif j < values[i-1]:
        colors.append("red")
    else:
        colors.append(colors[-1])

print(" ".join(colors))


colors = []
prev_value = float("-inf")
for value in values:
    value = int(value)
    if value > prev_value:
        colors.append("green")
    elif value < prev_value:
        colors.append("red")
    else:
        colors.append(colors[-1])

    prev_value = value

print(" ".join(colors))
