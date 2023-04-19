def code(text, key=1):
    str_ = ''
    for i in text:
        shift = ord(i) + key
        str_ += chr(shift)
    return str_


text_007 = code("Агент 007, срочно выйдите на связь", 10)
print(text_007)
