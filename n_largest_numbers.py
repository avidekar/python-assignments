# Given a list of integers, the task is to find N largest elements assuming size of list is
# greater than or equal o N.
#
# Examples :
#
# Input : [4, 5, 1, 2, 9]
#         N = 2
# Output :  [9, 5]
#
# Input : [81, 52, 45, 10, 3, 2, 96]
#         N = 3
# Output : [81, 96, 52]

def n_max_elements(nums, N):

    final_list = []
    for index in range(N):
        max = 0
        for num in nums:
            if num > max:
                max = num
        nums.remove(max)
        final_list.append(max)

    return final_list

nums = [81, 52, 45, 10, 3, 2, 96]
N = 3
retList = n_max_elements(nums, N)
print(retList)