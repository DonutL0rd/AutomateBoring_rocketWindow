import os
from pathlib import Path
print(os.getcwd())

os.chdir("/Users/gameg/OneDrive/Desktop/test_python_folder")

for file in os.listdir():
    f = Path(file)

    name, ext = f.stem, f.suffix
    file_name = name.replace(" ", "-")
    file_name = file_name.split("-")
    file_name = [s.strip() for s in file_name]
    new_name = '_'.join(file_name)
    os.rename(file, new_name)