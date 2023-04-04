import copy

class Player:
    def __init__(self, name): ##имя игрока
        self.name = name

def hod(player): ## возвращает поставленное значение
    if player == player1:
        return 'X'
    else:
        return '0'

def check(pole): ## Проверка на победителя
    #переведем pole для удобства в 0 и 1
    old = copy.deepcopy(pole) # делаем копию массива поля
    for i in range(3):
        for j in range(3):
            if pole[i][j] == 'X':
                pole[i][j] = 1
            elif pole[i][j] == '0':
                pole[i][j] = 0
            else:
                pole[i][j] = 999
    # Поиск победителя в строках
    if sum(pole[0]) == 3 or sum(pole[1]) == 3 or sum(pole[2]) == 3:
        win = 1
    elif sum(pole[0]) == 0 or sum(pole[1]) == 0 or sum(pole[2]) == 0:
        win = 0
    # Поиск победителя в столбцах
    elif pole[0][0] + pole[1][0] + pole[2][0] == 3 or pole[0][1] + pole[1][1] + pole[2][1] == 3 or pole[0][2] + pole[1][2] + pole[2][2] == 3:
        win = 1
    elif pole[0][0] + pole[1][0] + pole[2][0] == 0 or pole[0][1] + pole[1][1] + pole[2][1] == 0 or pole[0][2] + pole[1][2] + pole[2][2] == 0:
        win = 0
    # Поиск победителя в диагоналях
    elif pole[0][0] + pole[1][1] + pole[2][2] == 3 or pole[0][2] + pole[1][1] + pole[2][0] == 3:
        win = 1
    elif pole[0][0] + pole[1][1] + pole[2][2] == 0 or pole[0][2] + pole[1][1] + pole[2][0] == 0:
        win = 0
    else:
        win = 2 # победителя пока нет
    pole = old # возвращаем pole к начальному значению до проверки победителя
    return win, pole

## Выбираем имена игрокам
player1 = input('Введите имя первого игрока, который начинает играть крестиком\n')
player2 = input('Введите имя второго игрока, начинает играть ноликом\n')
while player2 == player1:
    player2 = input('Выввели такое же имя как и у первого игрока. Введите уникальное имя второго игрока, начинает играть ноликом\n')

player = player1

## Создаём игровое поле
pole = [['' for i in range(3)] for j in range(3)]
print('Перед вами поле 3x3', *pole, sep='\n')
count = 0
while True:
    if count == 0:
        coord = list(map(int, input('Выберите клетку, куда поставить значение в формате: Номер горизонтали ПРОБЕЛ номер вертикали\n').split()))
    else:
        coord = list(map(int, input('Ваш ход\n').split()))
    count += 1
    if 0 < coord[0] < 4 and 0 < coord[1] < 4:
        if pole[coord[0]-1][coord[1]-1] == '': ## Проверка на вносимое значение в пустую ячейку
            pole[coord[0]-1][coord[1]-1] = hod(player)
            print(*pole, sep='\n')
            if count > 4:
                winner, pole = check(pole)
                if winner == 1:
                    print('Победитель Игрок №1', player1)
                    break
                elif winner == 0:
                    print('Победитель Игрок №2', player2)
                    break
                else:
                    pass
            player1, player2 = player2, player1 # следующий ход делает другой игрок
            if count == 9: # максимум ходов
                print('Ничья')
                break
        else:
            print('Ячейка поля уже имеет значение, введите новое значение')
            count -= 1
    else:
        print('Вы ввели некорректное значение строки и столбца, попробуйте снова\n')
        count -= 1