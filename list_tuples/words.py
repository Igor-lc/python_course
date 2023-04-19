from sys import argv

words = ''.join(argv[1:]).split()
c = 0
for i in words:
    if i[0].isalpha():
        c += 1

print(c)
