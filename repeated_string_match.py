# coding=utf-8
# Given two strings A and B, find the minimum number of times A has to be repeated such that B
# is a substring of it. If no such solution, return -1.
#
# For example, with A = "abcd" and B = "cdabcdab".
#
# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it;
# and B is not a substring of A repeated two times ("abcdabcd").
#
# ???
#
def checkRepeatedString(a, b):

    if len(a) == 0: return -1
    if len(b) >= len(a): nrep = len(b) / len(a) + 1
    else: nrep = len(a) / len(b) + 1

    s = a * nrep
    low = 1
    high = minrep = nrep
    flag = False
    while low <= high:
        mid = low + (high - low)/2
        if b in s[0:mid * len(a)]:
            flag = True
            minrep = min(minrep, mid)
            hi = mid - 1
        else:
            lo = mid + 1
        return minrep if flag else -1



a = "abcd"
b = "cdabcdab"

retVal = checkRepeatedString(a, b)
print(retVal)