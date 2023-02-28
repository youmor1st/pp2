import datetime
current = datetime.date.today()
yes = current - datetime.timedelta(days=1)
tom = current + datetime.timedelta(days=1)
print("Current date:", current)
print("Yestarday", yes)
print("Tomorrow ",tom)
