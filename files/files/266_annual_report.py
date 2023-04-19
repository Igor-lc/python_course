"""
266. ГОДОВОЙ ОТЧЕТ
Рядом с программой находятся 4 файла: q1.txt, q2.txt, q3.txt и q4.txt.
Каждый файл содержит целое число — квартальную прибыль компании.

Напишите программу, которая читает все квартальные отчеты, суммирует результат и сохраняет
его в файл year.txt.
"""


# main version 1
open("year.txt", "w").write(str(sum([int(open(f"q{i}.txt").read()) for i in range(1, 5)])))



# version 2
with open("q1.txt") as q1, open("q2.txt") as q2, open("q3.txt") as q3, open("q4.txt") as q4:
    f = int(q1.read()) + int(q2.read()) + int(q3.read()) + int(q4.read())

    with open("year.txt", "w") as file_year:
        print(f, file=file_year)
        print(f)
