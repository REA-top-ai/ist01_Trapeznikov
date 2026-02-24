mark = int(input("марка 1 - Wolkswagen, 2 - BMW:"))
year = int(input("Возраст водителя(20 - 34):"))
stag = int(input("Стаж(2 - 15):"))
star  = int(input("Рейтинг(1 - 5):"))
prob = int(input("Пробки(1 - 7):"))
time = int(input("Время поездки: "))
tarif = 0

if mark == 1:
    if 20<= year <= 27:
        if 2 <= stag <= 9:
            if 1 <= star <= 2:
                if 1 <= prob <= 3:
                    cost = 8 * time
                elif 4 <= prob <= 7:
                    cost = 8.5 * time
                else:
                    print("Таких пробок нет. Выберите от 1 до 7")
            elif 3 <= star <= 5:
                if 1 <= prob <= 3:
                    cost = 7.5 * time
                elif 4 <= prob <= 7:
                    cost = 7.4 * time
                else:
                    print("Таких пробок нет. Выберите от 1 до 7")
            else:
                print("Такого рейтинга не существует. Выберите от 1 до 5")
        else:
            print("Водителей с таким стажем нет. Выберите другой вариант")
    elif 27 <= year <= 34:
        if 2 <= stag <= 9:
            if 1 <= star <= 2:
                if 1 <= prob <= 3:
                    cost = 7.2 * time
                else:
                    print("Таких пробок нет. Выберите от 1 до 3")
            elif 3 <= star <= 5:
                if 1 <= prob <= 3:
                    cost = 7 * time
                elif 4 <= prob <= 7:
                    cost = 7.2 * time
                else:
                    print("Таких пробок нет. Выберите от 1 до 7")
            else:
                print("Такого рейтинга не существует. Выберите от 1 до 5")
        elif 10 <= stag <= 15:
            if 1 <= star <= 2:
                if 1 <= prob <= 3:
                    cost = 6.9 * time
                elif 4 <= prob <= 7:
                    cost = 6.7 * time
                else:
                    print("Таких пробок нет. Выберите от 1 до 3")
            elif 3 <= star <= 5:
                if 1 <= prob <= 3:
                    cost = 6.6 * time
                else:
                    print("Таких пробок нет. Выберите от 1 до 3")
            else:
                print("Такого рейтинга не существует. Выберите от 1 до 5")

        else:
            print("Водителей с таким стажем нет. Выберите другой вариант")

elif mark == 2:
    if 20<= year <= 27:
        if 2 <= stag <= 9:
            if 1 <= star <= 2:
                if 1 <= prob <= 3:
                    cost = 12 * time
                elif 4 <= prob <= 7:
                    cost = 12.5 * time
                else:
                    print("Таких пробок нет. Выберите от 1 до 7")
            elif 3 <= star <= 5:
                if 1 <= prob <= 3:
                    cost = 11.6 * time
                elif 4 <= prob <= 7:
                    cost = 11.3 * time
                else:
                    print("Таких пробок нет. Выберите от 1 до 7")
            else:
                print("Такого рейтинга не существует. Выберите от 1 до 5")
        else:
            print("Водителей с таким стажем нет. Выберите другой вариант")
    elif 27 <= year <= 34:
        if 2 <= stag <= 9:
            if 1 <= star <= 2:
                if 1 <= prob <= 3:
                    cost = 11.4 * time
                else:
                    print("Таких пробок нет. Выберите от 1 до 3")
            elif 3 <= star <= 5:
                if 1 <= prob <= 3:
                    cost = 11.7 * time
                elif 4 <= prob <= 7:
                    cost = 119 * time
                else:
                    print("Таких пробок нет. Выберите от 1 до 7")
            else:
                print("Такого рейтинга не существует. Выберите от 1 до 5")
        elif 10 <= stag <= 15:
            if 1 <= star <= 2:
                if 1 <= prob <= 3:
                    cost = 10.8 * time
                elif 4 <= prob <= 7:
                    cost = 11 * time
                else:
                    print("Таких пробок нет. Выберите от 1 до 3")
            elif 3 <= star <= 5:
                if 1 <= prob <= 3:
                    cost = 10.9 * time
                else:
                    print("Таких пробок нет. Выберите от 1 до 3")
            else:
                print("Такого рейтинга не существует. Выберите от 1 до 5")

        else:
            print("Водителей с таким стажем нет. Выберите другой вариант")
else:
    print("Других машин нет. Выберите среди этих")

print("Стоимость вашей поездки составляет:", cost)
