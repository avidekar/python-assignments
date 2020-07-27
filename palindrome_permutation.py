# Given a string, determine if a permutation of the string could form a palindrome.
#
# Example 1:
#
# Input: "code"
# Output: false
# Example 2:
#
# Input: "aab"
# Output: true
# Example 3:
#
# Input: "carerac"
# Output: true

def checkForPalindrome(input_str):

    wordCount = set()
    for char in input_str:
        if char in wordCount:
            wordCount.remove(char)
        else:
            wordCount.add(char)

    return len(wordCount) <= 1

input_str = "carerac"
retFlag = checkForPalindrome(input_str)
print(retFlag)