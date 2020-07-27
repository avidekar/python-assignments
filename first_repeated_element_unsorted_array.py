# Find the first repeating element in an array of integers
# Given an array of integers, find the first repeating element in it. We need to find the element that occurs more than once and whose index of first occurrence is smallest.
# Examples:
#
# Input:  arr[] = {10, 5, 3, 4, 3, 5, 6}
# Output: 5 [5 is the first element that repeats]
#
# Input:  arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10}
# Output: 6 [6 is the first element that repeats]

# SOLUTION IS WRONG, BUT I KNOW THE FLOW

def getRepeatedVal(nums):

    dic = {}
    firstRepeatedNum = 0
    for index, val in enumerate(nums):
        if val in dic.keys():
            if dic[val] > 0:
                dic[val] *= -1
            else: continue
        else:
            dic[val] = index + 1

    for key, val in dic.items():
        if val < 0:
            if not firstRepeatedNum:
                firstRepeatedNum = val
            else:
                if firstRepeatedNum < val:
                    firstRepeatedNum = val

    firstRepeatedNum *= -1
    return nums[firstRepeatedNum]

nums = [6, 10, 5, 4, 9, 120, 4, 6, 10]
retVal = getRepeatedVal(nums)
print(retVal)