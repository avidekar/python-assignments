# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
def validateParanthesis(input_str):
    openbracket_list = ['(', '{', '[']
    closedbracket_list = [')', '}', ']']

    stack = []

    for char in input_str:
        if char in openbracket_list:
            stack.append(char)
        else:
            if stack:
                top_element = stack.pop()
                if openbracket_list.index(top_element) != closedbracket_list.index(char):
                    return False
            else:
                return False

    # if len(stack) == 0:
    #     return True
    # else:
    #     return False

    return len(stack) == 0



input_str = "((({[]})))"
#input_str = "((({[})))"
retFlag = validateParanthesis(input_str)
print(retFlag)


str = "1.1.1.1"
