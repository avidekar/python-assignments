# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
#
# In one shift operation:
#
# Element at grid[i][j] moves to grid[i][j + 1].
# Element at grid[i][n - 1] moves to grid[i + 1][0].
# Element at grid[m - 1][n - 1] moves to grid[0][0].
# Return the 2D grid after applying shift operation k times.

# Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
# Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

def shift_2d_matrix(matrix, k):
    rows, cols = len(matrix), len(matrix[0])
    for index in range(k):
        new_grid = [[0] * cols for index in range(rows)]

        # Case 1 : Move everything not in the last column
        for row in range(rows):
            for col in range(cols - 1):
                new_grid[row][col+1] = matrix[row][col]

        # Case 2 : Move everything in last column, but not the last row
        for row in range(rows - 1):
            new_grid[row+1][0] = matrix[row][cols - 1]

        # Case 3 : Move the bottom right
        new_grid[0][0] = matrix[rows - 1][cols - 1]

        matrix = new_grid

    return matrix

matrix = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
ret_list = shift_2d_matrix(matrix, k)
print(ret_list)