from sys import argv

for j in range(1, int(argv[1]) + 1):
    result = ''
    if j % 3 == 0:
        result += 'Fizz'
    if j % 5 == 0:
        result += 'Buzz'
    if not result:
        result = j
    print(result)
