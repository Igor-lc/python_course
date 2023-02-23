'''ИЗМЕНЯЕМ ЗАГОЛОВОК
Рядом с программой находится HTML-файл с именем index.html. В файле есть различные теги, среди которых <h1>, который отвечает за основной
заголовок документа. Так случилось, что верстальщик добавил лишние пробелы в начале и конце основного заголовка.

Напишите программу, которая читает HTML-файл, а затем очищает от лишних пробелов текст основного заголовка, а также приводит его к верхнему
регистру. После всех преобразований, программа должна напечатать результат. Сами HTML-теги должны остаться без изменений.'''

# version 1
import re
with open("index.html", encoding="utf8") as html_file:
    html = html_file.read()
    text = re.sub(
        '<h1>(.*)</h1>',
        lambda x: "<h1>{}</h1>".format(x.group(1).upper().strip()),
        html)
    print(text)


# version 2
with open("index.html", encoding="utf8") as f:
    text = f.read()
    start_position = text.find("<h1>")
    end_position = text.find("</h1>") + 5

    old_text = text[start_position:end_position]

    text = text.replace(old_text, "<h1>" + old_text[4:-5].strip().upper() + "</h1>")
    print(text)


