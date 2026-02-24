import random

n = int(input("Введите количество бросков кубика: "))
for _ in range(n):
    print(random.randint(1, 6))