class IncorrectLogin(BaseException):
    def __init__(self):
        print("Логин должен быть не менее 3 символов и не более 20")

        
class IncorrectPassword(BaseException):
    def __init__(self):
        print("Пароль должен быть не менее 4 символов и не более 32")


class LoginIsTaken(BaseException):
    def __init__(self):
        print("К сожалению, логин занят")


class IncorrectData(BaseException):
    def __init__(self):
        print("Неверный логин/пароль")

class IncorrectAction(BaseException):
    def __init__(self):
        print("Неверное действие")