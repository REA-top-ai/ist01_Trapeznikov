def password_generator(first_name, last_name):
    lenght1 = len(first_name)
    lenght2 = len(last_name)
    return first_name[lenght1 - 3:] + last_name[lenght2 - 3:]

first_name = input()
last_name = input()
temp_password = password_generator(first_name, last_name)
print(temp_password)