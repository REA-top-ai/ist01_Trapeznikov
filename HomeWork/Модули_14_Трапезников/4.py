from datetime import datetime


employees = [
    ["Иванов Иван Иванович", "Менеджер", "22.10.2013", 250000],
    ["Сорокина Екатерина Матвеевна", "Аналитик", "12.03.2020", 75000],
    ["Струков Иван Сергеевич", "Старший программист", "23.04.2012", 150000],
    ["Корнеева Анна Игоревна", "Ведущий программист", "22.02.2015", 120000],
    ["Старчиков Сергей Анатольевич", "Младший программист", "12.11.2021", 50000],
    ["Бутенко Артем Андреевич", "Архитектор", "12.02.2010", 200000],
    ["Савченко Алина Сергеевна", "Старший аналитик", "13.04.2016", 100000]
]


def programmers_bonus():
    total = 0
    for emp in employees:
        if "программист" in emp[1].lower():
            total += emp[3] * 0.03
    return total

def holiday_bonus():
    total = 0
    for emp in employees:
        name_parts = emp[0].split(" ")
        if len(name_parts) > 1 and name_parts[1].endswith("a"):
            total += 2000
    return total

def index_salary():
    for emp in employees:
        hire_date = datetime.strptime(emp[2], "%d.%m.%Y")
        years_worked = (datetime.now() - hire_date).days / 365.25
        if years_worked > 10:
            emp[3] *= 1.07
        else:
            emp[3] *= 1.05
    return employees

def vacation_list():
    vacation_employees = []
    for emp in employees:
        hire_date = datetime.strptime(emp[2], "%d.%m.%Y")
        months_worked = (datetime.now() - hire_date).days / 30.44
        if months_worked > 6:
            vacation_employees.append(emp[0])
    return vacation_employees



