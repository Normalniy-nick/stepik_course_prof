import csv

with open('C:/Users/ckzef/PycharmProjects/pythonProject/wifi.csv', 'r', encoding='utf-8') as wifi:
    data = csv.reader(wifi, delimiter=';')
    data = list(data)[1:]
    d = {}
    for i in sorted(data, key=lambda x: (int(x[3]), x[1])):
        d[i[1]] = d.get(i[1], 0) + int(i[3])

    for key, value in sorted(d.items(), key=lambda x: (-x[1], x[0])):
        print(f'{key}: {value}')
