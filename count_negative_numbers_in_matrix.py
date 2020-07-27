# Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
#
# Return the number of negative numbers in grid.

# Example - Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

def get_negative_count(grid):

    count = 0
    for nums in grid:
        count += get_negative_vals_count(nums)

    print(count)

def get_negative_vals_count(nums):

    start = 0
    end = len(nums)
    while start < end:
        mid = (start + end) // 2
        if nums[mid] < 0:
            end = mid
        else:
            start = mid+1

    return len(nums) - start

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
get_negative_count(grid)