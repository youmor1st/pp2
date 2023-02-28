import datetime
current = datetime.date.today()
five = current - datetime.timedelta(days=5)

print("Current date:", current)
print("Five days ago:", five)
