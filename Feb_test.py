import datetime
print(datetime.datetime.now())  
from datetime import datetime
current_datetime = datetime.now()
print(datetime.now())
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
print(current_datetime.tzinfo)

current_datetime = datetime.now()
print(current_datetime.date())
print(current_datetime.time())
print(current_datetime.date())

now = datetime.now()
day_of_week = now.weekday()

# Поверне число від 0 (понеділок) до 6 (неділя)
print(f"Сьогодні: {day_of_week}")  

from datetime import datetime

# Створення двох об'єктів datetime
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)

# Порівняння дат
print(datetime1 == datetime2)  # False, тому що дати не однакові
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2

from datetime import datetime

seventh_day_2019 = datetime(2019, 1, 7, 14)
seventh_day_2020 = datetime(2020, 1, 7, 14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)  
print(difference.total_seconds()) 

from datetime import datetime, timedelta
now = datetime.now()
future_time = now + timedelta(5, 3)
print(future_time)
print(now<future_time)
print(now<=future_time)
print(now>=future_time)

c = now - future_time
print(c)

current_datetime = datetime.now()
past_datetime = datetime(1979, 8, 5)

since1 = current_datetime - past_datetime
print(since1)

napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# Поточна дата
current_date = datetime.now()
cc = current_date - napoleon_burns_moscow
print(cc)
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(days_since)

now = datetime.now()
timestamp = datetime.timestamp(now)
print(timestamp) 

from datetime import datetime

# Поточний час
now = datetime.now()

# Конвертація datetime в timestamp
timestamp = datetime.timestamp(now)
print(timestamp)

now = datetime.now()
current_date = now.strftime("%A, %d %B %Y")
print(current_date)
current_date = now.strftime("%I-%M")
                            
print(current_date)
import random

num = random.random()
print(num)

a = 123
a = str(a)
print(f"this is {a}")
