import sys
values = list(map(int, sys.argv[1:]))
index = 0
result = []


while values[index] is not None:

    result.append(str(values[index]))

    next_index = values[index]

    values[index] = None

    index = next_index


print(" ".join(result))


# ver 2
digits = list(map(int, sys.argv[1:]))
way = [digits[0]]

for i in way:
    if digits[i] not in way:
        way.append(digits[i])
    else:
        print(' '.join(list(map(str, way))))
        break
