import os

print(os.getcwd())

os.chdir("/Users/gameg/OneDrive/Desktop")

for file in os.listdir():
    print(file)