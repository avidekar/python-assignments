# Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.
#
# A string such as "word" contains only the following valid abbreviations:
#
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".
#
# Note:
# Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.
#
# Example 1:
# Given s = "internationalization", abbr = "i12iz4n":
#
# Return true.
# Example 2:
# Given s = "apple", abbr = "a2e":
#
# Return false.

def checkValidAbbr(word, abbr):
    i = j = 0
    while j < len(abbr) and i < len(word):
        if abbr[j].isalpha():
            if abbr[j] != word[i]:
                return False
            i += 1
            j += 1
        else: # abbr[j] is num
            if abbr[j] == '0':  # to handle edge cases such as "01", which are invalid
                return False
            temp = 0
            while j < len(abbr) and abbr[j].isdigit():
                temp = temp * 10 + int(abbr[j])
                j += 1
            i += temp

    return j == len(abbr) and i == len(word)

word = "internationalization"
abbr = "i12iz4n"

retFlag = checkValidAbbr(word, abbr)
print(retFlag)