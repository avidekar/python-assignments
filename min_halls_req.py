# Minimum halls required for class scheduling
# Given N lecture timings, with their start time and end time (both inclusive), the task is to find the minimum number of halls required to hold all the classes such that a single hall can be used for only one lecture at a given time. Note that the maximum end time can be 105.
#
# Examples:
#
# Input: lectures[][] = {{0, 5}, {1, 2}, {1, 10}}
# Output: 3
# All lectures must be held in different halls because
# at time instance 1 all lectures are ongoing.
#
# Input: lectures[][] = {{0, 5}, {1, 2}, {6, 10}}
# Output: 2

def getMinHalls(lectures):
    MAX = 1000001
    prefix_sum = [0] * MAX

    for index in range(len(lectures)):
        prefix_sum[lectures[index][0]] += 1
        prefix_sum[lectures[index][1] + 1] -= 1

    ans = prefix_sum[0]
    for index in range(1, MAX):
        prefix_sum[index] += prefix_sum[index - 1]
        ans = max(ans, prefix_sum[index])

    return ans

lectures = [[0,5],[1,2],[6,10]]
retCount = getMinHalls(lectures)
print(retCount)