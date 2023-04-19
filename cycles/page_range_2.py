import sys
# ver 3
pages = sys.argv[1]
pages_list = []

for element in pages.split(","):
    if element.isdigit():
        pages_list.append(int(element))
    else:
        start, end = element.split("-")
        pages_list.extend(list(range(int(start), int(end) + 1)))

pages_list = list(set(pages_list))
pages_list.sort()

for i, _ in enumerate(pages_list):
    pages_list[i] = str(pages_list[i])

print(",".join(pages_list))

# ver 4
pages = sys.argv[1]
pages_dict = {}
for element in pages.split(","):
    if element.isdigit():
        pages_dict[int(element)] = True
    else:
        start, end = element.split("-")
        for page in range(int(start), int(end) + 1):
            pages_dict[page] = True

pages_list = sorted(pages_dict.keys())
for i in range(len(pages_list)):
    pages_list[i] = str(pages_list[i])

print(",".join(pages_list))
