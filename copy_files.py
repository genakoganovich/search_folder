import os, shutil


class Names:
    FOLDER = "//192.168.20.237/e$/data/IsraelProject/__STORAGE__/"
    TARGET = "//192.168.20.237/e$/data/IsraelProject/__STORAGE__/tmp/"
    LINES_FILE = "IsraelProject_lines.txt"
    NOT_EXISTS = "//192.168.20.237/e$/data/IsraelProject/__STORAGE__/not_exists/"


def print_file_names(folder, file):
    with open(os.path.join(folder, file), "r") as lines_f:
        for line in lines_f:
            print(line.strip())


def find_startswith(folder, start, end):
    result = list()
    for path, currentDirectory, files in os.walk(folder):
        for file in files:
            if file.startswith(start) and file.endswith(end):
                result.append(os.path.join(path, file))
    return result


def create_if_not_exists(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)


def copy_file_to_folder(file, folder):
    shutil.copy(file, os.path.join(folder, os.path.basename(file)))


def test():
    create_if_not_exists(Names.NOT_EXISTS)


test()
