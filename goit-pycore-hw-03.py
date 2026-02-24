# Task1 - Створіть функцію get_days_from_today(date), 
# яка розраховує кількість днів між заданою датою і поточною датою

from datetime import datetime
def get_days_from_today(date: str) -> int:
    given_date = datetime.strptime(date, "%Y-%m-%d").date()
    today = datetime.today().date()
    return (today - given_date).days
print(get_days_from_today("2026-03-26"))

# Task2 - Вам необхідно написати функцію get_numbers_ticket
# (min, max, quantity), яка допоможе генерувати набір унікальних 
# випадкових чисел для таких лотерей. Вона буде повертати випадковий набір 
# чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.

import numbers
import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if min < 1 or max > 1000 or min > max:
        return []
    if quantity < 1 or quantity > (max - min + 1):
        return []

    numbers = set()
    numbers = random.sample(range(min, max + 1), quantity)

    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    return sorted(numbers)
print(get_numbers_ticket(1, 100, 5))
print(get_numbers_ticket(1, 10, 15))
print(get_numbers_ticket(10, 25, 6))
print(get_numbers_ticket(50, 80, 10))

# Task3 - вам необхідна функція, яка автоматично нормалізує номери телефонів 
# до потрібного формату, видаляючи всі зайві символи та додаючи 
# міжнародний код країни, якщо потрібно.

import re

def normalize_phone(phone_numbers: str) -> str:
    cleaned = re.sub(r"[^\d+]", "",  phone_numbers)
    if cleaned.startswith("+"):
        return cleaned
    
    elif cleaned.startswith("380"):
        return "+" + cleaned
    
    else:
        return "+38" + cleaned

print(normalize_phone("380123456789"))
print(normalize_phone("380675022218"))
print(normalize_phone("+380987654321"))

# Task4 - потрібно створити функцію get_upcoming_birthdays, 
# яка допоможе вам визначати, кого з колег потрібно привітати.

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
   
    today = datetime.today().date()
    upcoming = []

    for user in users:
        
        birth = datetime.strptime(user['birthday'], "%Y.%m.%d").date()

        birthday_this_year = birth.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        congratulation_date = birthday_this_year

        if congratulation_date.weekday() == 5:  
                congratulation_date += timedelta(days=2)
        elif congratulation_date.weekday() == 6:  
                congratulation_date += timedelta(days=1)

        upcoming.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming

