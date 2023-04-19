from sys import argv
argv = list(map(int, argv[1:]))

args = [(argv[0], 0)]
prev = argv[0]

for i in args:
    for idx, j in enumerate(argv[1:], 1):

        if argv[i[0]] == j and prev == idx:
            if (j, idx) in args:
                break
            args.append((j, idx))
            prev = j

print(*[i[0] for i in args])


# ver 2
visited = [(argv[0], 0)]
prev_i = curr_i = argv[0]


for _ in range(len(argv)):
    for i, next_i in enumerate(argv[1:], 1):

        if argv[visited[-1][0]] == next_i:
            if (next_i, i) in visited:
                break

            visited.append((next_i, i))
            prev_i = next_i
        curr_i = next_i

print(*[i[0] for i in visited])
