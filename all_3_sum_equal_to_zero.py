# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

def get_results(nums):
    result = []
    found = set()
    dups = set()
    seen = {}

    for i, val1 in enumerate(nums):
        if val1 not in dups:
            dups.add(val1)
        # [-1, 0, 1, 2, -1, -4]
        for j, val2 in enumerate(nums[i+1:]):
            complement = -val1 -val2
            if complement in seen and seen[complement] == i:
                min_val = min(val1, val2, complement)
                max_val = max(val1, val2, complement)
                if (min_val, max_val) not in found:
                    print("++++++++++++")
                    print(found)
                    print("++++++++++++")
                    found.add((min_val, max_val))
                    result.append([val1, val2, complement])
            seen[val2] = i
            print("----------")
            print(seen)
            print("----------")
    print(result)

nums = [-1, 0, 1, 2, -1, -4]
get_results(nums)