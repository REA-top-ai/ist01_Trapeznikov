import random

name = input("Имя: ")
question = input("Вопрос: ")
if question != "":
    answer = ""
    random_number = random.randint(1, 9)

    if random_number == 1:
        answer = "Да, безусловно"
    elif random_number == 2:
        answer = "Это решительно так"
    elif random_number == 3:
        answer = "Без сомнения"
    elif random_number == 4:
        answer = "Ответ туманный, попробуйте еще раз"
    elif random_number == 5:
        answer = "Спросите еще раз позже"
    elif random_number == 6:
        answer = "Лучше не говорить вам сейчас"
    elif random_number == 7:
        answer = "Мои источники говорят нет"
    elif random_number == 8:
        answer = "Прогноз не очень хороший"
    elif random_number == 9:
        answer = "Очень сомнительно"
    else:
        answer = "Карамба. Программа дала сбой"

    if name == "":
        print("Questions:", question)
        print("Магический шар отвечает:", answer)
    else:
        print(name, "спрашивает:", question)
        print("Магический шар отвечает:", answer)
else:
    print("Придумай вопрос сначала, а потом ко мне приходи, мой юный падаван")
