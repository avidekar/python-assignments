# A decimal number can be converted to its Hexspeak representation by first converting it to an
# uppercase hexadecimal string, then replacing all occurrences of the digit 0 with the letter O,
# and the digit 1 with the letter I.  Such a representation is valid if and only if it consists
# only of the letters in the set {"A", "B", "C", "D", "E", "F", "I", "O"}.
#
# Given a string num representing a decimal integer N, return the Hexspeak representation of N
# if it is valid, otherwise return "ERROR".

# Example 1:
#
# Input: num = "257"
# Output: "IOI"
# Explanation:  257 is 101 in hexadecimal.

def check_if_hexspeak(str):
    #print(hex(int(str)))
    #print(hex(int(str))[2:])
    val = hex(int(str))[2:].upper()
    print(val)
    d = ('A', 'B', 'C', 'D', 'E', 'F', 'I', 'O')
    result = ""

    for char in val:

        if char != '0' and char != '1' and char not in d:
            result = "ERROR"
            break
        if char == '0':
            result += 'O'
        elif char == '1':
            result += 'I'
        else:
            result += char

    print(result)

val = "257"
check_if_hexspeak(val)