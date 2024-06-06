from cryptography.fernet import Fernet

with open('keyfile.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

while True:
    message = input('Enter the file an extension you want to decrypt or 0 to quit: ')
    if message != "0":
        try:
            with open(message, 'rb') as enc_file:
                encrypted = enc_file.read()

            decrypted = fernet.decrypt(encrypted)

            with open(message, 'wb') as dec_file:
                dec_file.write(decrypted)
        except FileNotFoundError:
            print('File not found please try again')
        except:
            print('Something went wrong')
            exit(-1)
    elif message == "0":
        break
    else:
        print('someting bad happened')
        exit(-1)

