# Given a sequence of words, check whether it forms a valid word square.
#
# Note:
# The number of words given is at least 1 and does not exceed 500.
# Word length will be at least 1 and does not exceed 500.
# Each word contains only lowercase English alphabet a-z.
# Example 1:
#
# Input:
# [
#   "abcd",
#   "bnrt",
#   "crmy",
#   "dtye"
# ]
#
# Output:
# true
#
# Explanation:
# The first row and first column both read "abcd".
# The second row and second column both read "bnrt".
# The third row and third column both read "crmy".
# The fourth row and fourth column both read "dtye".
#
# Therefore, it is a valid word square.
# Example 2:
#
# Input:
# [
#   "abcd",
#   "bnrt",
#   "crm",
#   "dt"
# ]
#
# Output:
# true
#
# Explanation:
# The first row and first column both read "abcd".
# The second row and second column both read "bnrt".
# The third row and third column both read "crm".
# The fourth row and fourth column both read "dt".
#
# Therefore, it is a valid word square.
# Example 3:
#
# Input:
# [
#   "ball",
#   "area",
#   "read",
#   "lady"
# ]
#
# Output:
# false
#
# Explanation:
# The third row reads "read" while the third column reads "lead".
#
# Therefore, it is NOT a valid word square.

def confirmValidWordSquare(inp):

    for i in range(0, len(inp)):
        for j in range(0, len(inp[i])):
            if j >= len(inp) or i >= len(inp[j]) or inp[j][i] != inp[i][j]:
                return False

        return True

inp = [
      "abcd",
      "bnrt",
      "crmy",
      "dtye"
]
retFlag = confirmValidWordSquare(inp)
print(retFlag)