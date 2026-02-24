mx = int(input("MAX: "))
mid = int(input("MID: "))
mn = int(input("MIN: "))
dif = int(input("DIF: "))

mxd = mx - mid
mnd = mid - mn

if (mxd > dif * 3 or mnd > dif * 3) and (mxd <= dif * 5 and mnd <= dif * 5):
    print("В ваших данных имеются выбросы и требуют предобработки")
elif mxd > dif * 5 or mnd > dif * 5:
    print("Вы ваших данных имеются экстремальные значения и требуют предобработки")
elif mxd <= dif * 3 or mnd <= dif * 3:
    print("Ваши данные пригодны для анализа")
