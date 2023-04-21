import sys
sys.setrecursionlimit(1000)
current_limit = sys.getrecursionlimit()
print("Поточн максимальна глибина рекурсії:", current_limit)

# I use recursion
# ver 1
def root1(number):
    number = sum(map(int, list(str(number))))
    return (number < 10 and number) or root1(number)


# ver 2
def root2(number):
    number = sum(map(int, list(str(number))))
    return (root2, lambda x: x)[number < 10](number)


# ver 3
def root3(number):
    number = sum(map(int, list(str(number))))
    return (lambda x: x if x < 10 else root3(x))(number)


# ver 4
def root4(number):
    number = sum(map(int, list(str(number))))
    return (lambda x: root4(number), lambda x: number)[number < 10](number)


# ver 5
def root5(number):
    result = 0
    for i in str(number):
        result += int(i)
    if result < 10:
        return result
    return root5(result)


# ver 6
def root6(number):
    result = 0
    while number > 0:
        result += number % 10
        number //= 10
    if result < 10:
        return result
    return root6(result)


# bad version:
def root7(number):
    dr = 0
    for i in str(number):
        dr += int(i)
    if len(str(dr)) != 1:
        while True:
            s = 0
            for j in str(dr):
                s += int(j)
            if len(str(s)) == 1:
                return s
            else:
                dr = s
    else:
        return dr

print(root1(9999999))
print(root2(9999999))
print(root3(9999999))
print(root4(9999999))
print(root5(9999999))
print(root6(9999999))
print(root7(9999999))

