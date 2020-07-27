# Given an array of 4 digits, return the largest 24 hour time that can be made.
#
# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.
#
# Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

#Example 1:
#
# Input: [1,2,3,4]
# Output: "23:41"
# Example 2:
#
# Input: [5,5,5,5]
# Output: ""
from itertools import permutations
def construct_largest_time(arr):
    max_time = -1
    for h1,h2, m1,m2 in permutations(arr):
        hours = 10 * h1 + h2
        minutes = 10 * m1 + m2
        time = 60 * hours + minutes

        if (0 <= hours < 24) and (0 <= minutes < 60) and (time > max_time):
            max_time = time

    print("{:02}:{:02}".format(*divmod(max_time, 60)) if max_time >= 0 else "")

arr = [1,2,3,4]
construct_largest_time(arr)