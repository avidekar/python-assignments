# Given a string, find the length of the longest substring without repeating characters.
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

def get_longest_substring(str):

    max_len = 0
    sub = ''
    for char in str:
        if char in sub:
            sub = sub[sub.find(char)+1:]
        sub += char
        if len(sub) > max_len:
            max_len = len(sub)

    print(sub)
    print(max_len)

str = "pwwkew"
get_longest_substring(str)