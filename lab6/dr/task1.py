import os


path = input("Enter the path to search: ")


directories = []
for entry in os.listdir(path):
    if os.path.isdir(os.path.join(path, entry)):
        directories.append(entry)

print("Directories:")
print(directories)


files = []
for entry in os.listdir(path):
    if os.path.isfile(os.path.join(path, entry)):
        files.append(entry)

print("Files:")
print(files)


all_entries = directories + files
print("All entries:")
print(all_entries)
