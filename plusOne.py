# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

def plusOne(nums):

    length = len(nums)
    for index in range(length):
        idx = length - index - 1
        nums[idx] += 1

        if nums[idx] == 10:
            if idx == 0:
                nums[idx] = 1
                nums.append(0)
            else:
                nums[idx] = 0
                continue
        break

    return nums

nums = [9,9,9,9]
ret = plusOne(nums)

print(ret)