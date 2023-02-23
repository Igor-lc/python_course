from sys import argv
user = argv[1]
pas = argv[2]

users = {
    "user1": "password1",
    "user2": "abcde",
    "user3": "123456",
    "user4": "lovelove",
    "user5": "kdmUdmk84M",
}

if users.get(user) is None:
    print("Пользователь не найден")
elif users.get(user) == pas:
    print("Доступ открыт")
else:
    print("Доступ закрыт")
