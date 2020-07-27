# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
import collections

def getFirstUniqueChar(str):

    counter = collections.Counter(str)

    for index, char in enumerate(str):
        if counter[char] == 1:
            return index

    return False

str = "loveleetcode"
retIndex = getFirstUniqueChar(str)
print(retIndex)

def first_non_rep_char(str):

    char_order = []
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            char_order.append(char)

    for char in char_order:
        if char_count[char] == 1:
            print(char)
            break
    print("None")

str = "PythonforallPythonMustforall"
first_non_rep_char(str)