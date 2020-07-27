#
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a maximal substring consisting of non-space characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5


def lenOfLastWord(inputStr):
    maxLength = 0
    for index in range(len(inputStr) - 1, -1, -1):
        if inputStr[index] != ' ':
            maxLength += 1
        elif maxLength > 0:
            break

    return maxLength


inputStr = "HelloWorld  "
maxLength = lenOfLastWord(inputStr)

print(maxLength)
