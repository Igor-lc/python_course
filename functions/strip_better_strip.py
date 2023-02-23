def strip(text):
    result = []
    for i, l in enumerate(text):
        if l == " " and text[i - 1] == " ":
            continue
        else:
            result.append(l)
    return "".join(result).strip()


def strip2(text):
    return " ".join(text.strip().split())


def strip3(text):
    result = list(text)
    s = 0  # для учета удаленных символов
    for i, _ in enumerate(result[1:]):
        if result[i - s] == " " and result[i - s - 1] == " ":
            del result[i - s]
            s += 1
    return ''.join(result).strip()


def strip4(text):
    result = list(text)
    for i, _ in enumerate(result[1:]):
        if result[i] == " " and result[i - 1] in (" ", None):
            result[i] = None
    return ''.join(filter(lambda x: x is not None, result)).strip()


print(strip("This is                a Code  "))
print(strip2("    This is        a Code  "))
print(strip3("     This is        a Code  "))
print(strip4("    This is        a Code  "))
