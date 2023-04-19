from sys import argv

revenue2023 = {
   "q1": 50,
   "q2": 200,
   "q3": 400,
   "q4": 300
}

data = argv[1].split(":")
revenue2023["q" + data[0]] = int(data[1])

q_percent = str(round(int(data[1]) * 100 / sum(revenue2023.values()), 1)) + "%"
print(q_percent)
