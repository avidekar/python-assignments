# Alice wrote a sequence of words in CamelCase as a string of letters, , having the following properties:
#
# It is a concatenation of one or more words consisting of English letters.
# All letters in the first word are lowercase.
# For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
# Given , print the number of words in  on a new line.
#
# For example, . There are  words in the string.
#
# Function Description
#
# Complete the camelcase function in the editor below. It must return the integer number of words in the input string.
#
# camelcase has the following parameter(s):
#
# s: the string to analyze
# Input Format
#
# A single line containing string .
#
# Constraints
#
# Output Format
#
# Print the number of words in string .
#
# Sample Input
#
# saveChangesInTheEditor
# Sample Output
#
# 5

def getCount(str):
    index = 0
    count = 1
    while index <= len(str) - 1:
        if str[index].isupper():
            count += 1
        index += 1
        
    return count

str = "saveChangesInTheEditor"
retCount = getCount(str)
print(retCount)