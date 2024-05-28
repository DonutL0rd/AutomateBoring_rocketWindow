import os


def simplify_dir(dir):
    dir_name = dir.replace("\\", "-")
    dir_name = dir_name.replace("\"", "")
    dir_name = dir_name.replace("C:", "")
    dir_name = dir_name.split("-")
    dir_output = "/".join(dir_name)
    return dir_output


def rename_files():
    res = []
    name, ext = os.path.splitext(file)
    for char in name:
        if char.isupper():
            res.append(' ')
        res.append(char.lower())
    file_name = ''.join(res).strip()
    file_name = file_name.replace(" ", "-")
    file_name = file_name.split("-")
    file_name = [s.strip() for s in file_name]
    new_name = '_'.join(file_name)
    print(f"changed {name} to {new_name + ext}")
    os.rename(file, new_name + ext)


chosenDir = input("Coppy directory path here\n")
chosenDir = simplify_dir(chosenDir)
os.chdir(chosenDir)

for file in os.listdir():
    rename_files()
