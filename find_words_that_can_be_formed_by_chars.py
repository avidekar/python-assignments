# You are given an array of strings words and a string chars.
#
# A string is good if it can be formed by characters from chars (each character can only be used once).
#
# Return the sum of lengths of all good strings in words.
# Example 1:
#
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation:
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

import collections

def find_words(words, str):
    char_dict = collections.Counter(str)
    ret_length = 0
    for word in words:
        word_dict = collections.Counter(word)
        isGood = True
        for key in word_dict:
            if ((key not in char_dict) and (word_dict[key] > char_dict[key])):
                isGood = False
                break
        if isGood:
            ret_length += len(word)

    print(ret_length)

words = ["cat","bt","hat","tree"]
chars = "atach"
find_words(words, chars)