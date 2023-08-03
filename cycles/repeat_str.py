import sys
N = int(sys.argv[1])
strings = sys.argv[1:]

res = []
i = 1
while i < len(strings):
    j = 1
    while j <= N:
        res.append(strings[i])
        j += 1
    i += 1

print(*res)


def multiplate(num, a):
    a = sys.argv[2:]
    N = int(sys.argv[1])
    string = ''
    for i in range(len(a)):
        string += N * (a[i] + ' ')
        i += 1
    return string

print(multiplate(sys.argv[1], sys.argv[2:]))