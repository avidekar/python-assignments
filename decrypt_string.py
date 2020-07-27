# Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase
# characters as follows:
#
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.
#
# It's guaranteed that a unique mapping will always exist.
# Example 1:
#
# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
# Example 2:
#
# Input: s = "1326#"
# Output: "acz"
# Example 3:
#
# Input: s = "25#"
# Output: "y"
# Example 4:
#
# Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
# Output: "abcdefghijklmnopqrstuvwxyz"

def decrypt_string(input):
    length = len(input)
    index = 0
    result = ""

    while index < length:
        if index + 2 < length and input[index+2] == '#':
            result += chr(int(input[index:index+2]))
            index += 3
        else:
            result += chr(int(input[index]))
            index += 1

    print(result)

str = "10#11#12"
decrypt_string(str)