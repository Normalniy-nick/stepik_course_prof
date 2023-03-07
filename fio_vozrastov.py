from datetime import date, time, timedelta, datetime

n = int(input())
spisok = []
chel = input().split()
spisok.append(chel)
pattern = '%d.%m.%Y'
for i in range(n-1):
    chel = input().split()
    if datetime.strptime(chel[2], pattern) < datetime.strptime(spisok[0][2], '%d.%m.%Y'):
        spisok.clear()
        spisok.append(chel)
    elif datetime.strptime(chel[2], '%d.%m.%Y') == datetime.strptime(spisok[0][2], '%d.%m.%Y'):
        spisok.append(chel)
    else:
        pass
if len(spisok) == 1:
     for i in spisok:
        print(i[2], i[0], i[1])
else:
    print(spisok[0][2], len(spisok))