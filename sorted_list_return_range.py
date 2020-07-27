# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# Example 1:
#
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# Example 2:
#
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

def summary_ranges(list):
    start_index = 0
    retList = []

    for index in range(len(list)):
        if index + 1 < len(list) and list[index] + 1 == list[index + 1]:
            continue

        if start_index == index:
            retList.append(str(list[start_index]))
        else:
            retList.append(str(list[start_index]) + "->" + str(list[index]))
        start_index = index + 1

    return retList

list = [0, 1, 2, 4, 5, 7]
list = [0, 2, 3, 4, 6, 8, 9]
print(list)
updated_list = summary_ranges(list)
print(updated_list)