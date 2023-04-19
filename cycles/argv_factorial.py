from sys import argv

for i in range(1, int(argv[1])):
    argv[1] = int(argv[1]) * i


print(argv[1])
