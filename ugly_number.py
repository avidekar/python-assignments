# Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
# Example 1:
#
# Input: 6
# Output: true
# Example 2:
#
# Input: 8
# Output: true
# Example 3:
#
# Input: 14
# Output: false
# Explanation: 14 is not ugly since it includes another prime factor 7.

def checkUglyNumber(num):
    if num < 0:
        return False
    if num == 1:
        return True

    while num % 2 == 0:
        num = num / 2

    while num % 3 == 0:
        num = num / 3

    while num % 5 == 0:
        num = num / 5

    if num == 1:
        return True

    return False


num = 90
retFlag = checkUglyNumber(num)
print(retFlag)