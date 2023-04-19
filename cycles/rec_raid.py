from sys import argv
data, step, text, f_num = '', int(argv[1]), argv[2], 0
files_list = []
for i in range(1, step + 1):
    files_list.append(open(f"data_-{i}.txt", "w+"))
# write
for i, c in enumerate(text):
    file_num = i % step
    file = files_list[file_num]
    file.write(c)

for file in files_list:
    file.close()


# ver ::step
txt = list(text)
for i in range(1, step+1, 1):
    with open(f"data_-{i}.txt", "w+", encoding="utf-8") as f:
        f.write((str("".join((txt[i-1::step])))))


# ver 2
while f_num < step:
    for i, j in enumerate(text):
        if i % step == f_num:
            data += j

    data, f_num = data + ';', f_num + 1
# ver 3
for f_num in range(step):
    substring = ''.join([char for index, char in zip(range(len(text)), text) if index % step == f_num])
    data += substring
    if f_num < step - 1:
        data += ';'
# ver 4
data = ';'.join([''.join([text[i] for i in range(len(text)) if i % step == j]) for j in range(step)])
# ver 5
data = ';'.join([''.join([j for i, j in enumerate(text) if i % step == k]) for k in range(step)])

# write
for i, j in enumerate(data.split(';'), 1):
    with open(f'data_-{i}.txt', 'w+', encoding='utf8') as f:
        print(j, file=f)
