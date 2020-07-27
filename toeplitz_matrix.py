# A
# matrix is Toeplitz if every
# diagonal
# from top
#
# -left
# to
# bottom - right
# has
# the
# same
# element.
#
# Now
# given
# an
# M
# x
# N
# matrix,
# return True if and only if the
# matrix is Toeplitz.
#
# Example
# 1:
#
# Input:
# matrix = [
#     [1, 2, 3, 4],
#     [5, 1, 2, 3],
#     [9, 5, 1, 2]
# ]
# Output: True
# Explanation:
# In
# the
# above
# grid, the
# diagonals
# are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In
# each
# diagonal
# all
# elements
# are
# the
# same, so
# the
# answer is True.
# Example
# 2:
#
# Input:
# matrix = [
#     [1, 2],
#     [2, 2]
# ]
# Output: False
# Explanation:
# The
# diagonal
# "[1, 2]"
# has
# different
# elements.

def confirmToeplitzMatrix(grid):

    dic = {}
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if (i-j) not in dic:
                dic[i-j] = col
            elif dic[i-j] != col:
                return False

    return True

grid = [
     [1, 2, 3, 4],
     [5, 1, 2, 3],
     [9, 5, 1, 2]
 ]
retFlag = confirmToeplitzMatrix(grid)
print(retFlag)