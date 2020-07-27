# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return
# the day number of the year.
# Example 1:
#
# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.
# Example 2:
#
# Input: date = "2019-02-10"
# Output: 41
# Example 3:
#
# Input: date = "2003-03-01"
# Output: 60
# Example 4:
#
# Input: date = "2004-03-01"
# Output: 61

each_month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_day_of_the_year(date):
    year, month, day = map(int, date.split("-"))
    if (year % 400) == 0 or ((year % 4 == 0) and (year % 100 != 0)):
        days[1] = 29

    print(day + sum(each_month_days[:month-1]))

date = "2019-03-10"
get_day_of_the_year(date)