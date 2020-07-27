# Given an array with n objects colored red, white or blue, sort them in-place so that objects
# of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue
# respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
#
# Example:
#
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

def getSortedColors(nums):

    curr = p0 = 0
    p2 = len(nums) - 1

    while curr <= p2:

        if nums[curr] == 0:
            nums[curr], nums[p0] = nums[p0], nums[curr]
            p0 += 1
            curr += 1

        elif nums[curr] == 2:
            nums[curr], nums[p2] = nums[p2], nums[curr]
            p2 -= 1

        else: #nums[curr] == 1
            curr += 1

    return nums

nums = [2,0,2,1,0,1]
retList = getSortedColors(nums)
print(retList)