import hashlib
import random
import string
from stubs import SystemStub
from bf import read_file_line_by_line

def generate_passwords_file():
    with open(file='passwords.txt', mode='w', encoding='utf-8') as file:
        random_values = list()
        for i in range(1001):
            random_letter_index = random.randrange(start=0, stop=26)
            random_letter = string.ascii_lowercase[random_letter_index]
            random_number = random.randrange(start=10, stop=99999)
            random_number_as_string = str(random_number)
            some = random_number_as_string.encode()
            random_index = random.randrange(start=3, stop=9)
            random_hash_part = hashlib.md5(some).hexdigest()[:random_index]
            password = random_letter + \
                       random_number_as_string + \
                       random_hash_part + \
                       '\n'
            random_values.append(password)
        file.writelines(random_values)

def do_bruteforce(system_stub, passwords_file_path):
    passwords = read_file_line_by_line(passwords_file_path)
    print(type(passwords))
    for password in passwords:
        password = password.strip()  # Убираем символ новой строки
        result = system_stub.auth(password)
        
        if result == '!!! SUCCESS !!!':
            return password

    return None  # В случае, если пароль не был найден

if __name__ == "__main__":
    generate_passwords_file()  # Шаг 1: Генерация файла passwords.txt
    system_stub = SystemStub()
    passwords_file_path = 'passwords.txt'
    cracked_password = do_bruteforce(system_stub, passwords_file_path)

    if cracked_password:
        print(f"Password cracked: {cracked_password}")
    else:
        print("Password not found.")
