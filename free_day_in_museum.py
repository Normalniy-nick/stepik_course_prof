import calendar
from datetime import datetime, date

year = int(input())
count = 0
for month in range(1, 13):
    for week in calendar.monthcalendar(year, month): # список дней по неделям
        if week[3] < 1:  # проверка первой недели на присутствие четверга, если четверга нет, то будет нулевое значение
            continue
        count += 1
        if count == 3:  # каждая третья неделя, где есть четверг
            tuesday = week[3]
            count = 0  # обнуляем счётчик четверга
            if tuesday:
                data = date(year, month, tuesday)
                print(datetime.strftime(data, '%d.%m.%Y'))
                break