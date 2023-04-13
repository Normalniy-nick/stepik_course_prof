class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, dengi):
        self.__balance = dengi

    def deposit(self, dengi):
        self.__balance += dengi

    def payment(self, minus_babki):
        if minus_babki > self.__balance:
            print('Не хватает средств на балансе. Пополните счет')
            return False
        else:
            self.__balance -= minus_babki
            return True

class Cart:
    def __init__(self, User):
        self.user = User
        self.__total = 0
        self.goods = {}

    def add(self, product, count_tovar=1):
        self.goods[product] = self.goods.get(product, 0) + count_tovar
        self.__total += product.price * count_tovar

    def remove(self, product, count_tovar=1):
        if count_tovar >= self.goods[product]:
            count_tovar = self.goods[product]
        self.goods[product] = self.goods.get(product, 0) - count_tovar
        self.__total -= product.price * count_tovar

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.__total):
            print('Заказ оплачен')
        else:
            print('Проблема с оплатой')

    def print_check(self):
        print('---Your check---')
        for i in sorted(self.goods, key=lambda x: x.name):
            if self.goods[i] > 0:
                print(f'{i.name} {i.price} {self.goods[i]} {i.price * self.goods[i]}')
        print(f'---Total: {self.total}---')

billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20