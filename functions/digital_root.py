import sys
sys.setrecursionlimit(1000)
current_limit = sys.getrecursionlimit()
print("Поточн максимальна глибина рекурсії:", current_limit)

# I use recursion

def root(number):
    result = 0
    for i in str(number):
        result += int(i)
    if result < 10:
        return result
    return root(result)
print(root(95554651))

# ver2
def root2(number):
    result = 0
    while number > 0:
        result += number % 10
        number //= 10
    if result < 10:
        return result
    return root2(result)
print(root2(95554651))


# ver3
def root3(number):
    number = sum(map(int, list(str(number))))
    return (lambda x: root3(number), lambda x: number)[number < 10](number)
print(root3("95554651"))


# ver 4
def root4(number):
    number = sum(map(int, list(str(number))))
    return (lambda x: x if x < 10 else root(x))(number)
print(root4("95554651"))


def root5(number):
    number = sum(map(int, list(str(number))))
    return (root5(number), lambda x: number)[number < 10]
print(root5("95554651"))



# bad version:
def root6(number):
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

print(root6(95554651))

