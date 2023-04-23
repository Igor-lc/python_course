import datetime
# ver 1
def dates(date):
    d, m, y = date.split(".")
    yesterday = datetime.date(int(y), int(m), int(d)).replace(day=int(d) - 1).strftime("%d.%m.%Y")
    tomorrow = datetime.date(int(y), int(m), int(d)).replace(day=int(d) + 1).strftime("%d.%m.%Y")
    return yesterday, tomorrow


# ver 2
DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS2 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    if not year % 100:
        return not (year % 400)
    else:
        return (year % 4) == 0


def dates2(date):
    day, month, year = date.split(".")
    day, month, year = int(day), int(month), int(year)

    if is_leap_year(year):
        days = DAYS2
    else:
        days = DAYS

    prev_day, prev_month, prev_year = day, month, year
    if day == 1:
        if month == 1:
            prev_year = year - 1
            prev_month = 12
        else:
            prev_month = month - 1

        prev_day = days[prev_month]
    else:
        prev_year = year
        prev_month = month
        prev_day = day - 1

    next_day, next_month, next_year = day, month, year
    if day == days[month]:
        if month == 12:
            next_year = year + 1
            next_month = 1
        else:
            next_month = month + 1
        next_day = 1
    else:
        next_year = year
        next_month = month
        next_day = day + 1

    prev_date = "{:02d}.{:02d}.{:02d}".format(prev_day, prev_month, prev_year)
    next_date = "{:02d}.{:02d}.{:02d}".format(next_day, next_month, next_year)
    return prev_date, next_date

result = dates2('12.03.2016')
print(result)


'''313. YESTERDAY AND TOMORROW
Write a dates function that takes a date string argument (the current day) and returns a tuple of two elements: the previous day and the next day, relative to the passed one.

The date argument is passed as a DD.MM.YYYY format string. The returned tuple also contains the dates as strings in the format DD.MM.YYYY. The function must take into account leap years.

result = dates('12.03.2016')
print(result)  # ('11.03.2016', '13.03.2016')'''
