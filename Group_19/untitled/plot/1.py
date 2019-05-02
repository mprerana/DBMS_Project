import datetime
date = datetime.date.today()
for i in range(5):
    date += datetime.timedelta(days=1)
    print(date)
date += datetime.timedelta(days=30)
print(date)