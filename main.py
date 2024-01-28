
import random

def get_numbers_ticket(min, max, quantity):
    for num in [min, max, quantity]:
        if not (1<= num <= 1000):
            return []
        random_numbers = random.sample(range(min, max+1), quantity)
        return sorted(random_numbers)
        
            
lottery_numbers = get_numbers_ticket(1, 70, 6)
print(lottery_numbers)
'''
'''
import re
def normalize_phone(phone_number):
    pattern = r"[\+,\d+]"
    normalize_phone = re.findall(pattern, phone_number)
    if len(normalize_phone) == 12:
        normalize_phone.insert(0, '+')
    elif len(normalize_phone) == 11:
        normalize_phone.insert(0, '+3')
    elif len(normalize_phone) == 10:
        normalize_phone.insert(0, '+38')
    normalize_phone = "".join(normalize_phone) 
    return normalize_phone

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
'''

'''   
import datetime as dt
from datetime import datetime as dtdt

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
 
def get_upcoming_birthdays(users=None):
    tdate = dtdt.today().date()
    birthdays = []
    for user in users:
        bdate = user["birthday"]
        bdate = str(tdate.year)+bdate[4:]
        bdate = dtdt.strptime(bdate, "%Y.%m.%d").date()
        week_day = bdate.isoweekday()
        days_between = (bdate - tdate).days
        if 0<=days_between<7:
            if week_day<6:
                birthdays.append({'name':user['name'], 'birthday':bdate.strftime("%Y.%m.%d")})
        else:
            if (bdate+dt.timedelta(days=1)).weekday()==0:
                birthdays.append({'name':user['name'], 'birthday': (bdate+dt.timedelta(days=1)).strftime("%Y.%m.%d")})
            elif (bdate+dt.timedelta(days=2)).weekday()==0:
                birthdays.append({'name':user['name'], 'birthday': (bdate+dt.timedelta(days=2)).strftime("%Y.%m.%d")})
    return birthdays

print(get_upcoming_birthdays(users))  
''' 