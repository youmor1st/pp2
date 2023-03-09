
my_list = ['aa','ew','rw']

s=str(input())

with open(s, 'w') as f:

    for item in my_list:
        f.write("%s\n" % item)

print("List written to file:", s)
