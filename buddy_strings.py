# Given
# two
# strings
# A and B
# of
# lowercase
# letters,
# return true if and only if we
# can
# swap
# two
# letters in A
# so
# that
# the
# result
# equals
# B.
#
# Example
# 1:
#
# Input: A = "ab", B = "ba"
# Output: true
# Example
# 2:
#
# Input: A = "ab", B = "ab"
# Output: false
# Example
# 3:
#
# Input: A = "aa", B = "aa"
# Output: true
# Example
# 4:
#
# Input: A = "Given two strings A and B of lowercase letters, return true if and only if we can
# swap two letters in A so that the result equals B.
#
#
#
# Example 1:
#
# Input: A = "ab", B = "ba"
# Output: true
# Example 2:
#
# Input: A = "ab", B = "ab"
# Output: false
# Example 3:
#
# Input: A = "aa", B = "aa"
# Output: true
# Example 4:
#
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# Example 5:
#
# Input: A = "", B = "aa"
# Output: false", B = "aaaaaaacb"
# Output: true
# Example
# 5:
#
# Input: A = "", B = "aa"
# Output: false
import itertools

def buddyStrings(a, b):
    if len(a) != len(b): return False
    if a == b: # ?
        seen = set()
        for char in a:
            if char in seen:
                return True
            seen.add(char)
        return False
    else:
        pairs = []
        for char_a, char_b in itertools.izip(a, b):
            if char_a != char_b:
                pairs.append((char_a, char_b))
            if len(pairs) >= 3: return False

        return len(pairs) <= 2 and pairs[0] == pairs[1][::-1]

a = "aaaaaaabc"
b = "aaaaaaacb"

retFlag = buddyStrings(a, b)
print(retFlag)