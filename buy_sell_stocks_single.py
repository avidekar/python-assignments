# If you were only permitted to complete at most one transaction (i.e., buy one and sell one
# share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

def calMaxProfit(nums):

    profit_max = 0
    low = nums[0]

    for index in range(1, len(nums)):
        if nums[index] > low:
            if nums[index] - low > profit_max:
                profit_max = nums[index] - low
        elif nums[index] < low:
            low = nums[index]
        else:
            continue

    return profit_max

nums = [7,1,5,3,6,4]
profit = calMaxProfit(nums)
print(profit)