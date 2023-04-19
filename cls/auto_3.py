class Auto:
    def __init__(self):
        self._number = []

    def get_number(self):
        print("Запуск get_number")
        return "".join(self._number).upper()

    def set_number(self, new_number):
        if new_number.__len__() != 8:
            print("Номер должен состоять из 8 символов")
        else:
            self._number = []
            for i in new_number:
                self._number.append(i)

    number = property(get_number, set_number)


auto1 = Auto()
auto1.number = "aa1111aa"
print("a1:", auto1.number)
