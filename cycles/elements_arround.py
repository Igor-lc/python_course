import sys
# ver 1
row = int(sys.argv[1])
column = int(sys.argv[2])

WIDTH = 6
HEIGHT = 8
# Читаем файл и преобразуем в матрицу
matrix = []
data_file = open("data.txt", "r")
for line in data_file:
    # Заводим список для хранения элементов одной строки файла.
    line_list = []
    for number in line.split():
        line_list.append(int(number))
    # line_list = list(map(int, line.split()))
    matrix.append(line_list)

result = 0
if row - 1 >= 0:
    result += matrix[row - 1][column]
if (row - 1) >= 0 and (column - 1 >= 0):
    result += matrix[row - 1][column - 1]
if (row - 1) >= 0 and (column + 1 < WIDTH):
    result += matrix[row - 1][column + 1]
if column - 1 >= 0:
    result += matrix[row][column - 1]
if column + 1 < WIDTH:
    result += matrix[row][column + 1]
if row + 1 < HEIGHT:
    result += matrix[row + 1][column]
if (row + 1 < HEIGHT) and (column - 1 >= 0):
    result += matrix[row + 1][column - 1]
if (row + 1 < HEIGHT) and (column + 1 < WIDTH):
    result += matrix[row + 1][column + 1]
print(result)



# ver 2
r, c = int(sys.argv[1]), int(sys.argv[2])

with open("data.txt", encoding='utf8') as f:
    WIDTH = ALL = 0
    for column in f.readlines():
        ALL += len(column.split()); WIDTH = len(column.split())
    HEIGHT = ALL / WIDTH - 1

    f.seek(0)
    m = list(map(int, f.read().split()))
    f.seek(0)
    res = ids = 0
    for row_num, values in enumerate(f.readlines()):
        for column, value in enumerate(values.split()):
            if row_num == r and column == c:
                if 0 < row_num < HEIGHT and 0 < column < WIDTH - 1:
                    res += m[ids - 1]
                    res += m[ids + 1]
                    res += m[ids - 5]
                    res += m[ids - 6]
                    res += m[ids - 7]
                    res += m[ids + 5]
                    res += m[ids + 6]
                    res += m[ids + 7]
                if row_num == 0 and 0 < column < WIDTH - 1:
                    res += m[ids - 1]
                    res += m[ids + 1]
                    res += m[ids + 5]
                    res += m[ids + 6]
                    res += m[ids + 7]
                if row_num == HEIGHT and 0 < column < WIDTH - 1:
                    res += m[ids - 1]
                    res += m[ids + 1]
                    res += m[ids - 5]
                    res += m[ids - 6]
                    res += m[ids - 7]
                if 0 < row_num < HEIGHT and column == 0:
                    res += m[ids + 1]
                    res += m[ids + 6]
                    res += m[ids + 7]
                    res += m[ids - 5]
                    res += m[ids - 6]
                if 0 < row_num < HEIGHT and column == WIDTH - 1:
                    res += m[ids - 1]
                    res += m[ids - 6]
                    res += m[ids - 7]
                    res += m[ids + 5]
                    res += m[ids + 6]
                if row_num == 0 and column == 0:
                    res += m[ids + 1]
                    res += m[ids + 6]
                    res += m[ids + 7]
                if row_num == HEIGHT and column == 0:
                    res += m[ids + 1]
                    res += m[ids - 5]
                    res += m[ids - 6]
                if row_num == 0 and column == WIDTH - 1:
                    res += m[ids - 1]
                    res += m[ids + 5]
                    res += m[ids + 6]
                if row_num == HEIGHT and column == WIDTH - 1:
                    res += m[ids - 1]
                    res += m[ids - 6]
                    res += m[ids - 7]
            ids += 1
print(res)
