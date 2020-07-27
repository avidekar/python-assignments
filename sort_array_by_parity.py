# Given an array A of non-negative integers, return an array consisting of all the even elements
# of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.
# Example 1:
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

def sort_array_by_parity(arr):

    start = 0
    end = len(arr) - 1

    while start < end:

        if arr[start] % 2 == 0 and arr[end] %2 == 1:
            # best case
            start += 1
            end -= 1

        elif arr[start] % 2 == 1 and arr[end] %2 == 0:
            arr[start], arr[end] = arr[end], arr[start]

        elif arr[start] % 2 == 0:
            start += 1

        else: #arr[start] % 2 == 1:
            end -= 1

    print(arr)

arr = [3,1,2,4]
sort_array_by_parity(arr)