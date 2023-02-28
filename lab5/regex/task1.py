import re

f= open('txt.txt',  encoding='utf-8')
text = str(f.read())
matches = re.findall("ab*$", text)
print(matches)
