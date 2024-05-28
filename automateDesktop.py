import os
from pathlib import Path


def simplifyDir(dir):
    dir_name = dir.replace("\\", "-")
    dir_name = dir_name.replace("\"","")
    dir_name = dir_name.replace("C:", "")
    dir_name = dir_name.split("-")
    dir_output = "/".join(dir_name)
    return dir_output


def string_to_lower_list_with_spaces(input_string):
    result_list = []
    for char in input_string:
        if char.isupper():
            result_list.append(' ')
        result_list.append(char.lower())
    result_string = ''.join(result_list).strip()


def replace_with_underscore():
    name, ext = os.path.splitext(chosenDir)
    file_name = name.replace(" ", "-")
    file_name = file_name.split("-")
    file_name = [s.strip() for s in file_name]
    new_name = '_'.join(file_name)
    print(f"changed {name} to {new_name}")


chosenDir = input("Coppy directory path here\n")
chosenDir = simplifyDir(chosenDir)
os.chdir(chosenDir)

for file in os.listdir():
    replace_with_underscore()
