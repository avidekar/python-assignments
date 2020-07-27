# Given
# an
# array
# consisting
# of
# n
# integers, find
# the
# contiguous
# subarray
# of
# given
# length
# k
# that
# has
# the
# maximum
# average
# value.And
# you
# need
# to
# output
# the
# maximum
# average
# value.
#
# Example
# 1:
#
# Input: [1, 12, -5, -6, 50, 3], k = 4
# Output: 12.75
# Explanation: Maximum
# average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75


def getMaxAvg(nums, k):

    m = a = sum((nums[:k]))

    for index in range(len(nums) - k):

        a += (nums[k + index] - nums[index])
        if a > m: m = a

    return m / k

nums = [1, 12, -5, -6, 50, 3]
k = 4
retVal = getMaxAvg(nums, k)
print(retVal)