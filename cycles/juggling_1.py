import sys
list_num = [int(x) for x in sys.argv[1:]]
result = []
result.append(list_num[0])

for i in range(1, len(list_num)):
    if result[0] == list_num[result[0]]:
        break
    elif list_num[result[i-1]] in result:
        result.append(list_num[result[i - 1]])
        break
    else:
        result.append(list_num[result[i - 1]])

print(*result)


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



'''305. INDEX JUGGLING
Difficulty: 4 out of 10
Write a program that takes an arbitrary number of elements from the command line arguments, and then, starting from the first element, iterates over the remaining elements as described below.

Each element of the list contains the index of the next element to be visited.
So, for example, in the list [2, 0, 1], the first element contains the number 2, which means that the next element has an index of 2 and the program should go to it.

The element with index 2 contains one, which means that after it the program should go to position 1, where 0 is located, and so on.

As it traverses the list, the program must remember the values contained in the cells in the order in which it traverses them. So for the list above, the traversal path would be [0, 2, 1].

If, during the traversal process, the program hits an element that it has already visited, then it should interrupt the work and print the path that has been traveled so far. For example, for the list [2, 0, 1, 2] the path would be [2, 1, 0]

The distance traveled must be output as numbers separated by spaces.

Examples of using:
> python program.py 2 5 4 0 1 6 3
> 2 4 1 5 6 3 0

> python program.py 0 1 2 3 4 5 6
> 0

> python program.py 1 2 3 4 5 6 0
> 1 2 3 4 5 6 0

> python program.py 5 6 5 2 1 3 0
> 5 3 2 5'''