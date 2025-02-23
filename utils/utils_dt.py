def check_if_leap_year(year):
    leap_year_check = (year % 4 == 0)
    century_check = (year % 100 == 0)
    leap_year_century_check = (year % 400 == 0)
    if century_check:
        return leap_year_century_check
    else:
        return leap_year_check


def days_in_month(month, year):
    if month == 1:
        return 31
    elif month == 2:
        if check_if_leap_year(year):
            return 29
        else:
            return 28
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif month == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    elif month == 12:
        return 31

def get_next_month_year(month, year):
    if month != 12:
        month += 1
    else:
        month = 1
        year += 1
    return month, year

def get_prev_month_year(month, year):
    if month != 1:
        month -= 1
    else:
        month = 12
        year -= 1
    return month, year

def get_days_from_start_of_year(date):
    day, month, year = date
    between = 0
    # wind days back to start of month (1st -> 1st should give 0)
    between += day - 1
    # wind months back to start of year
    while month > 1:
        month, year = get_prev_month_year(month, year)
        between += days_in_month(month, year)

    date = (1, month, year)

    return between, date

def get_date_diff_days(start_date, end_date):
    # Assuming start_date is before end_date
    day, month, year = start_date
    end_day, end_month, end_year = end_date

    diff = 0

    # wind start_date back to start of year
    diff_start_of_year, date = get_days_from_start_of_year(start_date)
    diff -= diff_start_of_year

    # match years
    if year == end_year:
        pass
    elif year < end_year:
        while year != end_year:
            if check_if_leap_year(year):
                diff += 366
            else:
                diff += 365
            year += 1
    else:
        while year != end_year:
            if check_if_leap_year(year):
                diff -= 366
            else:
                diff -= 365
            year -= 1

    # wind date forward to end_date from start of year
    diff_start_of_year, date = get_days_from_start_of_year(end_date)
    diff += diff_start_of_year

    return diff
