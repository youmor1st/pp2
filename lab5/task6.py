import re

f= open('txt.txt',  encoding='utf-8')
text = str(f.read())
x = re.sub(" ", ',', s)

print(x)
