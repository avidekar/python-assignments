# Given
# a
# string
# S and a
# character
# C,
# return an
# array
# of
# integers
# representing
# the
# shortest
# distance
# from the character
#
# C in the
# string.
#
# Example
# 1:
#
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

def shortestDist(str, char):

    prev = float('-inf')
    result = []

    for index, letter in enumerate(str):
        if letter == char:
            prev = index
        result.append(index - prev)
    print(result) # [inf, inf, inf, 0, 1, 0, 0, 1, 2, 3, 4, 0]

    prev = float('inf')
    for index in range(len(str) - 1, -1, -1):
        if str[index] == char:
            prev = index
        result[index] = min(result[index], prev - index)
    print(result) # [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
    return result

str = "loveleetcode"
char = 'e'
retList = shortestDist(str, char)
print(retList)