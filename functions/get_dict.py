def get_dict(text):
    dict = text.replace(":", "': '").replace(";", "', '")
    return "{'" + dict + "'}"


# print(get_dict("a:10;b:20;c:30"))


def get_dict2(text):
    dict = {}
    for i in text.split(";"):
        k, v = i.split(":")
        dict[k] = v
    return dict


# print(get_dict2("a:10;b:20;c:30"))

print("Модуль get_dict импортирован")
