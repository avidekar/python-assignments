# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


def maxSubArray(nums):
    n = len(nums)
    currSum = maxSum = nums[0]
    print("currSum - " + str(currSum))
    print("maxSum - " + str(maxSum))

    for index in range(1, n):
        currSum = max(nums[index], currSum + nums[index])
        #print("currSum - " +str(currSum))
        maxSum = max(currSum, maxSum)
        #print("maxSum - " +str(maxSum))


    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
maxVal = maxSubArray(nums)
print(maxVal)