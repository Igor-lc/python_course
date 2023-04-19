from sys import argv

with open("template.txt", "r+", encoding="cp1251") as f:
    data = f.read().replace("{{ name }}", argv[1])

with open("template.txt", "w", encoding="cp1251") as fi:
    print(data, file=fi, end='')
