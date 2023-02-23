from sys import argv

quarters = {
    "quarter_1": [137, 565, 145],
    "quarter_2": [145, 738, 1145],
    "quarter_3": [1345, 1141, 879],
    "quarter_4": [784, 689, 543]
}
print(sum(quarters[list(quarters)[int(argv[1]) - 1]]))


quarters = {
    "quarter_1": [137, 565, 145],
    "quarter_2": [145, 738, 1145],
    "quarter_3": [1345, 1141, 879],
    "quarter_4": [784, 689, 543]
}

data = quarters[f"quarter_{argv[1]}"]
print(sum(data))
