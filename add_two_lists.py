# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

def add_two_lists(l1, l2):

    result = []
    carry = 0
    for index in range(len(l1) - 1, -1, -1):
        sum = l1[index] + l2[index] + carry
        if sum < 10:
            result.append(sum)
            carry = 0
        else:
            carry, sum = divmod(sum, 10)
            result.append(sum)

    if carry:
        result.append(carry)

    print(result)


l1= [5,4,3]
l2 = [2,6,4]
add_two_lists(l1, l2)