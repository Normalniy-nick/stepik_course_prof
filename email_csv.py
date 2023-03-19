import csv

with open('C:/Users/ckzef/PycharmProjects/pythonProject/data.csv', 'r', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=',')
    data = list(data)[1:]
    d = {}
    for i in data:
        email = i[2]
        domen = ''
        for j in email:
            if j != '@':
                email = email[1:]
            else:
                domen = email[1:]
                break
        d[domen] = d.get(domen, 0) + 1
    with open('C:/Users/ckzef/PycharmProjects/pythonProject/domain_usage.csv', 'w', newline='', encoding='utf-8') as file_output:
        writer = csv.writer(file_output, delimiter=',')
        sp = [(i, d[i]) for i in d]
        sp = sorted(sp, key=lambda x: (x[1], x[0]))
        columns = ['domain', 'count']
        writer.writerow(columns)
        writer.writerows(sp)