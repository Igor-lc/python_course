from sys import argv
digits = list(map(int, argv[1:]))

print(*list(filter(lambda d: str(d) if d < 0 else 0, digits)) + list(filter(lambda d: str(d) if d >= 0 else 0, digits)))


negative, postitve = [], []
for i in digits:
    if i < 0:
        negative.append(str(i))
    else:
        postitve.append(str(i))

print(" ".join(negative + postitve))
