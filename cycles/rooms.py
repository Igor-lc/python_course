from sys import argv

f, n = int(argv[1]), int(argv[2])
f_, n_ = 1, 1


rooms = ''
room = 11

while n_ <= n:
    rooms += str(n_) + str(f_) + ' '
    print(n_, f_, n, f)

    f_ += 1
    if f_ > f:
        n_ += 1
        f_ = 1

print(rooms.strip())
