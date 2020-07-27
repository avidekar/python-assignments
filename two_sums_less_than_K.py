# Given an array A of integers and integer K, return the maximum S such that there exists i < j with
# A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

# Example 1:
#
# Input: A = [34,23,1,24,75,33,54,8], K = 60
# Output: 58
# Explanation:
# We can use 34 and 24 to sum 58 which is less than 60.
# Example 2:
#
# Input: A = [10,20,30], K = 15
# Output: -1
# Explanation:
# In this case it's not possible to get a pair sum less that 15.

def get_sum_of_two_less_than_final(A, K):

    A.sort()

    i = 0
    j = len(A) - 1
    min_target = -1

    while i < j:
        target = A[i] + A[j]
        if target > K:
            j -= 1

        else:
            if target > min_target and target != K:
                min_target = target
            i += 1

    print(min_target)


arr = [34,23,1,24,75,33,54,8]
K = 60
get_sum_of_two_less_than_final(arr, K)