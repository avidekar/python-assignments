# Given an integer n, find the closest integer (not including itself), which is a palindrome.
#
# The 'closest' is defined as absolute difference minimized between two integers.
# Example - Input: "123"
# Output: "121"

def get_nearest_palindrome(n):
    print("num is -> "+str(num))
    if n == '1' or int(n) < 0: return "0"
    if n == '0': return 1
    minimal = float('inf')
    # get prefix, for example, prefix is "12" for "1234", and "123" for "12345".
    l_left = (len(n) + 1) // 2
    prefix = n[:l_left]
    print("prefix is -> "+prefix)

    # Option 1: simply flipping prefix
    # if odd number of digit, omit first index
    n1 = int(prefix + prefix[::-1][int(len(n) % 2 == 1):])
    print("prefix[::-1] is -> " +str(prefix[::-1]))
    print("prefix[int(len(n) % 2 == 1):] is -> " +str(prefix[int(len(n) % 2 == 1):]))
    print(prefix[::-1][int(len(n) % 2 == 1):])
    print("n1 is -> " + str(n1))

    # Option 2: decrease prefix by 1
    n2_prefix = str(int(prefix) - 1)
    if len(n2_prefix) != len(prefix) or n2_prefix == '0':
        n2 = int('9' * (len(n) - 1))
    else:
        n2 = int(n2_prefix + n2_prefix[::-1][int(len(n) % 2 == 1):])
        print("prefix[::-1] is -> " + str(prefix[::-1]))
        print("prefix[int(len(n) % 2 == 1):] is -> " + str(prefix[int(len(n) % 2 == 1):]))
        print(prefix[::-1][int(len(n) % 2 == 1):])
    print("n2 is -> " + str(n2))

    # Option3: increase prefix by 1
    n3_prefix = str(int(prefix) + 1)
    if len(n3_prefix) != len(prefix):
        n3 = 10 ** len(n) + 1
    else:
        n3 = int(n3_prefix + n3_prefix[::-1][int(len(n) % 2 == 1):])
        print("prefix[::-1] is -> " + str(prefix[::-1]))
        print("prefix[int(len(n) % 2 == 1):] is -> " + str(prefix[int(len(n) % 2 == 1):]))
        print(prefix[::-1][int(len(n) % 2 == 1):])
    print("n3 is -> " + str(n3))

    # compare and get smallest
    ans = None
    for cand in [n3, n1, n2]:
        if abs(cand - int(n)) <= minimal and str(cand) != n:
            ans = cand
            minimal = abs(cand - int(n))

    print("ans is -> "+str(ans))

num = "1034"
get_nearest_palindrome(num)