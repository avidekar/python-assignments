# Given an integer number n, return the difference between the product of its digits and the
# sum of its digits.

# Example 1:
#
# Input: n = 234
# Output: 15
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15

def subtract_prod_and_sum(num):
    prod = 1
    sum = 0
    while num > 0:
        num, mod = divmod(num, 10)
        prod *= mod
        sum += mod
    return (prod - sum)

num = 234
ret_val = subtract_prod_and_sum(num)
print(ret_val)