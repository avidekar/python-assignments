# coding=utf-8
# Given an array that is sorted and then rotated around an unknown point. Find if the array has a
# pair with a given sum ‘x’. It may be assumed that all elements in the array are distinct.
#
# Examples :
# Input: arr[] = {11, 15, 6, 8, 9, 10}, x = 16
# Output: true
# There is a pair (6, 10) with sum 16
#
# Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 35
# Output: true
# There is a pair (26, 9) with sum 35
#
# Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 45
# Output: false
# There is no pair with sum 45.

def pairInSortedAndRotatedArray(nums, sum):
    n = len(nums)

    for index in range(len(nums)):
        if nums[index] > nums[index + 1]:
            break

    r = index
    l = (index + 1) % n

    while l != r:

        if nums[l] + nums[r] == sum:
            return True
        if nums[l] + nums[r] > sum:
            r = (r + n - 1) % n
        else: # nums[l] + nums[r] < sum
            l = (l + 1) % n

    return False

nums = [11, 15, 6, 8, 9, 10]
sum = 18
retFlag = pairInSortedAndRotatedArray(nums, sum)
print(retFlag)