#  CS 3B Intermediate Software Design in Python
#  Lab # 5
#  Module: RegEx
#  Description: This class prompts the user to insert a date, and converts
#               the date to a specific format
#  Development Env:  Windows 10
#  Version:  Python 3.11
#  Module filename:  aldosiswantoa5.py
#  Date:  3/10/23
#

# Importing Classes
import re


class datetimeConverter:
    # Constants
    MONTH_STRING = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November',
                    'December']
    REGEX_PATTERN = re.compile('^(0\d|1[0:2])/(0\d|[1-2]\d|3[0-1])/(['
                               '1-2]\d{3})$')

    """
    Constructs a datetimeConverter object that requests datetime input from 
    the user
    """
    def __init__(self):
        self.__date = None
        self.__day = None
        self.__month = None
        self.__year = None

        self.date = self.get_user_input()
        print(self.date)

    """
    Gets a date user input
    @returns user_input: the date input by the user
    """
    @staticmethod
    def get_user_input():
        user_input = input("Enter a date (mm/dd/yyyy): ")

        return user_input

    """
    Getter for __date, validates using RegEx
    @return date: the date that the user input 
    """
    @property
    def date(self):
        return 'The converted date is: ' + \
               datetimeConverter.MONTH_STRING[self.__month - 1] + ' ' + \
               self.__date[1] + ', ' + \
               str(self.__year)

    """
    Setter for __date, validates using RegEx
    @param date_user_input: the date input from the user
    """
    @date.setter
    def date(self, date_user_input):
        if datetimeConverter.REGEX_PATTERN.match(date_user_input):
            date_str = date_user_input.split('/')
            [month, day, year] = [int(date) for date in date_str]

            if month == 2:
                if self.is_leap_year(year):
                    if day > 29:
                        raise SystemExit
                else:
                    if day > 28:
                        raise SystemExit
            else:
                if month <= 7:
                    if month % 2 == 1 and day > 31:
                        raise SystemExit
                    elif month % 2 == 0 and day > 30:
                        raise SystemExit
                else:
                    if month % 2 == 1 and day > 30:
                        raise SystemExit
                    elif month % 2 == 0 and day > 31:
                        raise SystemExit

            self.__date = date_str
            self.__day = day
            self.__month = month
            self.__year = year

        else:
            raise SystemExit

    """
    Checks if date_list is a leap year
    @param year: a specified year
    @return leap_year: bool if date_list is a leap year
    """
    @staticmethod
    def is_leap_year(year):
        if (year % 4 == 0 and year % 100 != 0) or \
                (year % 400 == 0 and year % 100 == 0):
            return True
        else:
            return False
