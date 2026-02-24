def day_clothes(time, clothes):
    print("У меня большой гардероб")
    print(f"{time} лучше подходит {clothes} \n")


morning = "Утром"
day = "Днем"
evening = "Вечером"
night = "Ночью"
morning_c = "шорты и футболка"
day_c = "деловой костюм"
evening_C = "домашняя одежда"
night_C = "ночник"

day_clothes(morning, morning_c)
day_clothes(day, day_c)
day_clothes(evening, evening_C)
day_clothes(night, night_C)


def eat_something(time, meal):
    print("Мои предпочтения в еде")
    print(f"{time} я люблю есть {meal} \n")


morning_m = "блинчики"
day_m ="борщ и рис с котлетой"
evening_m = "макароны с сыром и котлеой"
night_m = "печенье"

eat_something(morning, morning_m)
eat_something(day, day_m)
eat_something(evening, evening_m)
eat_something(night, night_m)
