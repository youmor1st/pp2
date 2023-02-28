import datetime

date1_str = input("Enter the first date in YYYY-MM-DD HH:MM:SS format: ")
date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")


date2_str = input("Enter the second date in YYYY-MM-DD HH:MM:SS format: ")
date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

difference_seconds = (date2 - date1).total_seconds()

print("The difference between the two dates is", difference_seconds, "seconds.")
