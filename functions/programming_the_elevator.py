def check_access(card, floor):
    with open("db.txt", encoding="utf8") as f:
        cf = f.readlines()
        for i in cf:
            c, f = i.split(";")
            if card == c:
                return floor == f[0]


def check_access2(card_number, floor):
    for card in open("db.txt", "r"):
        file_card_number, room = card.strip().split(";")
        file_floor = room[0]
        if card_number == file_card_number:
            return floor == file_floor
    return None


print(check_access("123456", "8"))
print(check_access2("123456", "88"))
