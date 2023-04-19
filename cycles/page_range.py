import sys

# ver 1
pages = []
for i in sys.argv[1].split(','):
    if '-' in i:
        a, b = i.split('-')
        pages += list(range(int(a), int(b) + 1))
    else:
        pages.append(int(i))

pages.sort()
pages = [pages[0]] + [j for i, j in enumerate(pages[1:]) if j != pages[i]]
print(*pages, sep=',')


# ver 2
pages = sys.argv[1]
pages_list = []

for element in pages.split(","):
    if element.isdigit():
        if int(element) not in pages_list:
            pages_list.append(int(element))
    else:
        start, end = element.split("-")
        for page in range(int(start), int(end) + 1):
            if page not in pages_list:
                pages_list.append(page)

pages_list.sort()
for i in range(len(pages_list)):
    pages_list[i] = str(pages_list[i])

print(",".join(pages_list))


