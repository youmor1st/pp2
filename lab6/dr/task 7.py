waw=str(input())
qaq=str(input())
with open(waw, "r") as s, open(qaq, "w") as d:

    d.write(s.read())
