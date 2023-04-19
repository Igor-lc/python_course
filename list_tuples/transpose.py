with open("matrix.txt", encoding='utf8') as f:
    step = int(len(f.readline()) / 2)
    f.seek(0)
    f = f.read().split()

    for j in range(step):
        lst = []
        for i, x in enumerate(f[j:]):
            if not i % step:
                lst.append(x)

        with open("transpose_matrix.txt", 'a') as f2:
            print(*lst, file=f2)


# ver 2
matrix = [line.strip().split(" ") for line in open("matrix.txt").readlines()]
transpose_matrix = [[None] * len(matrix) for k in range(len(matrix[0]))]

for i, line in enumerate(matrix):
    for j, _ in enumerate(line):
        transpose_matrix[j][i] = matrix[i][j]

with open("transpose_matrix.txt", "w") as transpose_matrix_file:
    for line in transpose_matrix:
        print(" ".join(line), file=transpose_matrix_file)



# ver 3
matrix_file = open("matrix.txt", "r")
matrix = []

for line in matrix_file.readlines():
    matrix.append(line.strip().split(" "))

transpose_matrix = []
for k in range(matrix[0].__len__()):
    transpose_matrix.append([None] * matrix.__len__())

i = 0
for line in matrix:
    j = 0
    for col in line:
        transpose_matrix[j][i] = matrix[i][j]
        j += 1
    i += 1

transpose_matrix_file = open("transpose_matrix.txt", "w")
for line in transpose_matrix:
    transpose_matrix_file.write("{}\n".format(" ".join(line)))
transpose_matrix_file.close()

