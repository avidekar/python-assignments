# We are given two strings, A and B.
#
# A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.
#
# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true
#
# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false

def checkStrIfRotated(A, B):
    if len(A) == len(B) == 0:
        return True
    if len(A) != len(B):
        return False
    # print B
    for index in range(len(A)):
        # rotate each letter from A to check if it matches or not.
        B = B[1:] + B[:1]
        # print B
        if A == B:
            return True

    return False

A = 'abcde'
B = 'cdeab'
retFlag = checkStrIfRotated(A, B)
print(retFlag)