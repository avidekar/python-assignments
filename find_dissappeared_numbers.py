
# coding=utf-8
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
# some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does
# not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]

def getNums(nums):

    # Iterate over each of the elements in the original array
    for i in range(len(nums)):

        # treat the value as the new index
        new_index = abs(nums[i]) - 1

        # Check the magnitude of value at this new index
        # if the magnitude is positive, make it negative
        # thus indicating that the number nums[i] has
        # appeared or has been visited.
        if nums[new_index] > 0:
            nums[new_index] *= -1

    # response array that would contain the missing numbers
    result = []

    # Iterate over the numbers from 1 to N and add all those
    # that have positive magnitude in the array
    for i in range(1, len(nums) + 1):
        if nums[i - 1] > 0:
            result.append(i)

    return result

nums = [4,3,2,7,8,2,3,1]
retList = getNums(nums)
print(retList)