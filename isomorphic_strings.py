# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# Example 1:
#
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
#
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
#
# Input: s = "paper", t = "title"
# Output: true


def ifIsomorphic(a, b):
    mapping = {}
    for cs, ct in zip(a, b):
        if mapping[cs] != ct:
            return False
        if ct in mapping.values():
            return False
        mapping[cs] = ct

    return True

a = "paper"
b = "title"
retFlag = ifIsomorphic(a, b)
print(retFlag)