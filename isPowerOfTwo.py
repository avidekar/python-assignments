# Given an integer, write a function to determine if it is a power of two.
#
# Example 1:
#
# Input: 1
# Output: true
# Explanation: 20 = 1
# Example 2:
#
# Input: 16
# Output: true
# Explanation: 2^4 = 16
# Example 3:
#
# Input: 218
# Output: false


def isPowerOfTwo(num):
    if num == 0:
        return False
    while num % 2 == 0:
        num /= 2
        
    return num == 1

num = 16
retFlag = isPowerOfTwo(num)
print(retFlag)