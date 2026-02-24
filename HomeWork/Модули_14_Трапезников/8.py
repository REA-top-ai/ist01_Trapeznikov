import random

admin_number = random.randint(1, 9)
winners_found = 0
ticket_number = 1

while winners_found < 5:
    total = sum(int(digit) for digit in str(ticket_number))
    if total % admin_number == 0:
        print(f"Выигрышный номер: {ticket_number}")
        winners_found += 1
    ticket_number += 1