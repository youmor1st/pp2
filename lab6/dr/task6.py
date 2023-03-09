import string
s=str(input())
for letter in string.ascii_uppercase:
    s = letter + ".txt"
    with open(s, "w") as file:
        file.write("This is file {}.".format(s))
