import random

class SystemStub:
    login: str
    password: str

    def __init__(self, login: str = 'admin'):
        self.login = login
        self.password = 'j569872a0cfe89' # Тут хранится пароль

    def auth(self, password: str):
        is_password_blank = self.password == ''
        if is_password_blank:
            random_value = random.randrange(1, 10)
            is_winning_condition = random_value == 7
            if is_winning_condition:
                self.password = password
                return 'SUCCESS'
            else:
                return 'PASSWORD IS NOT VALID'
        else:
            is_same_password = password == self.password
            if is_same_password:
                return '!!! SUCCESS !!!'
            else:
                return '!!! TRUE PASSWORD IS NOT VALID !!!'
