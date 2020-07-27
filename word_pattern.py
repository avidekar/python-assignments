# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
#
# Example 1:
#
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# Example 2:
#
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# Example 3:
#
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# Example 4:
#
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false

def checkWordPattern(input_str, pattern):

    dic = {}
    pattern_set = set()
    word_set = set()
    inputList = input_str.split(" ")
    if len(inputList) != len(pattern):
        return False

    for index in range(len(inputList)):
        if pattern[index] in dic:
            if dic[pattern[index]] != inputList[index]:
                return False
        dic[pattern[index]] = inputList[index]
        pattern_set.add(pattern[index])
        word_set.add(inputList[index])

    if len(pattern_set) != len(word_set):
        return False

    return True

pattern = "abba"
input_str = "dog dog cat dog"

retFlag = checkWordPattern(input_str, pattern)
print(retFlag)