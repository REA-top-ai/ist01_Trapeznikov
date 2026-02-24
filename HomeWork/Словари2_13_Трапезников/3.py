caffeine = {
    "espresso": 64,
    "chai": 40,
    "decaf": 0,
    "drip": 120
    }

caffeine.update({"matcha": 30})

try:
    print(caffeine["matcha"])
except KeyError:
    print("Неизвестный уровень кофеина")