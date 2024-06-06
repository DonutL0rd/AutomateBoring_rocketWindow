from cryptography.fernet import Fernet

# Generate the key
key = Fernet.generate_key()

# Save the key to a file
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)
