#Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.
#
# If it is impossible to form any triangle of non-zero area, return 0
# #Example 1:
#
# Input: [2,1,2]
# Output: 5
# Example 2:
#
# Input: [1,2,1]
# Output: 0
# Example 3:
#
# Input: [3,2,3,4]
# Output: 10
# Example 4:
#
# Input: [3,6,2,3]
# Output: 8

def calculate_largest_perimeter_triangle(arr):
    arr.sort()
    for index in range(len(arr) - 3,-1,-1):
        if arr[index] + arr[index+1] > arr[index+2]:
            return arr[index] + arr[index+1] + arr[index+2]

arr = [3,6,2,3]
print(calculate_largest_perimeter_triangle(arr))