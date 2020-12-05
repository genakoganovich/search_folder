import os, shutil

# 1. read LINES_FILE that contains list of line names and create a LINES list
# 2. in the SOURCE folder find all the SGY_FILES that start with "LINE_NAME__stack__" and end with ".sgy"
# for each LINE_NAME from the LINES list
# 3. in the TARGET folder create a folder with name LINE_NAME if not exists for each LINE_NAME from LINES list
# 4. copy the found SGY_FILES from SOURCE folder to TARGET folder for each LINE_NAME to its own LINE_NAME folder


class Names:
    SOURCE = "//192.168.20.237/e$/data/IsraelProject/__STORAGE__/"
    TARGET = "//192.168.20.237/e$/data/IsraelProject/__STORAGE__/tmp/"
    LINES_FILE = "IsraelProject_lines.txt"
    NOT_EXISTS = "//192.168.20.237/e$/data/IsraelProject/__STORAGE__/not_exists/"


def create_lines_collection(folder, lines_file):
    lines_collection = list()
    with open(os.path.join(folder, lines_file), "r") as lines_f:
        for line in lines_f:
            lines_collection.append(line.strip())
    return lines_collection


def find_sgy_files_startswith(source_folder, start, end):
    sgy_files = list()
    for path, currentDirectory, files in os.walk(source_folder):
        for file in files:
            if file.startswith(start) and file.endswith(end):
                sgy_files.append(os.path.join(path, file))
    return sgy_files


def create_if_not_exists(full_name_line_folder):
    if not os.path.exists(full_name_line_folder):
        os.mkdir(full_name_line_folder)


def copy_file_to_target_folder(full_name_file, target_folder):
    shutil.copy(full_name_file, os.path.join(target_folder, os.path.basename(full_name_file)))


def create_folder_if_not_exists_and_copy_sgy_files(target_folder, line, sgy_files):
    line_folder = os.path.join(target_folder, line)
    create_if_not_exists(os.path.join(target_folder, line))
    for sgy_file in sgy_files:
        copy_file_to_target_folder(sgy_file, line_folder)


def run(source_folder, target_folder, lines_file):
    for line in create_lines_collection(source_folder, lines_file):
        sgy_files = find_sgy_files_startswith(source_folder, line + "__stack__", ".sgy")
        create_folder_if_not_exists_and_copy_sgy_files(target_folder, line, sgy_files)


def test():
    run(Names.SOURCE, Names.TARGET, Names.LINES_FILE)


test()
