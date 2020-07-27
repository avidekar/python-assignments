# Given an array arr[] of n integers, find the maximum that maximizes the sum of the value of i*arr[i] where i varies from 0 to n-1.
#
# Examples :
#
# Input : arr[] = {8, 3, 1, 2}
# Output : 29
# Explanation : Let us see all rotations
# {8, 3, 1, 2} = 8*0 + 3*1 + 1*2 + 2*3 = 11
# {3, 1, 2, 8} = 3*0 + 1*1 + 2*2 + 8*3 = 29
# {1, 2, 8, 3} = 1*0 + 2*1 + 8*2 + 3*3 = 27
# {2, 8, 3, 1} = 2*0 + 8*1 + 3*2 + 1*1 = 17
#
# Input : arr[] = {3, 2, 1}
# Output : 7

def maxSum(arr, n):
    # Compute sum of all array elements
    cum_sum = 0

    for i in range(0, n):
        cum_sum += arr[i]

        # Compute sum of i * arr[i] for
    # initial configuration.
    curr_val = 0

    for i in range(0, n):
        curr_val += i * arr[i]

        # Initialize result
    res = curr_val

    # Compute values for other iterations
    for i in range(1, n):
        # Compute next value using previous
        # value in O(1) time
        next_val = (curr_val - (cum_sum - arr[i - 1]) +
                    arr[i - 1] * (n - 1))

        # Update current value
        curr_val = next_val

        # Update result if required
        res = max(res, next_val)

    return res


# Driver code
arr = [8, 3, 1, 2]
n = len(arr)

print(maxSum(arr, n))