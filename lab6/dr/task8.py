import os

file_path = str(input())


if os.path.exists(file_path):
    if os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"The file {file_path} has been deleted.")
    else:
        print(f"You don't have the required permissions to delete the file {file_path}.")
else:
    print(f"The file {file_path} doesn't exist.")
