# You are given a string s containing lowercase English letters, and a matrix shift, where
# shift[i] = [direction, amount]:
# direction can be 0 (for left shift) or 1 (for right shift).
# amount is the amount by which string s is to be shifted.
# A left shift by 1 means remove the first character of s and append it to the end.
# Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
# Return the final string after all operations.
# Input: s = "abc", shift = [[0,1],[1,2]]
# Output: "cab"
# Explanation:
# [0,1] means shift to left by 1. "abc" -> "bca"
# [1,2] means shift to right by 2. "bca" -> "cab"

def shift_string(str, shift):

    for direction, amount in shift:
        amount %= len(str)
        if direction == 0:
            str = str[amount:] + str[:amount]
        else: # direction == 1
            str = str[-amount:] + str[:-amount]

    print(str)

s = "abc"
shift = [[0, 1], [1, 2]]
shift_string(s, shift)