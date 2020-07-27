# Students are asked to stand in non-decreasing order of heights for an annual photo.
#
# Return the minimum number of students that must move in order for all students to be standing
# in non-decreasing order of height.
#
# Notice that when a group of students is selected they can reorder in any possible way between
# themselves and the non selected students remain on their seats.

# Example 1:
#
# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation:
# Current array : [1,1,4,2,1,3]
# Target array  : [1,1,1,2,3,4]
# On index 2 (0-based) we have 4 vs 1 so we have to move this student.
# On index 4 (0-based) we have 1 vs 3 so we have to move this student.
# On index 5 (0-based) we have 3 vs 4 so we have to move this student.
# Example 2:
#
# Input: heights = [5,1,2,3,4]
# Output: 5
# Example 3:
#
# Input: heights = [1,2,3,4,5]
# Output: 0
from collections import Counter

def height_checker(heights):
    counter = Counter(heights)

    index = 0
    removal = 0
    for height in heights:
        while counter[index] == 0:
            index += 1

        print(index)
        if index != height:
            removal += 1

        counter[index] = -1
        print(counter)
    print(removal)

heights = [1,1,4,2,1,3]
height_checker(heights)