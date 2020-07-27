# Given two non-negative integers num1 and num2 represented as string, return the sum
# of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

def addStrings(num1, num2):
    len1 = len(num1)
    len2 = len(num2)
    carry = 0
    ans = []
    i = len1 - 1
    j = len2 - 1

    while i >= 0 or j >= 0:

        n1 = 0 if i < 0 else int(num1[i])
        n2 = 0 if j < 0 else int(num2[j])
        sm = n1 + n2 + carry
        ans.append(str(sm%10))
        carry = sm // 10
        i -= 1
        j -= 1

    ans = ans[::-1]
    res_str = "".join(ans)
    return str(carry) + res_str if carry else res_str

num1 = "5452"
num2 = "9790"

result = addStrings(num1, num2)
print(result)