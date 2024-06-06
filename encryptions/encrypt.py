import os

from cryptography.fernet import Fernet
import shutil
from random import randint


def main():
    while True:
        print('__________MENU__________')
        print(f'1: Make file\n'
              f'2: Encrypt file and move to flash drive\n'
              f'3: Quit\n')
        ans = int(input('What would you like to do: '))
        if ans == 1:
            make_file()
        elif ans == 2:
            encrypt()
        elif ans == 3:
            break
        else:
            print('something went wrong')


def make_file():
    ans = input('what would you like to name the text file?\n')
    ans = ans+".txt"
    with open(ans, 'w') as file:
        for i in range(367):
            file.write(str(randint(10000, 100000000)) + '\n')
        file.flush()
        os.fsync(file)
        file.close()


def encrypt():


    with open("keyfile.key", 'rb') as filekey:
        key = filekey.read()

    global fernet
    fernet = Fernet(key)

    while True:
        file_name = input('Enter the file name and extension: ')
        try:
            with open(file_name, 'rb') as file:
                original = file.read()
                break
        except FileNotFoundError:
            print('ERROR... FILE NOT FOUND')
        except:
            print('ERROR... SOMETHING WENT WRONG')
            exit(-1)
    encrypted = fernet.encrypt(original)

    with open(file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

main()