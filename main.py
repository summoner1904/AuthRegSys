import exception
from exception import *


class User:
    """
    Запрашивает у пользователя логин, пароль и проверяет их на корректность.
    """

    def get_user_data(self) -> tuple:
        """
        Запрашивает у пользователя логи и пароль
        :return: tuple (Возвращает кортеж, состоящий из логина и пароля)
        """
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        return self.check_correct_data(login, password)

    def check_correct_data(self, login, password) -> tuple:
        """
        Проверяет введенный логин и пароль на корректность.
        :param login (Логин пользователя)
        :param password (Пароль пользователя)
        :return: tuple (Если проверки успешны - возвращает кортеж с корректным логином, паролем)
        """
        try:
            if 3 < len(login) < 21:
                if 3 < len(password) < 33:
                    return login, password
                else:
                    raise IncorrectPassword
            else:
                raise IncorrectLogin()
        except IncorrectPassword:
            return self.get_user_data()
        except IncorrectLogin:
            return self.get_user_data()


class FileSystem:
    """
    Используется для работы с БД.
    """

    def request_base(self) -> list:
        """
        Выводит БД в формате списка.
        :return: list (Возвращает список со всеми логинами/паролями)
        """
        with open("data.txt") as read_file:
            return read_file.read().splitlines()

    def add_base(self, user_data) -> bool:
        """
        Вносит данные пользователя, введеных при регистрации, в БД
        :return: bool (1 - Успешная регистрация)
        """
        with open("data.txt", "a") as write_file:
            write_file.write(f'{user_data[0]}\n')
            write_file.write(f'{user_data[1]}\n')
            print("Успешная регистрация!")
        return True


class AuthSystem:
    """
    Используется для регистрации/авторизации пользователя.
    """
    user = User()
    data = FileSystem()

    def start(self) -> bool:
        """
        Запускает работу класса.
        :return: bool (Если регистрация/авторизация прошла успешно - останавливает программу.)
        """
        while True:
            if self.run_action():
                break

    def select_action(self) -> int:
        """
        Используется для выбора действия: регистрация/авторизация.
        :return: str (Возвращает выбор действия)
        """
        return int(input("1. Зарегистрироваться\n2. Авторизоваться\nВыбор: "))

    def registration(self) -> tuple:
        """
        Используется для регистрации. Проверяет занят ли логин. Если не занят - вносит его в БД.
        :return: bool (Если регистрация успешна - прерывается работа метода)
        """
        try:
            user_data = self.user.get_user_data()
            base = self.data.request_base()
            while True:
                if user_data[0] in base:
                    raise LoginIsTaken
                elif user_data[0] not in base:
                    if self.data.add_base(user_data):
                        return True
        except LoginIsTaken:
            return self.registration()

    def authorization(self) -> bool:
        """
        Используется для авторизации. Проверяет введенные пользователем логин, пароль в БД.
        :return: bool (Если авторизация успешна - прерывается работа метода)
        """
        try:
            counter = 0
            user_data = self.user.get_user_data()
            login = user_data[0]
            password = user_data[1]
            base = self.data.request_base()
            for i in range(len(base)):
                if base[i] == login:
                    if base[i + 1] == password:
                        print("Успешная авторизация!")
                        counter += 1
                        return True
            if counter == 0:
                raise IncorrectData
        except:
            return self.authorization()
            
        

    def run_action(self) -> bool:
        """
        Запускает метод регистрации/авторизации.
        :return: bool (Если возвращает 1 - запускает регистрацию, если возвращает 2 - запускает авторизацию)
        """
        try:
            action = self.select_action()
            if action == 1:
                return self.registration()
            elif action == 2:
                return self.authorization()
            else:
                raise IncorrectAction
        except IncorrectAction:
            return self.run_action()


if __name__ == "__main__":
    Timur = AuthSystem()
    Timur.start()
