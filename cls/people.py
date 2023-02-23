class People:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name.lower()

class Man(People):
    def get_sex(self):
        return "m"

class Woman(People):
    def get_sex(self):
        return "w"



# Версия 2 с созданием атрибута sex
class People:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name.lower()


class Man(People):
    def __init__(self, name):
        # Переопределяем __init__, но с вызовом родительского __init__
        # с помощью super и передачей name.
        super().__init__(name)
        self.sex = 'm'

    def get_sex(self):
        return self.sex


class Woman(People):
    def __init__(self, name):
        super().__init__(name)
        self.sex = 'w'

    def get_sex(self):
        return self.sex
