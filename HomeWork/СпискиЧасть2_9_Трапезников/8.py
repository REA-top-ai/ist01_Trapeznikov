inventory = ['двухспальная кровать', 'двухспальная кровать', 'изголовье', 'двухспальная кровать',
    'двухспальная кровать', 'комод', 'комод', 'стол', 'стул', 'тумбочка', 'тумбочка', 'королевский кровать',
    'двухспальная кровать', 'две односпальные кровати', 'две односпальные кровати',
    'простыни', 'простыни', 'подушка', 'подушка']

first = inventory[0]
print(first)

last = inventory[-1]
print(last)

inventory_2_6 = inventory[2:6]
print(inventory_2_6)

first3 = inventory[:3]
print(first3)

twin_beds = inventory.count("две односпальные кровати")
print(twin_beds)

inventory.sort()
print(inventory)