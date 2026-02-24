user_name = "Дмитрий"
Dmitriy_check = "Дмитрий, добро пожаловать! Твое рабочее место находится в этой комнате"
Dmitriy_check_F = ("Дмитрий, твое рабочее место находится в другой комнате."
                   "Отойди от чужого компьютера и займись работой!")
welcome_message = "Добро пожаловать!"

def check_user(user_name):
    if user_name == "Дмитрий":
        print(Dmitriy_check)
    else:
        print(welcome_message)


dmitriy = 1
angelina = 2
vasilisa = 3
ekaterina = 4


def check_user_2(user_name, apm):
    if user_name == "Дмитрий" and apm == 1:
        print(Dmitriy_check)
    elif user_name == "Дмитрий" and apm != 1:
        print(Dmitriy_check_F)
    elif user_name == "Ангелина" and apm == 2:
        print(welcome_message)
    elif user_name == "Василий" and apm == 3:
        print(welcome_message)
    elif user_name == "Екатерина" and apm == 4:
        print(welcome_message)
    else:
        print("Неверное либо имя пользователя, либо APM")


check_user_2("Ангелина", 2)

