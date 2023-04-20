def root(number):
    # I use recursion
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
    return (root3(number), number)[number < 10]

print(root3("95554651"))


# bad version:
def root4(number):
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

print(root4(95554651))

