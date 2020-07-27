# An
# array is monotonic if it is either
# monotone
# increasing or monotone
# decreasing.
#
# An
# array
# A is monotone
# increasing if
# for all i <= j, A[i] <= A[j].An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
# Input: [1, 2, 2, 3]
# Output: true
# Example
# 2:
#
# Input: [6, 5, 4, 4]
# Output: true
# Example
# 3:
#
# Input: [1, 3, 2]
# Output: false
# Example
# 4:
#
# Input: [1, 2, 4, 5]
# Output: true
# Example
# 5:
#
# Input: [1, 1, 1]
# Output: true

# Python all() function
# The all() function returns True if all items in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the all() function all returns True

def isMonotonic(A):
    return (all(A[i] <= A[i + 1] for i in xrange(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in xrange(len(A) - 1)))

A = [1, 2, 2, 3]
retFlag = isMonotonic(A)
print(retFlag)