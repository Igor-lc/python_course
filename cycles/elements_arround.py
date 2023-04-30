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


'''317. SUM OF ELEMENTS AROUND
Difficulty: 7 out of 10

Next to the program is the data.txt file with the following content:

1 2 3 4 5 9
6 7 8 9 0 8
1 7 4 3 1 7
2 5 13 1 2 1
3 2 4 0 4 2
5 9 7 0 16 0
8 0 19 3 4 3
7 4 6 1 0 21

This is a regular NxM matrix with numbers.

Write a program that receives the row number and column number in the matrix from the command line arguments, then finds the element at the intersection of the passed coordinates, and then calculates the sum of the values of the elements around the found element. Numbers of elements in rows and columns should be counted from zero.

Calculation example. The program receives the values 1 (row) and 5 (column). According to the given coordinates, the number 8 is found. There are elements around it: 9, 5, 0, 1, 7. Their sum is 22 - this is the answer.

Usage example:
> python program.py 1 5
22'''
