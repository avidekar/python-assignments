# Given an array of integers A, return the largest integer that only occurs once.
#
# If no integer occurs once, return -1.
# Example 1:
#
# Input: [5,7,3,9,4,9,8,3,1]
# Output: 8
# Explanation:
# The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.
# Example 2:
#
# Input: [9,9,8,8]
# Output: -1
# Explanation:
# There is no number that occurs only once.
import collections
def second_largest_unique_num(arr):
    c = collections.Counter(arr)
    max_num = 0

    for num, occurence in c.items():
        if occurence == 1:
            if max_num < num:
                max_num = num

    print(max_num)

arr = [5,7,3,9,4,9,8,3,1]
second_largest_unique_num(arr)