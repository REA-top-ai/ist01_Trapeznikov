import random

n = int(input("Введите количество бросков монеты: "))
for _ in range(n):
    if random.randint(0, 1) == 0:
        print("Орел")
    else:
        print("Решка")