# Given an integer n, return the number of trailing zeroes in n!.
#
# Example 1:
#
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:
#
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.

########### EXPLANATION ###########
#
# We add a trailing zero every time we multiply by 10 (5 * 2). Since we will have always more 2s
# than 5s, the problem is to find the number of 5s in the numbers from 1 to n.
# Let's consider 10! as example:
#
# 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
#
# In this case, we have two 5s (in 10 and 5), so the result is 2. How can we efficiently compute
# this number for a given n? Well, we could compute the multiple of 5 contained in n, but this
# is not enough: for example, 25 accounts for 2 5s, 50 accounts also for 2 5s, and so on.
#
# So, we do the following: we start from 5, and we see how many multiples of 5 we have in n.
# Then, we multiply 5 by 5 (25) and we add how many multiples of 25 we have in n. In this case
# we will not have duplicates, as at in each step we will add only one 5 to the result.

def getTrailingZeros(num):

    k, tot = 5, 0
    while k <= num:
        tot += num // k
        k *= 5

    return tot

ret = getTrailingZeros(6)
print(ret)