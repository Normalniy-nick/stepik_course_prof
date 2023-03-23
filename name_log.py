import csv
from datetime import datetime

with open('C:/Users/ckzef/PycharmProjects/pythonProject/name_log.csv', 'r', encoding='utf-8') as name_log:
    data = csv.reader(name_log, delimiter=',')
    d = {}
    data = list(data)[1:]
    for i in data:
        if i[1] not in d:
            d[i[1]] = (datetime.strptime(i[2], '%d/%m/%Y %H:%M'), i[0]) # В словарь кортеж ник и время
        else:
            if datetime.strptime(i[2], '%d/%m/%Y %H:%M') > d[i[1]][0]: # Если новое время раньше внесённого, то
                d[i[1]] = (datetime.strptime(i[2], '%d/%m/%Y %H:%M'), i[0]) # емэйл = новому нику с новым временем
            else:
                pass

    sp = []
    for key, value in sorted(d.items(), key=lambda x: x[1]):  # сортировка по ликсико email
        sp.append((value[1], key, datetime.strftime(value[0], '%d/%m/%Y %H:%M')))
    print(sp)
    with open('new_name_log.csv', 'w', newline='', encoding='utf-8') as out:
        writer = csv.writer(out, delimiter=',')
        columns = ['username', 'email', 'dtime']
        writer.writerow(columns)
        sp = sorted(sp, key=lambda x: x[1]) # сортировка по емэйлу
        writer.writerows(sp)