import utils.utils_dt as utils
import numpy as np

class DaysInPeriod:

    def __init__(self, start, end):
        self.start = start
        self.end = end

        self.month_starts = list()
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.iterate_months_years()
        # Any month_start that is divisible by 7 is a sunday (monday=1, ..., sunday=7)
        self.answer = np.sum(np.array(self.month_starts) % 7 == 0)
        print(self.answer)

    def iterate_months_years(self):
        day, month, year = self.start
        end_day, end_month, end_year = self.end

        # We know (1, 1, 1900) was a monday (1)
        reference_date = (1, 1, 1900)
        days = 1
        day_diff = utils.get_date_diff_days(reference_date, self.start)
        days += day_diff

        while (day <= end_day) & (month <= end_month) & (year <= end_year):
            self.month_starts.append(days)
            days += utils.days_in_month(month, year)
            month, year = utils.get_next_month_year(month, year)


if __name__ == '__main__':
    start = (1, 1, 1901)
    end = (31, 12, 2000)

    DaysInPeriod(start, end)
