# https://stepik.org/lesson/571244/step/8?unit=565785
# Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00. Напишите программу, которая принимает
# на вход текущие дату и время и определяет, сколько времени осталось до выхода курса.
# Программа должна вывести текст с указанием количества дней и часов, оставшихся до выхода курса, в правильном формате

from datetime import datetime

declensions = {0: ("день", "час", "минута"), 1: ("дня", "часа", "минуты"), 2: ("дней", "часов", "минут")}
def choose_plural(amount): # функция подсчёт по остаткам окончаний времени
    if amount > 10 and amount % 100 in (11, 12, 13, 14):
        res = declensions[2]
    elif amount % 10 == 1:
        res = declensions[0]
    elif amount % 10 in (2, 3, 4):
        res = declensions[1]
    else:
        res = declensions[2]
    return res

start = datetime.strptime('08.11.2022 12:00', '%d.%m.%Y %H:%M')
data = datetime.strptime(input(), '%d.%m.%Y %H:%M')

if data >= start:
    print('Курс уже вышел!')
else:
    declensions = {0: ("день", "час", "минута"), 1: ("дня", "часа", "минуты"), 2: ("дней", "часов", "минут")}
    res = start - data

    if res.days == 0 and res.seconds // 3600 == 0:  # дней = 0 и часов = 0 - только минуты
        print(f'До выхода курса осталось: {res.seconds // 60 % 60} {choose_plural(res.seconds // 60 % 60)[2]}')

    elif res.days == 0 and res.seconds // 60 % 60 == 0:  # 0 минут 0 дней - только часы
        print(f'До выхода курса осталось: {res.seconds // 3600} {choose_plural(res.seconds // 3600)[1]}')

    elif res.seconds // 3600 == 0:
        print(f'До выхода курса осталось: {res.days} {choose_plural(res.days)[0]}')  # дней

    elif res.days == 0:
        print(
            f'До выхода курса осталось: {res.seconds // 3600} {choose_plural(res.seconds // 3600)[1]} и {res.seconds // 60 % 60} {choose_plural(res.seconds // 60 % 60)[2]}')  # 0 дней - часов и минут
    else:
        print(
            f'До выхода курса осталось: {res.days} {choose_plural(res.days)[0]} и {res.seconds // 3600} {choose_plural(res.seconds // 3600)[1]}')