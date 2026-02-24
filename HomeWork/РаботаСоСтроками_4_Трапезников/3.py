def account_generator(first_name, last_name):
    return first_name[:3] + last_name[:3]

first_name = input()
last_name = input()
new_account = account_generator(first_name, last_name)
print(new_account)