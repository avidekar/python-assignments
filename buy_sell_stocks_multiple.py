# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
#
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Example 2:
#
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.

def calMaxProfit(prices):
    max_profit = 0
    if prices[0] < prices[1]:
        curr_price = prices[0]
        startIndex = 1
    else:
        curr_price = prices[1]
        startIndex = 2

    for index in range(startIndex, len(prices)):
        if prices[index] < prices[index - 1]:
            max_profit += prices[index - 1] - curr_price
            curr_price = prices[index]

    max_profit += prices[-1] - curr_price

    return max_profit




prices = [1,2,3,4,5]
profit = calMaxProfit(prices)
print(profit)