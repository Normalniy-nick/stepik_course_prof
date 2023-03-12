from datetime import date, timedelta
import calendar

def get_all_mondays(year: int):
    for i in range(1, 8):
        if calendar.weekday(year, 1, i) == 0:
            step = i
            break
    sp = []
    first = date(year, 1, step)
    while first <= date(year, 12, 31):
        sp.append(first)
        first += timedelta(7)
    return sp