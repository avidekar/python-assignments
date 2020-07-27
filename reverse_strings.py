# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]

def revString(str, k):
    rem_str = str[k:]
    rev_str = str[:k]
    start = 0

    while start < k:
        temp = rev_str[start]
        rev_str[start] = rev_str[k]
        rev_str[k] = temp
        start += 1
        k -= 1

    str = "%s%s" %(rev_str, rem_str)

    return str

str = "abcdefg"
k = 2
retStr = revString(str, k)
print(retStr)