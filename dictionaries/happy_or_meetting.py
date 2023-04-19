def ticket_type(ticket):
    num = int(ticket)

    left_sum = num % 1000000 // 100000 + num % 100000 // 10000 + num % 10000 // 1000
    right_sum = num % 1000 // 100 + num % 100 // 10 + num % 10 // 1

    return {0: "счастливый", 1: "встречный", 2: "пьяный"}\
        .get(abs(left_sum - right_sum), "обычный")


result = ticket_type("123602")
print(result)
