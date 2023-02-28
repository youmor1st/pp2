import re

f= open('txt.txt',  encoding='utf-8')
text = str(f.read())
matches = re.findall("ab{2,3}$", text)
print(matches)
