# There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
#
# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.
#
# Note:
# All costs are positive integers.
#
# Example:
#
# Input: [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
#              Minimum cost: 2 + 5 + 3 = 10.

def getMinCost(costs):
    if not len(costs):
        return 0
    lastR, lastG, lastB = costs[0][:]
    print lastR, lastG, lastB
    for i in range(1, len(costs)):
        curR = min(lastG, lastB) + costs[i][0]
        curG = min(lastR, lastB) + costs[i][1]
        curB = min(lastR, lastG) + costs[i][2]
        lastR, lastG, lastB = curR, curG, curB
        print lastR, lastG, lastB

    return min(min(lastR, lastG), lastB)

costs = [[17,2,17],[16,16,5],[14,3,19]]
minCost = getMinCost(costs)
print minCost