G = 9.8


def ek(m, v):
    return (m * (v ** 2)) / 2


print(__name__)

if __name__ == "__main__":
    print("модуль запущен напрямую")
else:
    print("модуль импортирован")

if __name__ == "__main__":
    if ek(100, 10) != 5000:
        print("Ошибка в функции ek")
