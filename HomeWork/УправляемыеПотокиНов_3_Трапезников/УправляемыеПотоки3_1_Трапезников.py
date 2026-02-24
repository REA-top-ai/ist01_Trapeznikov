enter_number = 3

dmitriy_check = ("Дмитрий, твое рабочее место находится в другой комнате."
                 "Отойди от чужого компьютера и займись работой")
true_developer = "Добро пожаловать"

user_name = input()
if user_name == "Дмитрий":
    print(dmitriy_check)
elif user_name == "Ангелина":
    print(true_developer)
else:
    enter_number -= 1
    print("Попробуйте еще раз. У вас осталось", enter_number, "- попыток")
    user_name = input()
    if user_name == "Дмитрий":
        print(dmitriy_check)
    elif user_name == "Ангелина":
        print(true_developer)
    else:
        enter_number -= 1
        print("Попробуйте еще раз. У вас осталось", enter_number, "- попыток")
        user_name = input()
        if user_name == "Дмитрий":
            print(dmitriy_check)
        elif user_name == "Ангелина":
            print(true_developer)
        else:
            enter_number -= 1
            print("Ваша учетная запись заблокирована. Обратитесь в службу поддержки")




