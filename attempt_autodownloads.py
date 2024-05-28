import os
from pathlib import Path

error_test = 2


def simplify_filenames():
    for file in os.listdir():
        f = Path(file)
        name, ext = f.stem, f.suffix
        file_name = name.replace(" ", "-") and name.replace("_", "-")
        file_name = file_name.split("-")
        file_name = [s.strip() for s in file_name]
        new_name = '_'.join(file_name)
        os.rename(file, new_name)
        print(f"changed {name} to {new_name}")


while error_test != 0:
    start_directory = input("enter the directory you want to simplify:")
    try:
        os.chdir(start_directory)
        print("worked!")
        simplify_filenames()
        error_test = 0
    except FileNotFoundError:
        print("not found please try again")
        error_test = 1





