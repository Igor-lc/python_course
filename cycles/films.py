from sys import argv


films = [i.split(',')[1] for i in open("films.txt", encoding='utf-8') if argv[1].casefold() in i.casefold()]
print('\n'.join(films))


def get_films(filename, search_query):
    with open(filename, encoding='utf-8') as f:
        return [line.strip().split(',')[1] for line in f if search_query.casefold() in line.casefold()]

if __name__ == '__main__':
    filename = 'films.txt'
    search_query = input('Введіть запит для пошуку: ')
    films = get_films(filename, search_query)
    print('\n'.join(films))
