# Given a sorted array and a target value, return the index if the target is found. If not, return
# the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2
# Example 2:
#
# Input: [1,3,5,6], 2
# Output: 1

def searchIndexPos(input_list, val):

    # head = 0
    # tail = len(input_list) - 1
    # while head <= tail:
    #
    #     mid = int((head + tail) / 2)
    #
    #     if input_list[mid] > val:
    #         tail = mid + 1
    #     elif input_list[mid] < val:
    #         head = mid - 1
    #     else:
    #         return mid
    #         - OR -  -->

    for index, num in enumerate(input_list):
        if num >= val:
            return index
    return index + 1

input_list = [1,3,5,6]
val = 7
retVal = searchIndexPos(input_list, val)
print(retVal)
