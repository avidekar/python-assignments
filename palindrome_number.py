# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
#
# Input: 121
# Output: true
# Example 2:
#
# Input: -121
# Output: false



def checkPalindrome(input_list):
    tail = len(input_list) - 1
    head = 0
    retFlag = True

    while head <= tail:
        if input_list[head] != input_list[tail]:
            retFlag = False
            return retFlag
        head += 1
        tail -= 1

    return retFlag


input_list = [1,2,1]
flag = checkPalindrome(input_list)
print(flag)