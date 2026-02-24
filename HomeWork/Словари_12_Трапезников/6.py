drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
drinks_to_caffeine = {key: value for key, value in zip(drinks, caffeine)}

print(drinks_to_caffeine)