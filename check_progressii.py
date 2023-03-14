import sys

spisok = [int(row.strip()) for row in sys.stdin]

if spisok == list(range(spisok[0], spisok[-1]+1)):
    print('Арифметическая прогрессия')
else:
    n = spisok[1]/spisok[0] #коэф.прогрессии
    for i in range(1, len(spisok)):
        if spisok[i]/spisok[i-1] == n:
            flag = True
        else:
            flag = False
            break
    if flag == True:
        print('Геометрическая прогрессия')
    else:
        print('Не прогрессия')