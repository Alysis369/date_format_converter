#  CS 3B Intermediate Software Design in Python
#  Lab # 5
#  Module: RegEx
#  Description: Driver file to test different RegEx test cases.
#  Development Env:  Windows 10
#  Version:  Python 3.11
#  Module filename:  aldosiswantoa5test.py
#  Date:  3/10/23
#

# Import Classes
from aldosiswantoa5 import datetimeConverter


def main():
    # 3 valid inputs
    obj = datetimeConverter()  # 02/13/1999 VALID
    obj = datetimeConverter()  # 06/30/2001 VALID
    obj = datetimeConverter()  # 06/03/2023 VALID

    # Leap year test
    obj = datetimeConverter()  # 02/29/2000 VALID

    # Invalid datetime
    obj = datetimeConverter()  # nov/2/2933 INVALID


if __name__ == "__main__":
    main()

"""
Enter a date (mm/dd/yyyy): 02/13/1999
The converted date is: February 13, 1999
Enter a date (mm/dd/yyyy): 06/30/2001
The converted date is: June 30, 2001
Enter a date (mm/dd/yyyy): 06/03/2023
The converted date is: June 03, 2023
Enter a date (mm/dd/yyyy): 02/29/2000
The converted date is: February 29, 2000
Enter a date (mm/dd/yyyy): nov/2/2933

Process finished with exit code 0
"""