class Auto:

    def __init__(self):
        self.number = []

    def get_number(self):
        return "".join(self.number)

    def set_number(self, new_number):
        if new_number.__len__() != 8:
            print("Номер должен состоять из 8 символов")
        else:
            self._number = []
            for i in new_number:
                self.number.append(i)

    #number = property(set_number, get_number)


auto1 = Auto()
auto1.number = "aa1111aa"
print("a1:", auto1.number)
