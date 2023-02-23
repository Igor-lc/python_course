def wellcome(name):
    mans = open("man.txt", encoding="utf8").read().split("\n")
    womans = open("woman.txt", encoding="utf8").read().split("\n")

    if (name in mans and name in womans) or (name not in mans and name not in womans):
        return f"Здравствуйте, {name}!"
    if name in mans:
        return f"Уважаемый {name}!"
    if name in womans:
        return f"Уважаемая {name}!"


print(wellcome("Python"))
