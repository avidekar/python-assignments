# coding=utf-8
# Given a string check if it is Pangram or not. A pangram is a sentence containing every letter in the English Alphabet.
#
# Examples : The quick brown fox jumps over the lazy dog ” is a Pangram [Contains all the characters from ‘a’ to ‘z’]
# “The quick brown fox jumps over the dog” is not a Pangram [Doesn’t contains all the characters from ‘a’ to ‘z’, as ‘l’, ‘z’, ‘y’ are missing]

def checkPanagram(str):
    List = []
    # create list of 26 charecters and set false each entry
    for i in range(26):
        List.append(False)

    # converting the sentence to lowercase and iterating
    # over the sentence
    for c in str.lower():
        if not c == " ": # make sure to check for special characters
        # if any(c for c in text if not c.isalnum() and not c.isspace()):
            # make the corresponding entry True
            List[ord(c) - ord('a')] = True

    # check if any charecter is missing then return False
    for ch in List:
        if ch == False:
            return False
    return True

str = "The quick brown fox jumps over the lazy dog"
#str = "The quick brown fox jumps over the dog"
retFlag = checkPanagram(str)
print(retFlag)