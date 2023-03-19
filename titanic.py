import csv
with open('C:/Users/ckzef/PycharmProjects/pythonProject/titanic.csv', 'r', encoding='utf-8') as titanic:
    data = csv.reader(titanic, delimiter=';')

    for i in sorted(data, key=lambda x: x[2], reverse = True):
        if i[0] == '1' and float(i[3]) < 18:
            print(i[1])