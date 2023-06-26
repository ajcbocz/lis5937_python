from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

from datetime import timedelta

print(now + timedelta(days=1))

current_time = datetime.now;
d = timedelta(days = 100, hours = 10, minutes = 13);
print(d);

