import datetime
from dataclasses import dataclass


@dataclass
class Date:
    __day: int
    __month: int
    __year: int

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        assert isinstance(day, int), 'day must be int '
        self.__day = day

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        assert isinstance(month, int), 'month must be int '
        self.__month = month

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        assert isinstance(year, int), 'day must be int '
        self.__year = year

    # @property
    def is_leap_year(self):
        if (self.__year % 400 == 0) and (self.__year % 100 == 0):
            print("it is a leap year".format(self.__year))

        elif (self.__year % 4 == 0) and (self.__year % 100 != 0):
            print("it is a leap year".format(self.__year))

        else:
            print("is not a leap year".format(self.__year))

    def is_valid_date(self):
        is_valid_date = True
        try:
            datetime.datetime(self.__year, self.__month, self.__day)
        except ValueError:
            is_valid_date = False

        if is_valid_date:
            print("Input date is valid ..")
        else:
            print("Input date is not valid..")

    def __str__(self):
        return f'{str(self.__day).zfill(2)}/{str(self.__month).zfill(2)}/{str(self.__year).zfill(4)}'

    # @property
    # def is_leap_year(self):
    #     is_leap_year = False
    #     first = self.year % 4
    #     second = self.year % 100
    #     third = self.year % 400
    #     if first == 0 and second != 0:
    #         is_leap_year = True
    #     elif first == 0 and third == 0:
    #         is_leap_year = True
    #     return is_leap_year
    # @property
    # def is_valid_date(self):
    #     is_valid_date = False
    #     months = {1: 31, 2: [28, 29], 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    #     if self.year > 1900:
    #         if self.__month == 2:
    #             if not self.is_leap_year:
    #                 max_day = months[2][0]
    #             else:
    #                 max_day = months[2][1]
    #         else:
    #             max_day = months[self.__month]
    #         if 0 < self.__day <= max_day:
    #             is_valid_date = True
    #     return is_valid_date
    #
    # def __init__(self, year, month, day):
    #     assert isinstance(year, int) or isinstance(month, int) or isinstance(day, int), "all input  be an integer."
    #     if 0 > day > 31:
    #         raise ValueError("Invalid day.")
    #     if year < 1900:
    #         raise ValueError("Year must be greater then 1900.")
    #     if 0 > month > 12:
    #         raise ValueError("Invalid month.")
    #
    # def __str__(self):
    #     return str(self.day).zfill(2) + "/" + str(self.month).zfill(2) + "/" + str(self.year)
