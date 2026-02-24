def calc_age(current_year, previous_year):
    age = current_year - previous_year
    return age

my_age = calc_age(2049, 1993)
dads_age = calc_age(2049, 1953)
print(f"Мне {my_age}, а моему отцу {dads_age} лет")