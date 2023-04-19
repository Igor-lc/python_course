from sys import argv

skobki = list(filter(lambda x: x in "()", argv[1]))
print(skobki)


o = c = 0
for idx, i in enumerate(skobki, 1):
    if i == '(':
        o += 1
    else:
        c += 1
        if c > o:
            print('0')
            break
    print('1') if o == c and idx == len(skobki) else False
    print('0') if o != c and idx == len(skobki) else False

