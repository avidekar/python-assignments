# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

def moveZeroes(nums):
    if len(nums) == 0:
        return nums

    latestZeroFound = 0
    for index in range(len(nums)):
        if nums[index] != 0:
            nums[index], nums[latestZeroFound] = nums[latestZeroFound], nums[index]
            latestZeroFound += 1
    return nums

nums = [2,0,0,3,12]
retList = moveZeroes(nums)
print(retList)