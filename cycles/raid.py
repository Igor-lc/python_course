import sys

# ver 1
files_count, chars_count, files_data = int(sys.argv[1]), int(sys.argv[2]), []
for f in range(1, files_count + 1):
    files_data.append(open(f"data-{f}.txt", "r", encoding='utf8').read())
print(files_data)

char, data, i = 0, "", 0
while char < chars_count:
    for file in files_data:
        if char == chars_count:
            break
        data += file[i]
        char += 1
    i += 1
print(data)

# ver 2. И ее сновная опасность - многократное открытие и чтение файлов, это может нагрузить систему.
files, symbols, text, file_num, symbol = int(sys.argv[1]), int(sys.argv[2]), '', 1, 0

while 1:
    for i in open(f'data-{file_num}.txt', encoding='utf8').read()[symbol]:
        text += i
        if not file_num % files:
            file_num = 1
            symbol += 1
        else:
            file_num += 1
    if symbols == len(text):
        break
print(text)
