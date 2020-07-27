# Given a string which consists of lowercase or uppercase letters, find the length of the longest
# palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

import collections
def getLongestpalindrome(str):
    len = 0
    hasOdd = False
    dic = collections.Counter(str)

    for value in dic.values():
        if value % 2 != 0:
            hasOdd = True

        lenPerAlphabet = (value // 2) * 2
        len += lenPerAlphabet

    if hasOdd:
        len += 1

    return len

str = "abccccdd"
length = getLongestpalindrome(str)
print(length)