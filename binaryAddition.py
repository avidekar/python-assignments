# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"


def addBinary(a, b):

    result = []
    index_a = len(a) - 1
    index_b = len(b) - 1

    while index_a >= 0 or index_b >= 0:
        if a[index_a]:
            a_bit = a[index_a]
        else:
            a_bit = 0

        if b[index_b]:
            b_bit = b[index_b]
        else:
            b_bit = 0

        carry = '0'
        if a_bit == b_bit:
            result.append(carry)
            carry = a_bit
        else:
            if carry == '0':
                result.append('1')
            else:
                result.append('0')
                carry = '1'

        index_a -= 1
        index_b -= 1

    if carry == '1':
        result.append(carry)

    return ''.join(result[::-1])

a = "1010"
b = "1011"
result = addBinary(a, b)
print(result)