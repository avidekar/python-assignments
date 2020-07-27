# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false

def validAnagram(a, b):
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()

    return a == b

a = "anagram"
b = "nagaram"

retFlag = validAnagram(a, b)
print(retFlag)