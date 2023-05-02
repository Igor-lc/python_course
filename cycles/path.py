with open("table.txt", encoding='utf8') as f:
    p = f.read().strip()

dic = {}
for i, value in enumerate(p):
    if value == ':':
        dic[p[i - 1]] = p[i + 1]

value = dic['1']
path_ = ''
for k, v in reversed(dic.items()):
    if k == value:
        path_ += k
        value = dic[k]

print(', '.join(list(reversed(path_))) + ', 1')
