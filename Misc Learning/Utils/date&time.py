from datetime import datetime

now = datetime.now()
print(f'Today is {now.strftime("%A, %d %b %Y")}')

# print time

from datetime import datetime
now = datetime.now()
print(f"Current time: {now.strftime('%I: %M %p')}")


# days in graduation
from datetime import datetime
now = datetime.now()

graduation = datetime(2025,8,15)

days = graduation - now

print(f"days in graduation: {days.days}")