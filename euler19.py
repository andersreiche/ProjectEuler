from datetime import timedelta, date
import calendar
import time
start = time.time()

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def isSunday(date):
    if calendar.day_name[date.weekday()] == "Sunday":
        return True
    return False

def isFirstDayOfMonth(date):
    if date.strftime("%d") == "01":
        return True
    return False

res = 0
start_date = date(1901, 1, 1)
end_date = date(2000, 12, 31)

for single_date in daterange(start_date, end_date):
    if isSunday(single_date) and isFirstDayOfMonth(single_date):
        res += 1


elapsed = time.time() - start
print(res)
print(f"result: {res} found in {elapsed} seconds.")