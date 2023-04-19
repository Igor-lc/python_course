from os import path, makedirs, chdir
from datetime import datetime as dt
from sys import argv

filename = None  # responsible for creating a file
dirs = None  # responsible for creating catalogs
f_dir = input("Enter a filename and directory as here '-f filename.txt -d DirOne dirTwo': ")
argv.extend(f_dir.split())


for idx, arg in enumerate(argv[:-1]):
    next_arg = argv[idx + 1]
    if arg == "-f":
        filename = next_arg
    if arg == "-d":
        dirs = next_arg + "/"
        continue
    if dirs and arg != "-f" and next_arg != "-f":
        dirs += next_arg + "/"


if filename:
    start_now = dt.now().strftime('%d-%m-%Y %H:%M:%S') + '\n'
    try:
        if dirs:
            makedirs(dirs) if not path.exists(dirs) else False
            chdir(dirs)
        with open(filename, "a", encoding="utf-8") as f:
            data, i = '', 1
            while True:
                line = input("Enter content line: ")
                if line == "stop":
                    now = dt.now().strftime('%d-%m-%Y %H:%M:%S')
                    print(start_now + now + '\n' + data, file=f)
                    break
                data += str(i) + ' ' + line + '\n'
                i += 1
    except (PermissionError, NotADirectoryError):
        print("File system limitation. Please use a different name or use: my_task.txt or my_task.py")



# ver 2
import argparse
import os
from datetime import datetime as dt


def create_file(filename, directory):
    try:
        if directory:
            os.makedirs(directory, exist_ok=True)
            os.chdir(directory)
        with open(filename, "a", encoding="utf-8") as f:
            return f
    except (PermissionError, NotADirectoryError):
        print("File system limitation. Please use a different name or use: my_task.txt or my_task.py")
        return None


def add_content(file):
    i = 1
    data = ''
    start = dt.now()
    start_now = dt.now().strftime('%d-%m-%Y %H:%M:%S') + '\n'
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            end = dt.now()
            now = dt.now().strftime('%d-%m-%Y %H:%M:%S')
            print(start_now + now, (end - start), '\n' + data, file=file)
            break
        data += str(i) + ' ' + line + '\n'
        i += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a file and add content to it.')
    parser.add_argument('-f', '--filename', type=str, required=True, help='the name of the file to create')
    parser.add_argument('-d', '--directory', type=str, default='', help='the directory to create the file in')
    args = parser.parse_args()

    file = create_file(args.filename, args.directory)
    if file:
        add_content(file)
        file.close()
