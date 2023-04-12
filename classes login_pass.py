import string


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @login.setter
    def login(self, login):
        if not isinstance(login, str):
            raise TypeError
        elif '@' not in login:
            raise ValueError
        elif '.' not in login or login.index('.') < login.index('@'):
            raise ValueError
        else:
            self.__login = login

    @staticmethod
    def is_include_digit(password):
        cyfr = '0123456789'
        for num in cyfr:
            if num in password:
                return True
        return False

    @staticmethod
    def is_include_all_register(password):
        count = ['low_in_password', 'up_in_password']
        flag = 0
        for i in password:
            if len(count) == 0:
                return True
            elif i in string.ascii_lowercase and (flag == 1 or flag == 0):
                count.remove('low_in_password')
                flag = 2
            elif i in string.ascii_uppercase and (flag == 2 or flag == 0):
                count.remove('up_in_password')
                flag = 1
        return False

    @staticmethod
    def is_include_only_latin(password):
        for i in password:
            if i not in string.ascii_letters and i not in '0123456789':
                return False
        return True

    @staticmethod
    def check_password_dictionary(password):
        with open('C:/Users/ckzef/PycharmProjects/pythonProject/easy_passwords.txt', 'r', encoding='utf-8') as file:
            spisok = file.readlines()
            spisok = [i.strip() for i in spisok]
            if password not in spisok:
                return True
            else:
                return False

    @password.setter
    def password(self, password):
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть строкой")
        elif len(password) < 5 and len(password) >= 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        elif not Registration.is_include_digit(password):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        elif not Registration.is_include_all_register(password):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        elif not Registration.is_include_only_latin(password):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        elif not Registration.check_password_dictionary(password):
            raise ValueError('Ваш пароль содержится в списке самых легких')

r1 = Registration('qwerty@rambler.ru', 'QwrRt124') # здесь хороший логин
print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124

# теперь пытаемся запись плохие пароли
r1.password = '123456'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
r1.password = 'LoW'  # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
r1.password = 43  # raise TypeError("Пароль должен быть строкой")