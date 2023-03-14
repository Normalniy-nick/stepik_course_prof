import sys
from datetime import datetime
data = sys.stdin.readlines()
check = datetime.strptime(data[0].strip(), '%d.%m.%Y') #первое значение - с чем сравниваем
flag = ''
for i in range(1, len(data)):
    if check > datetime.strptime(data[i].strip(), '%d.%m.%Y') and flag != 'ASC': #последовательность убывающая
        flag = 'DESC'
        check = datetime.strptime(data[i].strip(), '%d.%m.%Y')
    elif check < datetime.strptime(data[i].strip(), '%d.%m.%Y') and flag != 'DESC': #последовательность возрастающая
        flag = 'ASC'
        check = datetime.strptime(data[i].strip(), '%d.%m.%Y')
    else:
        flag = 'MIX' #последовательность смешанная
        break
print(flag)