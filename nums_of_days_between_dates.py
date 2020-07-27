# Write a program to count the number of days between two dates.
#
# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.
# Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15
import datetime
def get_num_of_days(date1, date2):

    y1, m1, d1 = map(int, date1.split("-"))
    y2, m2, d2 = map(int, date2.split("-"))

    num_of_days = abs(int((datetime.datetime(y1,m1,d1)- datetime.datetime(y2,m2,d2)).days))
    print(num_of_days)


get_num_of_days(date1="2020-01-15", date2 = "2019-12-31")