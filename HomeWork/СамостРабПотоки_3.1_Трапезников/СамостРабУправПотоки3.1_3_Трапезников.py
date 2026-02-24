age_of_user = int(input("Возраст пользователя: "))
age_limit = int(input("Ограничение: "))

if age_of_user < age_limit:
    print("Извините, ваш возраст не соответствует введенным возрастным ограничениям")
else:
    print("Приятного просмотра")