import re

f= open('txt.txt',  encoding='utf-8')
text = str(f.read())
matches = re.findall("a.*b$", text)
print(matches)
