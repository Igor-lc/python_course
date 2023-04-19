import datetime


def dates(date):
    d, m, y = date.split(".")
    yesterday = datetime.date(int(y), int(m), int(d)).replace(day=int(d) - 1).strftime("%d.%m.%Y")
    tomorrow = datetime.date(int(y), int(m), int(d)).replace(day=int(d) + 1).strftime("%d.%m.%Y")
    return yesterday, tomorrow


result = dates('12.03.2016')
print(result)  # ('11.03.2016', '13.03.2016')


def is_leap_year(year):
    if not year % 100:
        return not (year % 400)
    else:
        return (year % 4) == 0


def is_leap_year2(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return True

    return False

print(is_leap_year2(2017))
