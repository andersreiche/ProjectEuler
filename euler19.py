#Project euler problem 19

def is_leapyear(N):
    if N == 2000:
        return True
    if N%4 == 0:
        return True
    return False

days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
sundays = 0
for year in range(1901,2001):
    if is_leapyear(year):
        month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for day in month:
            if month[day]
