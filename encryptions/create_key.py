from cryptography.fernet import Fernet

# ______key_______#
key = Fernet.generate_key()

key_file_name = str(f'keyfile.key')

with open(key_file_name, 'wb') as filekey:
    filekey.write(key)

filekey.close()

