# coding=utf-8
# To implement an algorithm to determine if a string contains all unique characters.
#
# Examples:
#
# Input : s = “abcd”
# Output: True
# “abcd” doesn’t contain any duplicates. Hence the output is True.
#
#
#
# Input : s = “abbd”
# Output: False
# “abbd” contains duplicates. Hence the output is False.

def is_UniqueChars(str):
    if len(str) > 256:
        return False # str length cannot be more than 256

    ascii_set = [False] * 128

    for index in range(len(str)):
        ascii_val = ord(str[index])
        if ascii_set[ascii_val]:
            return False

        ascii_set[ascii_val] = True

    return True

str = "abcdeAe"
print(is_UniqueChars(str))
