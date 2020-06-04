import datetime
import time

a = datetime.datetime.now()
time.sleep(2)
b = datetime.datetime.now()
c = b - a
d = c.total_seconds() * 1000
print(d)