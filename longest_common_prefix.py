# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(input_list):
    retStr = ""
    if not input_list: return retStr
    if len(input_list) == 1: return input_list[0]

    input_list.sort()

    for index in range(len(input_list[0])):
        if input_list[0][index] == input_list[-1][index]:
            retStr += input_list[0][index]

    return retStr

input_list = ["flower","flow","flight"]
retStr = longestCommonPrefix((input_list))
print(retStr)
