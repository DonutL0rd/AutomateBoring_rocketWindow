import os
with open("my_file.txt", "w") as file:
    file.write("Hello, world!")
    file.flush()  # Flush the buffer
    os.fsync(file.fileno())  # Force write to disk

input("")