class User:
    def get_user_password(self) -> str:
        """
        Запрос пароля от пользователя.
        :return: str (возвращает введенный пароль)
        """
        return input("Введите пароль: ")

    def get_user_login(self) -> str:
        """
        Запрос логина от пользователя.
        :return: str (возвращает введенный логин)
        """
        return input("Введите логин: ")

    def correct_login(self) -> str:
        """
        Используется для проверки логина на корректную длину.
        :return: str (возвращает корректный логин)
        """
        login = self.get_user_login()
        while True:
            if len(login) < 3 or len(login) > 20:
                print("Логин должен быть не менее 3 символов и не более 20")
                login = self.get_user_login()
            else:
                return login

    def correct_password(self) -> str:
        """
        Используется для проверки пароля на корректную длину.
        :return: str (возвращает корректный пароль)
        """
        password = self.get_user_password()
        while True:
            if len(password) < 4 or len(password) > 32:
                print("Пароль должен быть не менее 4 символов и не более 32")
                password = self.get_user_password()
            else:
                return password


class FileSystem:
    def request_base(self) -> list:
        """
        Выводит БД в формате списка.
        :return: list (Возвращает список со всеми логинами/паролями)
        """
        with open("data.txt") as read_file:
            return read_file.read().splitlines()


class AuthSystem:
    user = User()
    data = FileSystem()

    def start(self) -> bool:
        """
        Запускает программу.
        :return: bool (Если регистрация/авторизация прошла успешно - останавливает программу.)
        """
        while True:
            if self.run_action():
                break

    def select_action(self) -> str:
        """
        Используется для выбора действия: регистрация/авторизация.
        :return: str (Возвращает выбор действия)
        """
        return input("1. Зарегистрироваться\n2. Авторизоваться\nВыбор: ")

    def registration(self) -> bool:
        """
        Используется для регистрации. Проверяет занят ли логин. Если не занят - вносит его в БД.
        :return: bool (Если регистрация успешна - останавливает программу)
        """
        login = self.user.correct_login()
        base = self.data.request_base()
        while True:
            if login in base:
                print("К сожалению логин занят!")
                break
            elif login not in base:
                with open("data.txt", "a") as write_file:
                    write_file.write(f'{login}\n')
                    write_file.write(f'{self.user.correct_password()}\n')
                    print("Успешная регистрация!")
                    return True


    def authorization(self) -> bool:
        """
        Используется для авторизации. Проверяет введенные пользователем логин, пароль в БД.
        :return: bool (Если авторизация успешна - останавливает программу)
        """
        login = self.user.correct_login()
        password = self.user.correct_password()
        base = self.data.request_base()
        for i in range(len(base)):
            if base[i] == login:
                if base[i + 1] == password:
                    print("Успешная авторизация!")
                    return True
                    break
                else:
                    break
            else:
                print("Неверный логин/пароль")
                break

    def run_action(self) -> bool:
        """
        Запускает метод регистрации/авторизации.
        :return: bool (Вызывает регистрацию/авторизацию)
        """
        action = self.select_action()
        if action == "1":
            return self.registration()
        elif action == "2":
            return self.authorization()
        else:
            print("Некорректное действие")


Timur = AuthSystem()
Timur.start()
