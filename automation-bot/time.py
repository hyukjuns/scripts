import time
import datetime

# epoch time
time_data = time.time()
print(time_data)

# epoch to localtime
time_data = time.ctime()
print(time_data)

# easy time
time_data = datetime.datetime.now()
print(time_data)