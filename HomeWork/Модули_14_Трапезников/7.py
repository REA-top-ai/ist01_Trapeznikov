import random

length = int(input("Введите длину пароля: "))
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
password = ''.join(random.choice(chars) for _ in range(length))
print(password)