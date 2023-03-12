import calendar
from datetime import datetime, date

year = int(input())
sp = []
count = 0
for month in range(1, 13):
    for week in calendar.monthcalendar(year, month):
        if week[3] < 1:
            continue
        count += 1
        if count == 3:
            tuesday = week[3]
            count = 0
            if tuesday:
                data = date(year, month, tuesday)
                print(datetime.strftime(data, '%d.%m.%Y'))
                break