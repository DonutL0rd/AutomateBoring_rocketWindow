import os
from cryptography.fernet import Fernet
import shutil
from random import randint


def main():
    while True:
        print('__________MENU__________')
        print(f'1: Make file\n'
              f'2: Encrypt file\n'
              f'3: Decrypt file\n'
              f'4: Quit\n')
        ans = int(input('What would you like to do: '))
        if ans == 1:
            make_file()
        elif ans == 2:
            encrypt()
        elif ans == 3:
            decrypt()
        elif ans == 4:
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


    with open("filekey.key", 'rb') as filekey:
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


def decrypt():
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    while True:
        message = input('Enter the file an extension you want to decrypt or 0 to quit: ')
        try:
            with open(message, 'rb') as enc_file:
                encrypted = enc_file.read()

            decrypted = fernet.decrypt(encrypted)

            with open(message, 'wb') as dec_file:
                dec_file.write(decrypted)

            break
        except FileNotFoundError:
            print('File not found please try again')
        except:
            print('Something went wrong')
            exit(-1)
main()