#
# Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
#
# A lucky number is an element of the matrix such that it is the minimum element in its row
# and maximum in its column.
# Example 1:
#
# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in
# its column

def get_lucky_nums(matrix):
    result = list(set(min(r) for r in matrix) & set(max(c) for c in zip(*matrix)))
    print(result)

matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
get_lucky_nums(matrix)