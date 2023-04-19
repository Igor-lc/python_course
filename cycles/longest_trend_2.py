import sys
trends = [int(i) for i in sys.argv[1].split()]
better_trends = [None] + [(-1 if curr < trends[i] else (0 if curr == trends[i] else 1)) for i, curr in enumerate(trends[1:])]


starts, ends = [], []
for i, curr in enumerate(better_trends[1:]):
    prev = better_trends[i]
    starts.append(i) if str(prev) in 'None-11' and prev != curr else None
    ends.append(i) if str(curr) in '-11' and prev != curr and i != 0 else None
ends.append(i + 1)


longest = []
for x, y in zip(starts, ends):
    if y + 1 - x > len(longest):
        longest = trends[x:y + 1]
print(*longest)
