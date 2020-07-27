# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
#
# Example 1:
#
# Input: "A man, a plan, a canal: Panama"
# Output: true


def validPalindrome(input_str):
    head = 0
    tail = len(input_str) - 1
    retFlag = True
    while head <= tail:
        while not input_str[head].isalnum():
            head += 1
        while not input_str[tail].isalnum():
            tail -= 1
        if input_str[head].lower() == input_str[tail].lower():
            head +=1
            tail -= 1
        else:
            retFlag = False
            break

    return retFlag

input_str = "A man, a plan, a canal: Panama"
flag = validPalindrome(input_str)
print(flag)