# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# 双指针 暴力破解-->超时
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # i = buy date
        # j = sell date,  sell date > buy date
        result  = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                result = max(result, profit)
        return result

# 改进1， 一次遍历，记录下每天为止的最小价格以及最大利润

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price-minprice)
        return maxprofit


#DP
# dp[i]表示前i天的最大利润
# 那第i天的最大利润就是max(dp[i-1], prices[i]-minprice)
# 边界 长度为0
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0 for i in range(n)]

        if n == 0: return 0

        minprice = prices[0]
        # 前两天最大利润= max（第一天最大利润，第二天的price- minprice）
        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i-1], prices[i]-minprice)
        # 因为dp存储的是“前n天的最大利润”，所以永远是最后一天记录的值最准确。
        return (dp[-1])


s = Solution()
s.maxProfit([7,1,5,3,6,4])

