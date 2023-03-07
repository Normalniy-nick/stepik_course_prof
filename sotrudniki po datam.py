from datetime import datetime

n = int(input())
d = {}
dd = {}
# Создадим словарь из дат - количество
for i in range(n):
    sotrudnik = input().split()
    d[sotrudnik[2]] = d.get(sotrudnik[2], 0) + 1

max_value = max(d.values())
res = []
check = []
# Пройдёмся по ключам-датам, каждому дню посчитаем количество повторений и кинем в словарь дней dd
for data, kolvo in d.items():
    if int(kolvo) == max_value:
        dd[data[:2]] = int(kolvo)
        if data not in check: # сверка уникальности дат
            res.append(data)
            check.append(data)
fin = []

for i in sorted(res, key=lambda x: datetime.strptime(x, '%d.%m.%Y')):
    print(i)

# for i in res: # закинем в новый словарь даты в нужном формате, чтобы потом их отсортировать и вывести
#     fin.append(datetime.strptime(i, '%d.%m.%Y'))
# for j in sorted(fin):
#     print(datetime.strftime(j, '%d.%m.%Y'))