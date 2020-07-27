# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# Example 2:
#
# Given nums = [0,0,1,1,1,2,2,3,3,4],
#
# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
#
# It doesn't matter what values are set beyond the returned length.

def removeDuplicates(input_list):

    updatedIndex = 1
    for index in range(1, len(input_list)):
        if input_list[index] != input_list[index - 1]:
            input_list[updatedIndex] = input_list[index]
            updatedIndex += 1

    return updatedIndex

input_list = [0,0,1,1,1,2,2,3,3,4]
retLength = removeDuplicates(input_list)
print(retLength)

from itertools import groupby
def remove_duplicates(input_list):
    result = []
    for num, group in groupby(input_list):
        result.append(num)

    print(result)

input_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
remove_duplicates(input_list)


def remove_duplicates1(input_list):
    start = 0
    while start < len(input_list) - 1:
        if input_list[start] == input_list[start+1]:
            del input_list[start]
        else:
            start += 1

    print(input_list)

input_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
remove_duplicates1(input_list)